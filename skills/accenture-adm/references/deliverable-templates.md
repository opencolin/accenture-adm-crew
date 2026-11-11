# ADM-style deliverable outlines

These outlines follow the deliverable names that appear in public ADM material. The section structure inside each one is general delivery practice, not Accenture's internal template. Scale each outline to the size and risk of the work.

## Contents

- Plan: Business Case, Solution Blueprint, Delivery Strategy, Project Plan, Entry/Exit Criteria, Roles and Responsibilities
- Analyze: Requirements, Requirements Traceability Matrix, Fit/Gap Analysis, RICEF Inventory, Test Plan
- Design: Functional Design, Interface Agreement, Data Conversion Design
- Build and Test: Test Closure Memo
- Deploy: Deployment Plan, Go Live Support Plan, Client Readiness Sign Off, Handover Documents
- Cross-stage: Stage Exit Checklist, Status Report

## Plan

### Business Case
1. Problem and opportunity
2. Options considered, including do nothing
3. Recommended option and rationale
4. Benefits: quantified, with baseline, target, owner and measurement date
5. Costs: one-off and run
6. Risks and sensitivities
7. Approval requested

### Solution Blueprint
1. Business objectives and scope (in and out)
2. Current capability assessment summary
3. Target capabilities and business processes
4. Application view: packages, custom components, integrations
5. Technical architecture view: environments, infrastructure, security
6. Data view: sources, conversion, ownership
7. Organisation, training and service model
8. Key decisions, assumptions and open questions

### Delivery Strategy
1. Delivery style per workstream (stage-gated, agile, hybrid) and why
2. Release and phasing approach
3. Sourcing and location model
4. Estimating approach (top-down now, bottom-up when inventories exist)
5. Environments and tooling
6. Governance: forums, decision rights, escalation
7. Quality approach: reviews, entry and exit criteria, metrics

### Project Plan
1. Milestones and stage dates
2. Work breakdown by stage and workstream
3. Dependencies and critical path
4. Resource plan
5. Risk, issue and change control procedures
6. Reporting cadence

### Entry/Exit Criteria

| Stage | Entry criteria | Exit criteria | Evidence | Approver |
|-------|----------------|---------------|----------|----------|

Write criteria that can be checked: "all severity 1 and 2 defects closed", not "testing is complete".

### Roles and Responsibilities

A RACI table with deliverables as rows and roles as columns. Typical roles: Project Manager, Quality Manager, Business Architect, Application Designer, Data Architect, Technical Architect, Technical Designer, Training and Performance Support Lead, Service Introduction Lead, plus client sponsor and process owners.

## Analyze

### Requirements

| ID | Requirement | Type (functional / non-functional) | Priority | Source | Acceptance criteria |
|----|-------------|-------------------------------------|----------|--------|---------------------|

Group by business process. Non-functional requirements (performance, security, availability, compliance) get the same rigour as functional ones.

### Requirements Traceability Matrix

| Req ID | Design element | Build object | Test case | Test result | Status |
|--------|----------------|--------------|-----------|-------------|--------|

Started in Plan, extended one column at a time, and updated in every stage through Test. A requirement with an empty cell at a stage exit is a gap.

### Fit/Gap Analysis

| Process / requirement | Fit (standard / configuration / gap) | Gap description | Resolution option (process change, configuration, enhancement, workaround) | Effort | Decision |
|-----------------------|----------------------------------------|-----------------|-----------------------------------------------------------------------------|--------|----------|

### RICEF Inventory

| ID | Type (Report, Interface, Conversion, Enhancement, Form, Workflow) | Description | Process area | Complexity | Estimate | Owner | Status |
|----|-------------------------------------------------------------------|-------------|--------------|------------|----------|-------|--------|

This inventory is the basis for the bottom-up estimate.

### Test Plan
1. Scope and objectives
2. Test phases (component, assembly, product/integration, performance, security, user acceptance, mock conversion) with entry and exit criteria for each
3. Environments and test data
4. Roles
5. Defect management: severity definitions, turnaround, triage
6. Schedule
7. Risks

## Design

### Functional Design (per RICEF object)
1. Purpose and business context
2. Requirements covered (IDs)
3. Functional description and process flow
4. Inputs, outputs, data mapping
5. Business rules and error handling
6. Security and authorisation
7. Test conditions
8. Assumptions and open issues

### Interface Agreement
1. Systems and owners on each side
2. Data exchanged, format, frequency, volume
3. Protocol, security, error handling and reconciliation
4. Service levels and support contacts
5. Sign-off by both owners

### Data Conversion Design
1. Objects in scope and source systems
2. Mapping and transformation rules
3. Cleansing responsibilities
4. Load sequence and tooling
5. Reconciliation and validation
6. Mock conversion schedule

## Build and Test

### Test Closure Memo
1. Test phase and scope
2. Planned versus executed and passed
3. Defects by severity: opened, closed, outstanding
4. Exit criteria status, one line each
5. Deferred items with business owner acceptance
6. Recommendation: proceed, proceed with conditions, do not proceed

## Deploy

### Deployment Plan
1. Deployment approach (big bang, phased, pilot)
2. Cutover activities with timing, owner and duration
3. Go and no-go decision points and criteria
4. Rollback plan
5. Communications
6. Business continuity during cutover

### Go Live Support Plan
1. Hypercare period and exit criteria
2. Support model: tiers, hours, contacts
3. Incident process and severity definitions
4. Monitoring
5. Transition to steady-state support

### Client Readiness Sign Off

A checklist across solution, data, people (training complete), support organisation, infrastructure and business continuity, each with status, evidence and the signing owner.

### Handover Documents
1. Solution overview and architecture
2. Operational procedures and runbooks
3. Known issues and workarounds
4. Open items and owners
5. Support contacts and service levels
6. Location of all deliverables

## Cross-stage

### Stage Exit Checklist

| Criterion | Status (met / partly / not met) | Evidence | Gap and action | Owner |
|-----------|----------------------------------|----------|----------------|-------|

Close with a recommendation and the conditions attached to it.

### Status Report
1. Overall status and trend
2. Progress against plan by workstream
3. Milestones: next four weeks
4. Top risks and issues with owners and dates
5. Decisions needed
6. Metrics: schedule variance, effort variance, defects, requirements volatility
