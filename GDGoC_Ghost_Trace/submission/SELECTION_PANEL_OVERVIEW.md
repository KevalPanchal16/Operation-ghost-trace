# Selection Panel Overview — Cybersecurity Lead

## Project
**Operation: Ghost Trace** — two original, offline CTF challenges focused on
digital forensics and network forensics.

## What has been delivered
1. **The Paper Trail (Beginner, 100 suggested points):** A log-correlation
   challenge. Players identify a suspicious backup login, correlate its
   source address with HTTP export requests, reorder fragments, and decode
   URL-safe Base64.
2. **DNS After Dark (Experienced, 300 suggested points):** A PCAP analysis
   challenge. Players identify a synthetic DNS beacon, order query-name
   fragments, Base32-decode the payload, and reverse repeating-key XOR using
   a clue in a DNS TXT response.

## Why these two challenges
The pair covers complementary, practical investigation skills without
relying on real targets or exploit development. The beginner task has a
guided, observable progression. The experienced task requires packet-level
filtering, traffic correlation, and a multi-step reconstruction process.

## Evidence and documentation
- Actual player-ready artifact files are in the two `player/` directories.
- Organizer challenge cards contain the intended flag, learning outcomes,
  player prompt, point recommendation, and three-step hint ladder.
- Organizer walkthroughs contain reproducible solve steps and expected output.
- `hosting/CTFD_HOSTING_GUIDE.md` describes CTFd setup, challenge configuration,
  pre-event testing, event-day operations, and shutdown.
- `tools/validate_artifacts.py` checks that the supplied evidence is consistent
  with the documented intended solutions.

## Safety by design
- Synthetic logs and packets only.
- Reserved documentation IP ranges only: TEST-NET-1/2/3.
- Reserved `.invalid` DNS names only.
- No malware, real credentials, personal data, or external targets.
- Challenges are solved offline from supplied evidence.

## Suggested scoring
| Challenge | Points | Rationale |
|---|---:|---|
| The Paper Trail | 100 | Introductory log correlation and encoding |
| DNS After Dark | 300 | Multi-stage packet analysis and reconstruction |

## How to review
Start with the repository README, inspect each player artifact, compare it
with its organizer challenge card and walkthrough, then run the validation
script. Organizer materials should remain private during any live CTF.

## Author reflection (to personalize before submission)
I designed the two challenges to reward investigation rather than guessing.
The first teaches participants to correlate evidence across logs; the second
asks them to reason about DNS metadata and reconstruct a message from packet
evidence. I prioritized clear scope, fair hints, reproducibility, and safe
offline execution.
