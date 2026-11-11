# Challenge 01 — The Paper Trail

**Category:** Digital Forensics / Log Analysis  
**Difficulty:** Beginner  
**Suggested value:** 100 points  
**Estimated solve time:** 10–20 minutes  
**Flag:** `GDG{logs_reveal_the_path}`

## Player prompt
A fictional Northstar Archive service recorded an unusual authentication
sequence followed by a backup export. Investigate the supplied authentication
and HTTP access logs. Correlate the suspicious session, reconstruct the
exported value, and submit the flag.

## Files supplied to players
- `CASE_BRIEF.txt`
- `auth.log`
- `web_access.log`

## Learning outcomes
- Recognize a failed-login sequence followed by a successful login.
- Correlate source addresses across log sources.
- Extract and order numbered fragments.
- Decode URL-safe Base64 using a standard tool or short script.

## Hint ladder
1. **Nudge:** Start with `auth.log`. Look for a sequence that stands out, not just a single failed login.
2. **Direction:** Correlate the successful `svc-backup` login's source address with `web_access.log`. Ignore export-looking requests from other addresses.
3. **Near-solve:** The relevant requests use `/api/export/chunk/NN`. Sort by `NN`, concatenate the `data` values, then decode URL-safe Base64 (restore `=` padding if your decoder requires it).

## Intended flag
`GDG{logs_reveal_the_path}`
