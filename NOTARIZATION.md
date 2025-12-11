# IRST — NOTARIZATION & TIMESTAMP RECORD

This file records timestamp / notarization events for IRST canonical documents.

Each entry SHOULD reference:

- which hash batch (from meta/HASHES.md) it corresponds to
- which service or mechanism was used (e.g., OpenTimestamps, other)
- where the receipt or proof is stored (path or external URL)

---

## Template for entries

A typical flow for this repo may use OpenTimestamps to anchor the SHA-256 hash batches from meta/HASHES.md onto the Bitcoin blockchain. The corresponding proof files (e.g. .ots receipts) should be stored under ots_receipts/ and referenced here.

<!--
Example (do not reuse literally):

## 2025-12-08 — Initial IRST Governance & Enforcement notarization

- Related hash batch: `Hash batch 2025-12-08T12:34:56Z` (see meta/HASHES.md)
- Scope:
  - `README.md`
  - `docs/IRST_Overview_v1.0.md`
  - `docs/IRST_Origin_Statement_v1.0.md`
  - `docs/IRST_Governance_Charter_v1.1.md`
  - `docs/IRST_Operational_Enforcement_v2.0.md`
- Service: OpenTimestamps
- Receipt file: `ots_receipts/IRST_Operational_Enforcement_v2.0.md.ots`
- Notes: first public IRST governance + enforcement snapshot.
-->

---

## Log

### 2025-12-11 — Initial IRST spec timestamping

- Scope:
  - `docs/IRST_Governance_Charter_v1.1.md`  
    - SHA-256: `6502dc8bd485114fc55ed767760cf822b972a6439ec217241052daa34e8c6eb9`
  - `docs/IRST_Operational_Enforcement_v2.0.md`  
    - SHA-256: `4c7dbba21a28abe3b15ae9f54cea4d2629a99330202726dde2fbf2fa16ebcac4`
- Service: OpenTimestamps (Bitcoin-backed timestamping)
- Proof files:
  - `ots_receipts/IRST_Governance_Charter_v1.1.md.ots`
  - `ots_receipts/IRST_Operational_Enforcement_v2.0.md.ots`
- Notes: First integrity lock-in for the core IRST governance and enforcement texts.
