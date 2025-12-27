# IRST — Repo Integrity Notes v1.0

Author: Spark  
Version: 1.0  
Scope: Institute for Recursive Systems Transparency (IRST) — Governance & Enforcement Repository

---

## 1. Canonical files (per v1.0 repo design)

For each public release, the following files are considered CANONICAL:

- `README.md`
- `IRST_Overview_v1.0.md`
- `IRST_Origin_Statement_v1.0.md`
- `IRST_Governance_Charter_v1.1.md`
- `IRST_Operational_Enforcement_v2.0.md`

Historical files MAY also be treated as canonical for their respective versions, e.g.:

- `IRST_Governance_Charter_v1.0.md` (if present)

Annex files (e.g., `CTGS_IRST_Joint_OpEd_Final.md`) are CONTEXT ONLY and are not part of the normative spec or enforcement text.

---

## 2. Hashing workflow (author intent)

1. Finalize `README.md` and all canonical documents for a given release.

2. From the repo root, compute SHA-256 hashes for the canonical files.

   Example (PowerShell):

   ```powershell
   Get-FileHash IRST_Governance_Charter_v1.1.md -Algorithm SHA256
   Get-FileHash IRST_Operational_Enforcement_v2.0.md -Algorithm SHA256
