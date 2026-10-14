"""
Autonomous Company Operator - Interactive Live Demo
Usage:
    python demo.py             (Runs in interactive mode, prompts for HITL approval)
    python demo.py --auto      (Runs in fully automated test/eval mode)
"""

import sys
import argparse
from pathlib import Path
from operator_core import AutonomousOperator
from test_operator import reset_test_environment

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def main():
    parser = argparse.ArgumentParser(description="Autonomous Company Operator Demo")
    parser.add_argument("--auto", action="store_true", help="Auto-authorize human approval steps")
    parser.add_argument("--goal", type=str, default="Reconcile pending bills in inbox, enforce spending policies, post authorized payments to ledger, and return audit proof.")
    args = parser.parse_args()

    base_dir = Path(__file__).parent.resolve()
    print("=" * 80)
    print("🤖 AUTONOMOUS COMPANY OPERATOR (AI EMPLOYEE) - LIVE DEMO")
    print("=" * 80)
    
    print("\n[SETUP] Resetting environment sandbox...")
    reset_test_environment(base_dir)
    print("  -> Workspace initialized with 3 incoming vendor bills.")
    print("  -> Company context loaded (SOP finance policy + Approved vendors).")
    
    operator = AutonomousOperator(base_dir=base_dir, auto_approve_hitl=args.auto)
    
    print(f"\n[REQUEST] Incoming Executive Directive:")
    print(f"  \"{args.goal}\"\n")
    
    # 1. Understand
    operator.understand_goal(args.goal)
    
    # 2. Plan
    operator.generate_plan()
    
    # 3. Execute, Observe, Adapt
    operator.execute_loop()
    
    # 4. Verify
    print("\n" + "-" * 80)
    print("🔍 VERIFYING REAL OUTCOMES...")
    verified = operator.verify_outcomes()
    
    # 5. Evidence & Dossier
    report_file = operator.generate_evidence_dossier()
    
    print("\n" + "=" * 80)
    print(f"🎯 TASK STATUS: {'SUCCESS - OUTCOME FULLY VERIFIED' if verified else 'FAILED'}")
    print(f"📄 Audit Evidence Generated: {report_file}")
    print(f"📊 JSON Proof Manifest: {base_dir / 'evidence' / 'audit_dossier.json'}")
    print("=" * 80)

if __name__ == "__main__":
    main()
