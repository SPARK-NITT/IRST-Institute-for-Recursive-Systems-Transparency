\# IRST — NOTARIZATION \& TIMESTAMP RECORD



This file records timestamp / notarization events for IRST canonical documents.



Each entry SHOULD reference:

\- which hash batch (from `meta/HASHES.md`) it corresponds to

\- which service or mechanism was used (e.g., OpenTimestamps, other)

\- where the receipt or proof is stored (path or external URL)



---



\## Template for entries



<!--

Example (do not reuse literally):



\## 2025-12-08 — Initial IRST Governance \& Enforcement notarization



\- Related hash batch: `Hash batch 2025-12-08T12:34:56Z` (see `meta/HASHES.md`)

\- Scope:

&nbsp; - `README.md`

&nbsp; - `docs/IRST\_Overview\_v1.0.md`

&nbsp; - `docs/IRST\_Origin\_Statement\_v1.0.md`

&nbsp; - `docs/IRST\_Governance\_Charter\_v1.1.md`

&nbsp; - `docs/IRST\_Operational\_Enforcement\_v2.0.md`

\- Service: OpenTimestamps

\- Receipt file: `receipts/2025-12-08\_ots\_proof.bin`

\- Notes: first public IRST governance + enforcement snapshot.

-->



---

A typical flow for this repo may use OpenTimestamps to anchor the SHA-256 hash batches from `meta/HASHES.md` onto the Bitcoin blockchain. The corresponding proof files (e.g. `.ots` receipts) should be stored under `receipts/` and referenced here.


\## Log



(Append notarization events here in chronological order.)




