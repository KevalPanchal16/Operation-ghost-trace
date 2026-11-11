#!/usr/bin/env python3
"""Validate Operation: Ghost Trace challenge artifacts using Python stdlib only."""
from pathlib import Path
import base64, re, struct, socket
ROOT = Path(__file__).resolve().parents[1]

# Challenge 01: correlate source, sort fragments and decode.
auth = (ROOT/'challenges/01-paper-trail/player/auth.log').read_text(encoding='utf-8')
web = (ROOT/'challenges/01-paper-trail/player/web_access.log').read_text(encoding='utf-8')
assert 'Accepted password for svc-backup from 192.0.2.44' in auth
assert auth.count('Accepted password for svc-backup from 192.0.2.44') == 1, 'Expected exactly one suspicious successful login from 192.0.2.44'
parts = {}
for line in web.splitlines():
    if not line.startswith('192.0.2.44 '):
        continue
    m = re.search(r'GET /api/export/chunk/(\d+)\?data=([A-Za-z0-9_-]+)', line)
    if m:
        parts[int(m.group(1))] = m.group(2)
assert sorted(parts) == [0,1,2,3,4], f'Unexpected chunk IDs: {sorted(parts)}'
encoded = ''.join(parts[i] for i in sorted(parts))
flag1 = base64.urlsafe_b64decode(encoded + '=' * (-len(encoded) % 4)).decode()
assert flag1 == 'GDG{logs_reveal_the_path}', flag1

# Challenge 02: minimal PCAP/DNS parser; extracts synthetic DNS queries and TXT answer.
pcap_path = ROOT/'challenges/02-dns-after-dark/player/dns_trace.pcap'
data = pcap_path.read_bytes()
assert data[:4] == bytes.fromhex('d4c3b2a1'), 'Unexpected PCAP magic/endian'
off = 24
queries = []
txt_key = None

def read_name(buf, pos):
    labels=[]
    while True:
        n=buf[pos]; pos += 1
        if n == 0: break
        if n & 0xc0: raise ValueError('Compressed name not expected in question')
        labels.append(buf[pos:pos+n].decode('ascii')); pos += n
    return '.'.join(labels), pos

while off < len(data):
    if off+16 > len(data): raise ValueError('Truncated packet header')
    ts, us, incl, orig = struct.unpack_from('<IIII', data, off); off += 16
    frame = data[off:off+incl]; off += incl
    if len(frame) != incl: raise ValueError('Truncated frame')
    if len(frame) < 14+20+8: continue
    eth_type = struct.unpack_from('!H', frame, 12)[0]
    if eth_type != 0x0800: continue
    ipoff=14
    ihl=(frame[ipoff]&0x0f)*4
    if frame[ipoff+9] != 17: continue
    src=socket.inet_ntoa(frame[ipoff+12:ipoff+16])
    udpoff=ipoff+ihl
    sport,dport,ulen,ucs=struct.unpack_from('!HHHH',frame,udpoff)
    if dport != 53 and sport != 53: continue
    dns=frame[udpoff+8:udpoff+ulen]
    if len(dns)<12: continue
    ident,flags,qd,an,ns,ar=struct.unpack_from('!HHHHHH',dns,0)
    pos=12
    if qd:
        qname,pos=read_name(dns,pos)
        qtype,qclass=struct.unpack_from('!HH',dns,pos); pos += 4
        if src == '192.0.2.10' and dport == 53 and qname.endswith('.telemetry.invalid'):
            queries.append(qname)
        if flags & 0x8000 and qname == 'key.telemetry.invalid' and an:
            # Skip answer owner name (pointer or labels), then parse TXT RR.
            if dns[pos] & 0xc0 == 0xc0: pos += 2
            else:
                _,pos=read_name(dns,pos)
            rtype,rclass,ttl,rdlen=struct.unpack_from('!HHIH',dns,pos); pos+=10
            rdata=dns[pos:pos+rdlen]
            if rtype == 16 and rdata:
                txt_key=rdata[1:1+rdata[0]].decode('ascii').split('=',1)[1].encode()

fragments={}
for q in queries:
    m=re.fullmatch(r'p(\d{2})\.([A-Z2-7]+)\.telemetry\.invalid', q)
    if m: fragments[int(m.group(1))]=m.group(2)
assert sorted(fragments) == list(range(len(fragments))) and len(fragments)>=3, fragments
assert txt_key == b'F0G-7', txt_key
b32=''.join(fragments[i] for i in sorted(fragments))
encrypted=base64.b32decode(b32 + '=' * (-len(b32)%8))
flag2=bytes(b ^ txt_key[i%len(txt_key)] for i,b in enumerate(encrypted)).decode()
assert flag2 == 'GDG{dns_fragments_reassemble}', flag2

# Ensure answer strings are absent from public/player evidence.
for path in (ROOT/'challenges').glob('*/player/*'):
    content = path.read_bytes()
    assert b'GDG{logs_reveal_the_path}' not in content
    assert b'GDG{dns_fragments_reassemble}' not in content

print('PASS — Challenge 01 recovered:', flag1)
print('PASS — Challenge 02 recovered:', flag2)
print('PASS — player artifacts do not contain either flag in plaintext')
