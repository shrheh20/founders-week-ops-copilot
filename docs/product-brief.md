# Founders Week Ops Copilot

**MVP Product Brief | Version 0.1 | October 26, 2026**

## 1. Problem Statement

Event operations teams manage information across CRM systems, registration spreadsheets, and program documents. Answering questions that require combining these sources is slow and error-prone.

In our **fictional customer scenario**, a five-person operations team manages approximately 500 startup records. Complex information requests take 15–20 minutes, while registration spreadsheets can lag behind Salesforce by up to two days. Sensitive founder and investor information also requires controlled access.

**Opportunity:** Build a unified operational assistant that provides accurate, traceable answers while reducing manual information retrieval.

## 2. Target Users

- **Event Operations Coordinator:** Searches registrations, companies, and schedules to answer operational questions.
- **Program Manager:** Reviews event status, identifies incomplete records, and approves follow-up tasks.
- **Authorized Administrator:** Manages source integrations, access permissions, and data quality issues.

## 3. MVP Capabilities

**Capability 1 — Unified Data Retrieval**

- Ingest synthetic startup, attendance, and registration records from CSV files and a mock CRM REST API.
- Validate, deduplicate, and store structured records in PostgreSQL.
- Provide search and filtering through a Streamlit interface.

**Capability 2 — Evidence-Based AI Assistance**

- Use SQL-backed read-only tools for structured operational questions.
- Retrieve relevant passages from event documents with source citations.
- Use one AI orchestrator to select tools for questions involving multiple sources.
- Explicitly indicate insufficient evidence instead of inventing answers.
- Display source records and relevant tool activity.

**Capability 3 — Human-Approved Follow-Up**

- Identify incomplete registrations and operational issues.
- Prepare draft follow-up tasks.
- Require explicit human approval before any persistent write action.
- Do not automatically send emails or external messages.

## 4. Core User Workflow

1. Operator submits a question.
2. Application validates the request and enforces permissions.
3. System selects structured search, document retrieval, or a bounded AI workflow.
4. Results are checked against available evidence.
5. Operator receives an answer with source references and freshness information.
6. When appropriate, the system prepares a follow-up task requiring human approval.

## 5. Technology Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **Operator Interface:** Streamlit
- **AI:** OpenAI Responses API with custom function tools
- **Workflow:** LangGraph for bounded state and human approval
- **Local Deployment:** Docker Compose
- **Testing and CI:** pytest, GitHub Actions

## 6. Success Metrics

The initial pilot will measure:

- **Retrieval time:** Reduce a representative 15–20-minute manual workflow to under two minutes.
- **Answer correctness:** Target at least 95% on an explicitly defined synthetic evaluation set.
- **Evidence quality:** Provide traceable sources for factual answers.
- **Security:** Zero unauthorized disclosures in defined permission tests.
- **Workflow safety:** All write actions require explicit human approval.
- **Reliability:** Handle missing, stale, malformed, or conflicting data without producing unsupported answers.

These are proposed acceptance targets, not achieved results.

## 7. MVP Boundaries

**In scope:** Synthetic records, a mock CRM API, CSV ingestion, document retrieval, SQL-backed search, a single orchestrator, approved draft actions, testing, and reproducible local deployment.

**Out of scope:** Production Salesforce integration, real attendee or founder information, autonomous email sending, multi-agent coordination, fine-tuning, Kubernetes, React, and enterprise-scale deployment.

## 8. Data and Security Constraints

Use exclusively synthetic or appropriately public data. Do not upload confidential employer, founder, investor, or attendee information into the repository or AI requests.

Enforce permissions in application code before exposing records to AI tools. Maintain source provenance and timestamps, and ensure generated instructions inside retrieved documents cannot override application permissions.

## 9. Definition of Done

A reviewer can clone the repository, configure the documented environment, start the application, search synthetic records, ask a question, inspect cited evidence, and prepare a follow-up task that requires explicit approval.

The repository will include setup documentation, sample data, automated tests, evaluation results, an architecture diagram, and a three-minute product demonstration.