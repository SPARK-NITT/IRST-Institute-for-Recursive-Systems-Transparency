\# IRST — Repo Integrity Notes v1.0



Author: Spark  

Version: 1.0  

Scope: Institute for Recursive Systems Transparency (IRST) — Governance \& Enforcement Repository



---



\## 1. Canonical files (per v1.0 repo design)



For each public release, the following files are considered CANONICAL:



\- `README.md`

\- `docs/IRST\_Overview\_v1.0.md`

\- `docs/IRST\_Origin\_Statement\_v1.0.md`

\- `docs/IRST\_Governance\_Charter\_v1.1.md`

\- `docs/IRST\_Operational\_Enforcement\_v2.0.md`



Historical files MAY also be treated as canonical for their respective versions, e.g.:



\- `docs/IRST\_Governance\_Charter\_v1.0.md` (if present)



Annex files (e.g., `annex/CTGS\_IRST\_Joint\_OpEd\_Final.md`) are CONTEXT ONLY and are not part of the normative spec or enforcement text.



---



\## 2. Hashing workflow (author intent)



1\. Finalize README and all canonical documents for a given release.

2\. From the repo root, run the helper:



&nbsp;  ```bash

&nbsp;  python scripts/hash\_utils.py README.md docs meta/HASHES.md



