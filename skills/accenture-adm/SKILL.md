---
name: accenture-adm
description: Reference and working method for Accenture Delivery Methods (ADM) and the Accenture Delivery Suite (ADS) — the six stages (Plan, Analyze, Design, Build, Test, Deploy), workstreams, deliverables, roles, estimators, stage containment and quality gates, and agile/hybrid adaptations. Use this skill whenever the user mentions ADM, ADS, "Accenture Delivery Methodology", Accenture-style delivery, stage gates or stage containment, RICEF/WRICEF inventories, or asks to plan, structure, review or document a consulting or systems-integration engagement the way Accenture would — including drafting deliverables such as a solution blueprint, delivery strategy, fit/gap analysis, requirements traceability matrix, test plan, deployment plan or stage exit checklist, even if they do not name ADM explicitly.
---

# Accenture Delivery Methods (ADM)

ADM is Accenture's corporate delivery methodology and the "methods" pillar of the Accenture Delivery Suite (ADS), alongside Tools (ADT), Architectures (ADA) and Metrics. It is a matrix of six stages crossed with workstreams, with named deliverables in each cell.

Use this skill for two kinds of request:

1. **Explain ADM**: answer questions about what it is and how it works.
2. **Apply ADM**: structure an engagement, draft a deliverable, or review work against the method.

## Be accurate about what is known

ADM is proprietary and Accenture does not publish the methods library. Everything in this skill comes from public sources of varying quality, and `references/adm-reference.md` labels each fact as Documented, Reported, or General practice. This matters because people often use ADM answers in proposals, interviews and client conversations, where a confidently invented detail does real damage.

- Say "Accenture Delivery Methods". "Methodology" and "Application Delivery Method" are misnomers; correct them gently if the user uses them.
- When asked for something the public record does not contain (the full method list, ADT tool names, task numbering rules, current-year changes, internal templates), say it is not public and offer the general-practice equivalent, labelled as such.
- Deliverable names are reliable. Deliverable ID numbers (for example PL150) come from a single public copy of ADM for SAP training material; present them as indicative.
- Do not reproduce Accenture's internal templates or claim an output is an official Accenture artefact. Outputs are "ADM-style" or "structured along ADM stages".

## The model in brief

**Stages** (the columns):

| Stage | Purpose | Signature deliverables |
|-------|---------|------------------------|
| Plan | Define the solution blueprint and organise the project | Business Case, Solution Blueprint, Delivery Strategy, Requirements, Traceability Matrix, Project Plan, Entry/Exit Criteria |
| Analyze | Gather and manage requirements; evaluate packages and infrastructure | Fit/Gap Analysis, RICEF Inventories, Business Process Design, Integration Conceptual Design, Test Plan |
| Design | Design applications, architecture, infrastructure and training | Configuration Design, Functional Designs, Data Conversion Design, Interface Agreements |
| Build | Develop applications, architecture, infrastructure and training | Technical Designs, built components, Common Test Data |
| Test | Test everything built; validate with users | Test results, Mock Conversion Plan, Test Closure Memo |
| Deploy | Roll out to the organisation | Deployment Plan, Go Live Support Plan, Client Readiness Sign Off, Handover Documents |

**Workstreams** (the rows): Project Management, Application, Technical Architecture, Training & Performance Support, Service Introduction.

**Quality spine:** entry and exit criteria per stage, stage containment (fix defects in the stage that introduced them), peer reviews of every work product, verification checkpoints at the end of key tasks, and a traceability matrix kept current from Plan through Test.

**Delivery styles:** stage-gated, agile, or hybrid. Choose per workstream, not per program.

## Explaining ADM

Read `references/adm-reference.md` before answering anything beyond the summary above. It has a table of contents; go to the relevant section. Lead with the direct answer, cite the confidence level when the fact is Reported or weaker, and include source links from the Sources section when the user is doing research.

## Applying ADM

Follow this sequence. Skip steps the user has already covered.

1. **Establish context.** You need the client or project, the type of work (custom build, package implementation, migration, managed service), size, regulatory constraints, and where in the lifecycle they are. Ask only for what is missing and material; otherwise state assumptions and proceed.
2. **Pick the delivery style.** Stage-gated when requirements are stable, dependencies are dense or sign-offs are mandated. Agile when requirements will be discovered and releases can be small. Hybrid when the program mixes both. State the choice and the reason, because the wrong style is one of the most common ways these programs fail.
3. **Scale the method.** A six-week project does not need thirteen Plan deliverables. Keep what manages real risk, merge or drop the rest, and say what you dropped. Full ceremony on small work is the main criticism of methods like this.
4. **Lay out the stage-by-workstream plan.** For each stage give purpose, activities per relevant workstream, deliverables, owner role and exit criteria. Do not leave Training & Performance Support and Service Introduction empty until Deploy; they start in Plan.
5. **Draft the requested deliverable** using the matching outline in `references/deliverable-templates.md`. Fill it with the user's specifics, not placeholders. Mark assumptions.
6. **Add the quality hooks.** Name the reviews, the exit criteria and how the deliverable traces to requirements.

For a review request ("is this plan sound?", "are we ready to exit Design?"), check the work against the stage's exit questions in the reference, report gaps in order of risk, and say what evidence would close each one.

## Output conventions

- Name the stage and workstream a deliverable belongs to.
- Use tables for stage plans, RACI and traceability; prose for rationale.
- Keep ADM terms the user will meet on a project (RICEF, stage containment, service introduction) and define them once.
- When mapping to agile, translate rather than rename: Plan becomes inception and release planning, Analyze and Design become backlog refinement and sprint-level design, Build and Test run inside sprints with a hardening or release test, Deploy becomes release and hypercare. Entry and exit criteria become Definition of Ready and Definition of Done plus release readiness.

## Reference files

- `references/adm-reference.md`: the full public-source reference with history, ADS pillars, every stage with deliverables and gate questions, workstreams, roles, method library, estimators, quality system, SAFe adaptations, myWizard, pitfalls, glossary and sources. Read the relevant section for any explanatory question or before building a stage plan.
- `references/deliverable-templates.md`: outlines for the most requested deliverables. Read when drafting one.
