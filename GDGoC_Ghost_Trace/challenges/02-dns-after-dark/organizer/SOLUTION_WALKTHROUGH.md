# Organizer Walkthrough — DNS After Dark

> Organizer-only. Do not place this file in a player download bundle.

## 1. Establish the relevant traffic
Open `dns_trace.pcap` in Wireshark. Start with:
```text
dns && ip.src == 192.0.2.10
```
The client `192.0.2.10` makes a short, regular series of queries to names
ending in `.telemetry.invalid`. Background queries from other clients are
decoys. The `.invalid` suffix is reserved and the IP addresses are from
documentation ranges; no resolution should be attempted.

## 2. Inspect the query labels and TXT clue
The relevant query names have the form:
```text
p00.<fragment>.telemetry.invalid
p01.<fragment>.telemetry.invalid
...
```
The numeric first label establishes fragment order. The DNS TXT response
for `key.telemetry.invalid` contains `rotation-key=F0G-7`.

Useful Wireshark display filters:
```text
dns.qry.name contains "telemetry.invalid" && ip.src == 192.0.2.10
dns.flags.response == 1 && dns.qry.name == "key.telemetry.invalid"
```

With tshark, list the relevant query names:
```bash
tshark -r dns_trace.pcap \
  -Y 'ip.src == 192.0.2.10 && dns.flags.response == 0 && dns.qry.name contains "telemetry.invalid"' \
  -T fields -e dns.qry.name
```

## 3. Reassemble and decode
Join the second label from `p00`, `p01`, and subsequent fragments in numeric
order. The joined text is Base32 without padding. Decode Base32, then XOR
each byte with the repeating ASCII key `F0G-7`.

Reproducible Python 3 standard-library solution (after exporting the DNS
query names and TXT key from Wireshark/tshark):
```python
import base64

fragments = [
    # Paste second labels in p00, p01, ... order.
]
encoded = ''.join(fragments)
encrypted = base64.b32decode(encoded + '=' * (-len(encoded) % 8))
key = b'F0G-7'  # from the TXT response: rotation-key=F0G-7
flag = bytes(b ^ key[i % len(key)] for i, b in enumerate(encrypted))
print(flag.decode())
```

## 4. Expected output
```text
GDG{dns_fragments_reassemble}
```

## Validation notes
- PCAP is handcrafted from synthetic Ethernet/IPv4/UDP/DNS packets.
- All source/destination IPs are documentation-only ranges.
- All queried domains end in `.invalid`; no real domain is contacted.
- The flag is not stored in plaintext in the player PCAP or prompt.
- No exploit, malware, external target, credential or real data is involved.
