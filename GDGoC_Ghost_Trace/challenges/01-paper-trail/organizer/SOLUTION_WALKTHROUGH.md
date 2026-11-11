# Organizer Walkthrough — The Paper Trail

> Organizer-only. Do not place this file in a player download bundle.

## 1. Identify the suspicious authentication sequence
Open `auth.log` and search for `svc-backup`. The notable sequence is three
failed password attempts from `192.0.2.44`, followed by a successful login
for the same account from that same address at 22:40:09 UTC.

Example:
```text
Nov  8 22:39:12 ... Failed password for svc-backup from 192.0.2.44 ...
Nov  8 22:39:31 ... Failed password for svc-backup from 192.0.2.44 ...
Nov  8 22:39:50 ... Failed password for svc-backup from 192.0.2.44 ...
Nov  8 22:40:09 ... Accepted password for svc-backup from 192.0.2.44 ...
```

## 2. Correlate with the HTTP log
Search `web_access.log` for `192.0.2.44`. The source makes five successful
requests to `/api/export/chunk/NN`. A decoy request from `192.0.2.77` is not
part of the authenticated session and must be excluded.

## 3. Extract and sort the fragments
Run this from the challenge's player directory:
```bash
python - <<'PY'
import base64, re
from urllib.parse import urlparse, parse_qs

parts = {}
for line in open('web_access.log', encoding='utf-8'):
    if not line.startswith('192.0.2.44 '):
        continue
    m = re.search(r'GET (/api/export/chunk/(\d+)\?[^ ]+)', line)
    if not m:
        continue
    chunk_id = int(m.group(2))
    query = urlparse(m.group(1)).query
    parts[chunk_id] = parse_qs(query)['data'][0]

encoded = ''.join(parts[i] for i in sorted(parts))
decoded = base64.urlsafe_b64decode(encoded + '=' * (-len(encoded) % 4))
print(decoded.decode())
PY
```

## 4. Expected output
```text
GDG{logs_reveal_the_path}
```

## Validation notes
- The challenge uses only synthetic log entries and documentation-only IPs.
- The flag is not present in plaintext in player files.
- The decoy is intentionally excluded by source/session correlation.
- The flag is recoverable with Python's standard library; no network access is needed.
