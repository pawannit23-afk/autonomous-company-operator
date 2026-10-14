# Standard Operating Procedure (SOP): Accounts Payable & Invoice Processing

## Objective
Process pending vendor bills from `workspace/inbox`, validate compliance against company policy, record transactions in `workspace/accounting/ledger.csv`, and move processed documents to `workspace/archive/`.

## Policy Rules & Permitted Actions
1. **Vendor Verification**:
   - Only process invoices from vendors listed in `company_context/approved_vendors.json`.
   - If a vendor is not listed or missing tax ID, mark as `REJECTED_UNKNOWN_VENDOR` and do NOT process.

2. **Autonomous Spending Limit**:
   - Invoices with total amount **<= $1,000.00** from approved vendors are **PERMITTED FOR AUTONOMOUS APPROVAL**.
   - Invoices with total amount **> $1,000.00** require **MANDATORY HUMAN-IN-THE-LOOP (HITL) APPROVAL**. The operator must pause and request explicit authorization from a designated company admin before posting.

3. **Ledger Integrity**:
   - Every approved payment must append: `Timestamp, Invoice_ID, Vendor, Amount_USD, Status, Approver, Verification_Hash`.
   - Prevent duplicate entries (check existing ledger records before appending).

4. **Outcome Verification Criteria**:
   - Invoices moved from inbox to archive.
   - Exact sum of ledger additions matches sum of approved invoices.
   - Return structured audit dossier with evidence and hashes.
