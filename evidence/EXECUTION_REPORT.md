# Autonomous Operator Execution Dossier

**Goal**: Reconcile pending bills in inbox, enforce spending policies, post authorized payments to ledger, and return audit proof.

**Status**: `VERIFIED_SUCCESS`

## Metrics Summary
- **Invoices Discovered**: 3
- **Invoices Approved Autonomous**: 1
- **Invoices Approved Hitl**: 1
- **Invoices Rejected Compliance**: 2
- **Total Disbursed Usd**: 3932.5

## Processed & Signed Ledger Entries
| Invoice ID | Vendor | Amount | Approver | Hash |
|---|---|---|---|---|
| INV-2026-OCT-010 | Amazon Web Services | $482.50 | AUTONOMOUS_OPERATOR | `49a4dcfaac99a0a3` |
| INV-2026-OCT-088 | Datadog | $3,450.00 | HUMAN_ADMIN_AUTHORIZED | `914f4aa9c130fe04` |

## Policy Enforcement & Error Adaptations
- {'file': 'inv_003_shadow_vendor.txt', 'resolution': 'Fallback heuristic parser extracted partial entities; flagged missing Tax ID.'}
- {'item': 'inv_003_shadow_vendor.txt', 'reason': "Unrecognized vendor 'CryptoCloud Services Ltd'. Excluded from payment queue."}
