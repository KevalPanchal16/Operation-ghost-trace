# Hosting Guide — Operation: Ghost Trace

## 1. Hosting model
Both challenges are **artifact-based**. They do not need a vulnerable web
service, shell, network listener, container target, or participant access to
an internal network. The recommended platform is CTFd: it provides challenge
pages, downloadable attachments, static flags, hints, scoring, and a
scoreboard. Upload the files as challenge attachments; do not expose the
organizer walkthroughs.

Official references:
- CTFd installation: https://docs.ctfd.io/docs/deployment/installation/
- Creating challenges: https://docs.ctfd.io/tutorials/challenges/creating-challenges/

## 2. Local pilot deployment
1. Install Docker Engine/Desktop and the Docker Compose plugin.
2. Clone the official CTFd repository:
   ```bash
   git clone https://github.com/CTFd/CTFd.git
   cd CTFd
   ```
3. Follow the current CTFd installation guide for the repository's Compose
   configuration. Set a unique, randomly generated `SECRET_KEY`; do not use
   a sample or commit the secret to Git.
4. Start the stack with:
   ```bash
   docker compose up -d
   ```
5. Open `http://localhost:8000` on the host machine and complete the initial
   administrator setup. Keep this pilot bound to localhost / a trusted local
   network; do not expose the default setup directly to the public internet.

The official CTFd installation guide notes that its default Compose setup
does not configure TLS. For a public deployment, put CTFd behind a correctly
configured HTTPS reverse proxy, restrict administrative access, use strong
credentials, keep the host and images patched, and test backups before the
event. Ask the institution's IT team to approve the host/network first.

## 3. Configure the challenges in CTFd
Create two standard challenges in the Admin Panel.

### Challenge 01 — The Paper Trail
- Name: `The Paper Trail`
- Category: `Digital Forensics`
- Value: `100` points (suggested)
- Description: copy only the player-facing incident prompt from `CHALLENGE_CARD.md`; do not paste the flag or hint ladder into the public description
- Attachments: `CASE_BRIEF.txt`, `auth.log`, `web_access.log`
- Flag type: Static
- Flag value: use the exact value in the organizer challenge card
- Hints: add the three hints from the challenge card in order (suggested unlock costs: 5, 10, 15 points)

### Challenge 02 — DNS After Dark
- Name: `DNS After Dark`
- Category: `Network Forensics`
- Value: `300` points (suggested)
- Description: copy only the player-facing incident prompt from `CHALLENGE_CARD.md`; do not paste the flag or hint ladder into the public description
- Attachments: `CASE_BRIEF.txt`, `scope_notes.txt`, `dns_trace.pcap`
- Flag type: Static
- Flag value: use the exact value in the organizer challenge card
- Hints: add the three hints from the challenge card in order (suggested unlock costs: 5, 10, 15 points)

In CTFd, challenge files, flags, and hints are configured through the
challenge editor. Check that each attachment is downloadable from a normal
participant account before publishing the challenge. Do not upload any file
from an `organizer/` directory as a participant attachment. The flag belongs
in CTFd's flag configuration, and hints belong in its hint configuration; they
should not appear in the public description or player download.

## 4. Pre-event test plan
- Create a test participant account separate from the administrator account.
- Download each attachment as the test participant.
- Solve Challenge 01 from a clean folder using only its player files.
- Solve Challenge 02 from a clean folder using only its player files and
  Wireshark or tshark.
- Submit both flags and verify that CTFd accepts the exact strings.
- Open each hint only after confirming the prior hint is visible as intended.
- Confirm organizer walkthroughs are not attached to either challenge.
- Check mobile/desktop readability of descriptions and attachment names.
- Confirm challenge visibility and event start/end settings before launch.

## 5. Event-day operations
- Assign one challenge owner and one platform/infra owner.
- Keep an offline copy of all player artifacts and the organizer solutions.
- Announce that all artifacts are synthetic and no external targets are in scope.
- Monitor CTFd health, attachment downloads, and support questions.
- If CTFd becomes unavailable, distribute the player artifact bundle locally
  and collect flags through the event's approved fallback process.
- Never distribute the organizer folder to participants.

## 6. Shutdown and cleanup
- Export the CTFd event data for archival if required.
- Disable public registration and participant access after the event.
- Remove temporary accounts and rotate any temporary credentials.
- Preserve the challenge artifacts and writeups in the organizer archive.

## 7. Scope and safety
These challenges are static forensic artifacts. No challenge requires a live
target, exploit, malware, credential guessing against a real service, or
outbound traffic. The PCAP contains only synthetic UDP/DNS packets using
documentation-only address ranges and `.invalid` names. Players must analyze
the supplied files offline and must not send packets to captured addresses.
