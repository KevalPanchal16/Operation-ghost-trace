# OPERATION: GHOST TRACE
## GDGoC NFSU Gandhinagar — Cybersecurity Lead Mission

**A two-challenge digital forensics and network forensics mini-CTF.**

This repository contains two original, offline, artifact-based challenges:

| ID | Challenge | Category | Level | Suggested points |
|---|---|---|---|---:|
| 01 | The Paper Trail | Digital Forensics / Log Analysis | Beginner | 100 |
| 02 | DNS After Dark | Network Forensics / DNS Analysis | Experienced | 300 |

### Repository layout
```text
challenges/
  01-paper-trail/
    player/       # safe-to-distribute prompt and evidence
    organizer/    # flag, hints, and full walkthrough
  02-dns-after-dark/
    player/
    organizer/
hosting/          # CTFd setup and operational checklist
tools/            # artifact validation script
submission/       # selection-panel overview and AI disclosure template
```

### Quick start for reviewers
1. Read `submission/SELECTION_PANEL_OVERVIEW.md` for the design summary.
2. Open the `player/` folders to inspect the actual challenge artifacts.
3. Open the corresponding `organizer/` folders to review flags, hint ladders,
   and full solution walkthroughs.
4. Read `hosting/CTFD_HOSTING_GUIDE.md` for the deployment plan.
5. Run `python tools/validate_artifacts.py` to perform local integrity checks.

### Important release hygiene
The `organizer/` directories contain the answers. Keep them out of any
participant-facing download bundle. For an actual event, publish only the
`player/` files to CTFd and keep organizer materials in a restricted folder.
For this selection exercise, provide the panel access to both player and
organizer material so they can evaluate the complete work.

### Safety statement
This project is entirely offline and uses fictional incident narratives,
synthetic logs, synthetic DNS traffic, documentation-only IPv4 ranges, and
the reserved `.invalid` domain. It contains no malware, exploit against a
real service, real credentials, real people’s data, or external target.

### Reproducibility
Evidence files are committed as static artifacts. The validation script
uses only Python 3's standard library. Wireshark/tshark are optional analysis
tools for the advanced challenge.
