# Autonomous Company Operator (AI Employee)
### Founding Engineer Problem Statement Submission & Working Prototype

[![Status: Production-Grade Prototype](https://img.shields.io/badge/Status-Fully%20Verified-success.svg)]()
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]()
[![Architecture: Tiered%20Action%20Loop](https://img.shields.io/badge/Architecture-Goal%E2%86%92Plan%E2%86%92Execute%E2%86%92Adapt%E2%86%92Verify-orange.svg)]()

---

## 1. Quick Start (Run & Test in 10 Seconds)

This prototype is **100% self-contained** using Python standard libraries (zero third-party dependency headaches, guaranteed to run instantly on any machine).

### Run the Interactive Live Demo:
```bash
cd autonomous_operator
python demo.py
```
*(Prompts the user interactively when human approval is required by company policy)*

### Run Automated Evaluation Mode:
```bash
python demo.py --auto
```

### Run the 12-Point Founding Engineer Verification Suite:
```bash
python test_operator.py
```

---

## 2. Executive Vision & Core Philosophy

> *"A narrow system that genuinely demonstrates autonomy is considerably more valuable than a broad prototype that only simulates it."*

### Why Most "Desktop AI Assistants" Fail in Real Companies:
1. **The Vision Trap**: Relying entirely on raw vision coordinate clicking (e.g. pure Claude Computer Use) is slow, fragile, non-deterministic, and breaks on minor UI shifts.
2. **Context Blindness**: Business requests (*"Process the invoices in the inbox"*) leave critical implicit rules unsaid (Who are approved vendors? What is our spending limit? How do we handle edge cases?).
3. **Lack of Verifiable Proof**: An AI saying *"I finished the task"* is useless without an auditable chain of evidence and cryptographic receipts.

### Our Solution: The Tiered Autonomous Operator
Our operator introduces three core innovations:
1. **Context Grounding (The "Employee Handbook")**: The operator reads company SOPs (`sop_finance_policy.md`) and vendor registries (`approved_vendors.json`) to ground actions in company law.
2. **Deterministic Policy & HITL Gates**: Autonomous actions are bounded by spending thresholds. Low-risk operations proceed without interruption; high-stakes actions pause for authorized human sign-off.
3. **Outcome Verification & Proof-of-Work**: The task is only considered "Complete" after independent numerical and cryptographic assertions pass.

---

## 3. How the 12 Problem Statement Criteria Are Satisfied

| Criterion | Implementation in Prototype | Code Reference |
| :--- | :--- | :--- |
| **1. Understanding intended outcome** | Translates high-level vague prompt into structured task intent. | `operator_core.py::understand_goal()` |
| **2. Determining what needs to be done** | Ingests company context, spending thresholds, and permitted actions. | `operator_core.py::understand_goal()` |
| **3. Planning required actions** | Decomposes task into a 6-stage milestone execution graph. | `operator_core.py::generate_plan()` |
| **4. Selecting appropriate tools** | Selects file scanner, policy engine, JSON parser, and ledger writer. | `operator_core.py::execute_loop()` |
| **5. Executing actions** | Reads inbox, processes payments, writes to ledger, moves files. | `operator_core.py::execute_loop()` |
| **6. Observing what happened** | Captures state observations after each step into an execution trace. | `operator_core.py::observe()` |
| **7. Determining next action based on result** | Evaluates compliance outcomes before deciding to approve or escalate. | `operator_core.py::execute_loop()` |
| **8. Recovering from failures (Adaptation)** | Detects malformed/unstructured documents and falls back to heuristic parsing. | `operator_core.py::parse_with_adaptation()` |
| **9. Maintaining relevant state/context** | Maintains centralized `self.state` tracking trace, plans, and active memory. | `operator_core.py::__init__()` |
| **10. Asking for human input/approval** | Triggers mandatory HITL prompt when invoice exceeds policy ($1,000 threshold). | `operator_core.py::request_human_approval()` |
| **11. Verifying requested outcome completed** | Independently asserts: inbox empty, ledger sums match, cryptographic hashes valid. | `operator_core.py::verify_outcomes()` |
| **12. Returning evidence & summary** | Generates `audit_dossier.json` and human-readable `EXECUTION_REPORT.md`. | `operator_core.py::generate_evidence_dossier()` |

---

## 4. The Core Loop in Action

```
[ User Prompt ]
      │
      ▼
┌──────────────┐
│  UNDERSTAND  │ ◄─── Ingests sop_finance_policy.md & approved_vendors.json
└──────┬───────┘
      ▼
┌──────────────┐
│     PLAN     │ ───► Generates Milestone Execution DAG (6 Milestones)
└──────┬───────┘
      ▼
┌──────────────┐
│   EXECUTE    │ ───► Discovers invoices in workspace/inbox
└──────┬───────┘
      ▼
┌──────────────┐
│   OBSERVE    │ ───► Discovers: 1 Standard ($482), 1 High-Value ($3,450), 1 Unstructured (.txt)
└──────┬───────┘
      ▼
┌──────────────┐
│    ADAPT     │ ───► Heuristic parser recovers partial data; Policy rejects unknown vendor
└──────┬───────┘
      ▼
┌──────────────┐
│  HITL GATE   │ ───► High-value invoice triggers Human-In-The-Loop approval gate
└──────┬───────┘
      ▼
┌──────────────┐
│    VERIFY    │ ───► Independent mathematical balance check + SHA256 receipt validation
└──────┬───────┘
      ▼
┌──────────────┐
│   COMPLETE   │ ───► Outputs audit_dossier.json & EXECUTION_REPORT.md
└──────────────┘
```

---

## 5. Directory Structure

```
autonomous_operator/
├── operator_core.py            # Core Autonomous Operator engine (Loop implementation)
├── demo.py                     # Interactive and automated CLI runner
├── test_operator.py            # Complete 12-criterion test suite
├── README.md                   # Project documentation
├── SUBMISSION.md               # Founding Engineer architectural writeup
├── company_context/            # Implicit knowledge repository
│   ├── sop_finance_policy.md   # Company standard operating procedure
│   └── approved_vendors.json   # Permitted vendors and tax IDs
├── workspace/                  # Operating environment
│   ├── inbox/                  # Incoming files
│   ├── accounting/             # Target business systems (ledger.csv)
│   └── archive/                # Processed document archive
└── evidence/                   # Generated Proof-of-Work
    ├── audit_dossier.json      # Structured machine-readable audit trail
    └── EXECUTION_REPORT.md     # Executive summary & verification report
```

---

## 6. Scaling to Production (Founding Engineer Roadmap)

1. **Browser & SaaS Action Layer**: Wrap Playwright with semantic DOM accessibility trees (aria-labels, test-ids) rather than screen coordinates.
2. **Sandboxed Sub-Operators**: Run each milestone inside an ephemeral Docker container with fine-grained API credentials.
3. **Policy-as-Code**: Express company boundaries in OPA (Open Policy Agent) or Rego for auditable enterprise permission boundaries.
4. **Active Learning from Corrections**: When a human modifies a plan or rejects an approval, store the rationale in vector memory to refine future proposals.
