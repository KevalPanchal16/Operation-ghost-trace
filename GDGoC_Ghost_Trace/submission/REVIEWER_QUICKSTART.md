# Reviewer Quickstart

A reviewer can validate this submission in approximately 10–15 minutes.

1. Read `README.md` and `submission/SELECTION_PANEL_OVERVIEW.md`.
2. Open `challenges/01-paper-trail/player/CASE_BRIEF.txt`; inspect both logs.
3. Compare the intended route in `challenges/01-paper-trail/organizer/SOLUTION_WALKTHROUGH.md`.
4. Open `challenges/02-dns-after-dark/player/CASE_BRIEF.txt` and inspect `dns_trace.pcap` in Wireshark.
5. Compare the intended packet-analysis path in `challenges/02-dns-after-dark/organizer/SOLUTION_WALKTHROUGH.md`.
6. Run `python tools/validate_artifacts.py` to independently reconstruct both flags from the supplied artifacts.
7. Review `hosting/CTFD_HOSTING_GUIDE.md` for CTFd configuration, testing, and operational controls.

**Expected validation result:** both flags are recovered exactly, and neither flag appears in plaintext in player-facing files.
