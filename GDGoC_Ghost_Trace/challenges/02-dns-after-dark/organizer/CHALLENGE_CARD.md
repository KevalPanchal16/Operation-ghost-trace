# Challenge 02 — DNS After Dark

**Category:** Network Forensics / DNS Analysis  
**Difficulty:** Experienced  
**Suggested value:** 300 points  
**Estimated solve time:** 30–60 minutes  
**Flag:** `GDG{dns_fragments_reassemble}`

## Player prompt
A fictional lab sensor captured a burst of DNS traffic after an internal
endpoint began making unusual lookups. Analyze the supplied PCAP, identify
the relevant client and DNS zone, reconstruct the message sent in query
names, and recover the flag.

## Files supplied to players
- `CASE_BRIEF.txt`
- `scope_notes.txt`
- `dns_trace.pcap`

## Learning outcomes
- Filter and investigate DNS traffic in a packet capture.
- Distinguish a periodic beacon from unrelated background lookups.
- Reconstruct indexed fragments from DNS query labels.
- Recognize and reverse Base32 plus repeating-key XOR using a TXT record.

## Hint ladder
1. **Nudge:** DNS lookups are not only about resolving names. Inspect the query names and look for repetition in both the client and destination zone.
2. **Direction:** Focus on client `192.0.2.10` and query names ending in `.telemetry.invalid`. The first label is a sequence number; the next label carries a fragment. Also inspect TXT answers in the same zone.
3. **Near-solve:** Sort `p00`, `p01`, … numerically and concatenate their second labels. Base32-decode the result. The TXT answer for `key.telemetry.invalid` gives the repeating XOR key; XOR the decoded bytes with that key to obtain the flag.

## Intended flag
`GDG{dns_fragments_reassemble}`
