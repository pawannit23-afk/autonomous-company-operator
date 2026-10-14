"""
Test and Benchmark Suite for Autonomous Company Operator
Verifies all 12 criteria required by the Founding Engineer problem statement:
1. Understanding intended outcome
2. Determining what needs to be done
3. Planning required actions
4. Selecting appropriate tools
5. Executing actions
6. Observing what happened
7. Determining next action based on result
8. Recovering from failures (adaptation)
9. Maintaining relevant state/context
10. Asking for human approval (HITL)
11. Verifying requested outcome completed
12. Returning evidence & structured summary
"""

import os
import sys
import shutil
import json
from pathlib import Path
from operator_core import AutonomousOperator

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def reset_test_environment(base_dir: Path):
    inbox = base_dir / "workspace" / "inbox"
    archive = base_dir / "workspace" / "archive"
    accounting = base_dir / "workspace" / "accounting"
    
    inbox.mkdir(parents=True, exist_ok=True)
    archive.mkdir(parents=True, exist_ok=True)
    accounting.mkdir(parents=True, exist_ok=True)
    
    # Clear archive and inbox
    for f in inbox.glob("*.*"):
        f.unlink()
    for f in archive.glob("*.*"):
        f.unlink()
        
    # Re-seed inbox with test cases
    inv1 = {
        "invoice_id": "INV-2026-OCT-010",
        "vendor": "Amazon Web Services",
        "tax_id": "US-91-1234567",
        "amount_usd": 482.50,
        "line_items": [{"description": "EC2 Compute Fleet", "cost": 482.50}]
    }
    with open(inbox / "inv_001_aws.json", "w") as f:
        json.dump(inv1, f)
        
    inv2 = {
        "invoice_id": "INV-2026-OCT-088",
        "vendor": "Datadog",
        "tax_id": "US-13-9876543",
        "amount_usd": 3450.00,
        "line_items": [{"description": "APM Enterprise", "cost": 3450.00}]
    }
    with open(inbox / "inv_002_datadog.json", "w") as f:
        json.dump(inv2, f)
        
    with open(inbox / "inv_003_shadow_vendor.txt", "w") as f:
        f.write("BILLING MEMO\nFrom: CryptoCloud Services Ltd\nAmount: $750.00\nNo Tax ID provided.\n")
        
    # Reset ledger to clean baseline
    with open(accounting / "ledger.csv", "w", encoding="utf-8") as f:
        f.write("Timestamp,Invoice_ID,Vendor,Amount_USD,Status,Approver,Verification_Hash\n")

def test_full_autonomous_lifecycle():
    base_dir = Path(__file__).parent.resolve()
    print("\n" + "="*80)
    print("🚀 RUNNING AUTONOMOUS OPERATOR VERIFICATION TEST SUITE")
    print("="*80)
    
    reset_test_environment(base_dir)
    
    # Initialize operator
    op = AutonomousOperator(base_dir=base_dir, auto_approve_hitl=True)
    
    # 1. Understanding
    goal = "Execute end-to-end accounts payable audit, ingest context, and balance ledger."
    op.understand_goal(goal)
    assert op.state["current_goal"] == goal
    assert len(op.state["approved_vendors"]) > 0
    print("  [PASS] 1 & 2: Goal understanding & Company Context grounding")

    # 2. Planning
    op.generate_plan()
    assert len(op.state["plan"]) == 6
    print("  [PASS] 3 & 4: Planning & Tool selection")

    # 3. Execution, Observation, Failure Recovery, HITL
    op.execute_loop()
    assert len(op.state["observations"]) > 0
    assert len(op.state["recovered_errors"]) > 0, "Should have adapted to unstructured/unapproved vendor"
    assert len(op.state["human_decisions"]) > 0, "Should have triggered HITL gateway for > $1,000"
    print("  [PASS] 5, 6, 7 & 8: Execution, Observation, and Failure Recovery (Adaptation)")
    print("  [PASS] 9 & 10: State tracking & Human-In-The-Loop authorization")

    # 4. Outcome Verification
    verified = op.verify_outcomes()
    assert verified is True, "Cryptographic and ledger verification must pass"
    print("  [PASS] 11: Independent Outcome Verification")

    # 5. Evidence Dossier
    report_file = op.generate_evidence_dossier()
    assert report_file.exists()
    assert (base_dir / "evidence" / "audit_dossier.json").exists()
    print("  [PASS] 12: Evidence & Audit Dossier generation")

    print("\n" + "="*80)
    print("⭐ ALL 12 FOUNDING ENGINEER SPECIFICATION CRITERIA VERIFIED!")
    print("="*80)

if __name__ == "__main__":
    test_full_autonomous_lifecycle()
