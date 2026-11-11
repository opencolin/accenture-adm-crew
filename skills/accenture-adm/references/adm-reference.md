# Accenture Delivery Methods (ADM)

Accenture Delivery Methods (ADM) is Accenture's corporate methodology for planning, building and deploying client solutions. It is the "methods" pillar of the Accenture Delivery Suite (ADS). ADM is usually drawn as a matrix: six **stages** (Plan, Analyze, Design, Build, Test, Deploy) crossed with **workstreams** (Project Management, Application, Technical Architecture, Training & Performance Support, Service Introduction), with named deliverables in each cell.

> **Note:** ADM is proprietary. Accenture does not publish the methods library, so this page is assembled from public material: an Accenture government proposal, Accenture newsroom and point-of-view papers, conference decks, training material that has leaked into the public web, and third-party summaries. Each section says how well its content is sourced. Where a detail is general delivery practice rather than a documented ADM fact, it is labelled as such.

## Contents

- At a glance
- Confidence levels used on this page
- History
- The Accenture Delivery Suite (ADS)
- How ADM is structured
- The six stages
- Workstreams
- Roles
- The method library
- Estimators
- Tools, architectures and metrics
- Quality management
- Agile, DevOps and hybrid delivery
- Automation: myWizard
- Applying ADM-style delivery
- How ADM relates to other frameworks
- Glossary
- Sources

## At a glance

| Item | Summary |
|------|---------|
| Full name | Accenture Delivery Methods. "Accenture Delivery Methodology" and "Application Delivery Method" are common misnomers. |
| Owner | Accenture |
| Parent framework | Accenture Delivery Suite (ADS) |
| Lifecycle | Plan → Analyze → Design → Build → Test → Deploy |
| Workstreams | Project Management, Application, Technical Architecture, Training & Performance Support, Service Introduction |
| Types of work | Custom development, package implementation (for example SAP), outsourcing and application management |
| Quality basis | Stage containment, embedded verification checkpoints, peer reviews, the Quality and Process Improvement (QPI) program, CMMI and ISO 9001 alignment |
| Delivery styles | Stage-gated (waterfall), agile, and hybrid |

## Confidence levels used on this page

| Label | Meaning |
|-------|---------|
| **Documented** | Stated by Accenture itself, or in Accenture training material quoted publicly |
| **Reported** | Stated by a third party (dissertation, framework guide, quiz site); plausible but not confirmed by Accenture |
| **General practice** | Standard delivery practice added to make the page usable; not claimed as ADM content |

## History

- **Before ADM.** Accenture's 2003 US-VISIT proposal to the US Department of Homeland Security describes a methodology "based on over 30 years of experience" and refined across more than 5,000 projects, and names the Business Integration Methodology (BIM) as a predecessor. *(Documented)*
- **Early 2000s.** The same proposal refers to "Global Accenture methods and tools that are part of the Accenture Delivery Suite (ADS)" and calls ADM "our corporate methodology". ADS training material carries a 2004 copyright. *(Documented)*
- **2002–2005.** Accenture's Government Operating Unit was appraised at CMMI Level 3 in May 2002, with Level 4 following in 2004, and a 2005 conference deck describes an enterprise-wide CMMI rollout in which "all Accenture people, regardless of where they are located, use the same methodology". *(Documented)*
- **2007–2008.** An "Accenture Delivery Methods Estimator" appears in software catalogues, reaching version 3.0 in 2008. *(Reported)*
- **2016 onward.** Accenture launched the myWizard intelligent automation platform for application services in April 2016 and a new generation in September 2020. No public source ties myWizard to ADM by name, but it automates the same delivery lifecycle. *(Documented, link to ADM inferred)*
- **2021.** Accenture published "SAFe for Enterprise Solutions", its adaptation of the Scaled Agile Framework for SAP, Oracle and Workday programs. *(Documented)*

No public source describes the current (2024 onward) state of the ADM library.

## The Accenture Delivery Suite (ADS)

ADS "provides an integrated set of methods, tools and architectures to support systems delivery". ADM is one of its pillars. *(Documented)*

| Pillar | What it is |
|--------|-----------|
| **Accenture Delivery Methods (ADM)** | "Proven processes, deliverables and techniques that enable global teams to define what to do and how to do it." Includes estimators and step-by-step procedures. |
| **Accenture Delivery Tools (ADT)** | "A recommended toolset, comprised of vendor-provided tools and internally developed Accenture tools" covering the development lifecycle. Variants exist per platform, such as ADT for SAP. |
| **Accenture Delivery Architectures (ADA)** | "Technical architectures that provide proven structured application frameworks and reusable components." |
| **Accenture Delivery Metrics** | "A core set of metrics to measure key engagement delivery processes." |

Sources disagree on the count. Most list the four pillars above; one lists six by splitting out Estimators and Procedures as separate items. Quiz sites that list "Deliverables" and "Process" as pillars are not reliable.

Stated benefits of ADS and ADM: lower cost through reuse, reduced risk, higher productivity, greater predictability, higher quality with less rework, better coordination across sites, and consistent skills and language across teams. *(Documented)*

## How ADM is structured

ADM is described as:

- "A comprehensive library of methods that supports multiple types of work"
- "Built on a common framework to promote growth of consistent skills"
- Defining "standard language, roles and deliverables"
- Including "estimators for estimating level of effort" and "repeatable, step-by-step procedures to drive consistency"
- "Focused on the fundamentals and discipline, especially around program and project management"

*(Documented)*

The method is a matrix. In Accenture's words, "the vertical bars are stages of work in a project" and "the horizontal bars are workstreams defined as domain or area of work".

```
                     Plan   Analyze   Design   Build   Test   Deploy
Project Management    ■        ■        ■        ■       ■       ■
Application           ■        ■        ■        ■       ■       ■
Technical Architecture■        ■        ■        ■       ■       ■
Training & Perf. Supp.■        ■        ■        ■       ■       ■
Service Introduction  ■        ■        ■        ■       ■       ■
```

Each cell holds activities and tasks that produce deliverables. Deliverables carry an ID made of a two-letter prefix and three digits (for example `PL150 Solution Blueprint`). An Accenture course description lists the method's layers as methods, processes, activities, tasks, tools, architecture assets and a library repository. The exact hierarchy and the numbering rule are not public.

## The six stages

Stage purposes are quoted from ADM for SAP training material *(Documented)*. Deliverable IDs come from one public copy of that material and were read through a summarising tool, so treat the names as reliable and the numbers as indicative. Gate questions are *general practice*.

### 1. Plan

**Purpose:** "Define Solution Blueprint" and "organise the project (determine the business goals, scope, and high-level requirements of the project)".

| Deliverables |
|--------------|
| PG091 Business Case |
| PL081 Stakeholders Goals and Expectations |
| PL101 Requirements |
| PL123 Current Capability Assessment |
| PL150 Solution Blueprint |
| PL170 Delivery Strategy |
| PL201 Requirements Traceability Matrix |
| PM110 Project Plan |
| PM246 Team Charter |
| PM262 Roles and Responsibilities |
| PM263 Project Orientation and Training Materials |
| PM266 Training Needs Matrix |
| PM289 Entry/Exit Criteria |

**Gate questions:** Is the business case approved? Are scope, delivery strategy and success measures agreed? Are entry and exit criteria defined for every later stage?

### 2. Analyze

**Purpose:** "Gather, identify, analyse, and manage the requirements", "evaluate packaged software and select technology infrastructure components", and "determine environmental and process needs to support the new capability".

| Deliverables |
|--------------|
| AP215 Fit/Gap Analysis |
| AP250 RICEF Inventories (reports, interfaces, conversions, enhancements, forms) |
| AP260 Integration Conceptual Design |
| BP310 Business Process Design |
| PL103 Solution Metrics |
| TE580 Test Plan (first version) |
| Updated PL101 Requirements, PL170 Delivery Strategy, PL201 Traceability Matrix |

**Gate questions:** Are requirements baselined and traceable? Is every gap between package and requirement dispositioned? Is the test approach agreed?

### 3. Design

**Purpose:** "Design the applications, technical architecture, technical infrastructure, and application training."

| Deliverables |
|--------------|
| AP326 Configuration Rationale |
| AP332 Configuration Design |
| AP350 RICEF Functional Design |
| AP360 Integration Functional Design |
| AP370 Data Conversion Design |
| AP481 Interface Agreement |
| Updated PL101, PL170, TE580 |

**Gate questions:** Does every requirement trace to a design element? Are interface agreements signed by both sides? Are non-functional requirements addressed in the architecture?

### 4. Build

**Purpose:** "Develop the applications, technical architecture, technical infrastructure, and application training."

| Deliverables |
|--------------|
| AP450 RICEF Technical Design |
| AP475 Integration Technical Design |
| TE483 Common Test Data |
| TE598 Test Closure Memo (for component-level testing) |
| Updated AP332, AP370, PL201, TE580 |

**Gate questions:** Is code peer reviewed and unit tested? Is the traceability matrix current? Are test data and environments ready for the Test stage?

### 5. Test

**Purpose:** "Test components built by all workstreams" and "validate the solution with the users".

| Deliverables |
|--------------|
| AP568 Mock Conversion Plan |
| TE598 Test Closure Memo |
| Updated PL201, TE483, TE580 |

**Gate questions:** Have integration, performance, security and user acceptance tests met their exit criteria? Are open defects within agreed thresholds? Has a mock conversion succeeded?

### 6. Deploy

**Purpose:** "Roll out the application, technical architecture, technical infrastructure, and training to the organisation."

| Deliverables |
|--------------|
| DP211 Deployment Plan |
| DP221 Deployment Work Plan |
| DP424 Go Live Preparation Action Plan |
| DP428 Go Live Support Plan |
| DP679 Client Readiness Sign Off |
| DP699 Handover Documents |

**Gate questions:** Has the client signed readiness? Is the support organisation trained and staffed? Is there a rollback plan?

> **Note:** Third-party guides describe a wider lifecycle, "often framed as Envision, Define, Design, Build, Test, Deploy, and Run/Optimize". That framing is not attributed to Accenture. The six-stage version is the one that appears in Accenture's own material.

## Workstreams

The four delivery workstreams are named in Accenture material, with Project Management running alongside them *(Documented)*. No public source defines their scope; the descriptions below are inferred from the stage purposes and role names *(General practice)*.

| Workstream | Covers |
|------------|--------|
| **Project Management** | Planning, estimating, scope and change control, risk and issue management, quality management, status reporting, stage entry and exit |
| **Application** | Requirements, business process design, functional and technical design, configuration, custom development, data conversion, application testing |
| **Technical Architecture** | Development, execution and operations architectures; infrastructure; environments; integration; performance and security |
| **Training & Performance Support** | Training needs analysis, curriculum and materials, user training, on-the-job support and change enablement |
| **Service Introduction** | Preparing the organisation that will run the solution: support model, service levels, operational procedures, handover |

## Roles

Roles named in connection with ADM *(Reported)*:

| Role | Workstream |
|------|-----------|
| Project Manager | Project Management |
| Quality Manager | Project Management |
| Business Architect | Application |
| Application Designer | Application |
| Data Architect | Application / Technical Architecture |
| Technical Architect | Technical Architecture |
| Technical Designer | Technical Architecture |
| Training and Performance Support Lead | Training & Performance Support |
| Service Introduction Lead | Service Introduction |

The workstream column is inferred from role names.

## The method library

ADM is a library, not one method. Each method shares the common framework and is specialised for a type of work.

| Method | Evidence | Notes |
|--------|----------|-------|
| ADM for SAP | Documented | Full lifecycle support; SAP-specific terminology, roles, templates, samples and checklists; top-down and bottom-up estimators; multi-site development guidance; transition to the support organisation |
| ADM for Custom Development (including a "with SOA" edition) | Reported | Appears as a named software listing |
| ADM for Program Management | Reported | Named in training material snippets |
| Application Management framework | Documented | Covers five areas of running an application management unit: Business Operations Management, Environment Management, Quality Management, Service Management, Service Provision |
| ADM for Agile Development | Reported | Defined in a public contract glossary as "a continually refined approach ... that utilizes common tools and techniques that are agile, inclusive, interactive, and iterative" |

ADM for SAP states its own boundaries. It applies when managing "a single project or one project within a series of planned projects or releases" where SAP is "the key element of the solution". It excludes selling the work, strategic planning and business architecture, program management, and specialised guidance for other technologies. Those are covered by other methods.

Separately named methods for Oracle, infrastructure or testing are widely assumed but not confirmed by any public source read for this page.

## Estimators

- ADM "includes estimators for estimating level of effort"; ADM for SAP ships "top-down and bottom-up estimators". *(Documented)*
- Accenture's SAFe paper explains the approach: estimators "generate gross numbers to predict how long a job may take by evaluating data from past experiences building out all types of WRICEFs". *(Documented)*
- A top-down estimate works from overall scope and complexity factors early in Plan. A bottom-up estimate sums object-level effort once inventories exist in Analyze and Design. *(General practice)*

## Tools, architectures and metrics

- **Tools (ADT).** A recommended set of vendor and Accenture-built tools mapped to lifecycle activities. No reliable public list of individual tool names exists. Tool names found on exam-prep sites are not trustworthy.
- **Architectures (ADA).** Reusable application frameworks and components that give projects a starting architecture.
- **Metrics.** A core metric set collected on every engagement. In Accenture's government practice, every project collected standard metrics and submitted them monthly. *(Documented)*

## Quality management

| Mechanism | Description | Evidence |
|-----------|-------------|----------|
| **Stage containment** | Find and fix defects in the stage that introduced them. "Continuous quality reviews ... enable stage containment to reduce rework and improve quality." | Documented |
| **Embedded checkpoints** | "Verification and validation checkpoints are embedded in our methodology and are performed as the final step of key tasks and activities." | Documented |
| **Entry and exit criteria** | Defined in Plan (deliverable PM289) and applied at each stage boundary | Documented |
| **Peer reviews** | "A structured review of work products by a project team member" using standard criteria, with measures analysed statistically | Documented |
| **Best practice reviews** | Monthly reviews of each project against the CMMI framework | Documented |
| **Senior reviews** | Independent reviews by senior Accenture leadership | Documented |
| **QPI** | The Quality and Process Improvement program supplies "standard processes, tools, coaching, and training" and "increased visibility into project execution" | Documented |
| **CQMA** | Client Quality Management Assessment, held at least every six months | Reported |
| **Traceability** | The Requirements Traceability Matrix (PL201) is updated in every stage from Plan through Test | Documented |

**Certifications.** Accenture reports CMMI-DEV appraisals from Level 3 to Level 5 across its delivery centres, with some centres also holding CMMI-SVC Level 5. Third parties report ISO 9001 certification since 1991, plus ISO 27001, ISO 20000 and People CMM Level 5.

The V-model is often associated with ADM in practitioner discussion, and stage containment is consistent with it, but no public source read for this page states it.

## Agile, DevOps and hybrid delivery

Accenture describes three application delivery approaches: agile, DevOps and waterfall *(Reported)*. Third-party guides characterise current ADM use as hybrid: stage-gated delivery for dependency-heavy or regulated work such as ERP, agile for digital products and analytics, and DevSecOps tooling across both, wrapped in common governance, quality and value tracking *(Reported)*.

### SAFe for Enterprise Solutions

Accenture's 2021 paper adapts the Scaled Agile Framework for packaged systems with nine changes *(Documented)*. The paper does not mention ADM by name.

1. Start with the Solution Train.
2. Think "minimum integrated business process" (MIBP) instead of a minimum viable product.
3. Use the business process master list (BPML) as guidance, not as structure.
4. Use Capability Strings.
5. Treat WRICEF objects as SAFe Features.
6. Use an estimator for the "job size" in weighted shortest job first (WSJF) prioritisation.
7. Think "continuish" deployment.
8. Continually evolve the live system through a sustainment and enhancement release train and a Solution Triage Team.
9. Adapt the SAFe Implementation Roadmap.

### Choosing a delivery style

*(General practice, consistent with third-party descriptions of ADM)*

| Choose | When |
|--------|------|
| Stage-gated | Requirements are stable, dependencies are dense, regulation demands signed-off stages, or the solution is a large package rollout |
| Agile | Requirements will be discovered, users can give frequent feedback, and releases can be small |
| Hybrid | A program mixes both, for example an ERP core with digital front ends. Run agile build inside gated Plan and Deploy stages. |

## Automation: myWizard

myWizard is Accenture's intelligent automation platform for application services *(Documented)*.

- Launched 12 April 2016, hosted on Microsoft Azure, with virtual agents including an Intelligent Data Scientist, a Virtual Testing Savant and a Virtual Scrum Master.
- A new generation was announced on 9 September 2020. Accenture then reported use on 9,000 engagements at 1,500 companies by more than 100,000 professionals.
- Accenture received the 2020 Watts Humphrey Software Process Achievement Award for its automation journey, described by a "4S" model: Simple, Seamless, Scalable, Sustainable.

## Applying ADM-style delivery

A working sequence that follows the documented ADM structure *(General practice)*:

1. **Frame the engagement.** Write the business case, stakeholder goals and success metrics.
2. **Choose the delivery style** per workstream and record the reasoning in the delivery strategy.
3. **Set up governance.** Assign the roles above, define decision rights, and write entry and exit criteria for each stage.
4. **Estimate twice.** Top-down in Plan, bottom-up once inventories exist.
5. **Baseline requirements** and start the traceability matrix. Keep it current through Test.
6. **Design before build**, covering application, architecture, training and service introduction together.
7. **Build with reviews.** Peer review every work product and contain defects in-stage.
8. **Test against the plan** written in Analyze, and close each test phase with a closure memo.
9. **Prepare the receiving organisation** through the Service Introduction workstream well before go-live.
10. **Deploy with sign-off.** Obtain client readiness sign-off and complete handover documents.

### Common pitfalls

| Pitfall | Countermeasure |
|---------|----------------|
| Producing artefacts to pass gates without solving the business problem | Tie gate decisions to outcomes in the business case |
| Applying the full method to a small project | Tailor deliverables to risk and size |
| Forcing agile onto compliance-heavy work, or waterfall onto exploratory work | Pick the style per workstream |
| Leaving training and service introduction until Deploy | Run those workstreams from Plan |
| Non-functional requirements surfacing in Test | Treat them as first-class requirements from Analyze |
| Traceability matrix abandoned after Design | Make its update an exit criterion for every stage |

## How ADM relates to other frameworks

| Framework | Relationship |
|-----------|--------------|
| PMBOK, PRINCE2 | Comparable stage and governance disciplines; ADM adds delivery content (deliverables, estimators, templates) |
| CMMI | ADM processes were tailored to satisfy CMMI process areas; appraisals verify adherence |
| Scrum, SAFe | Used inside the agile path; Accenture adapts SAFe for enterprise packages |
| ITIL | Relevant to Service Introduction and to application management after Deploy |
| SAP Activate, Oracle Unified Method | Vendor methods for the same package work; Accenture's SAFe paper positions its model against both |

## Glossary

| Term | Meaning |
|------|---------|
| ADS | Accenture Delivery Suite: methods, tools, architectures, metrics |
| ADM | Accenture Delivery Methods |
| ADT | Accenture Delivery Tools |
| ADA | Accenture Delivery Architectures |
| BIM | Business Integration Methodology, a predecessor |
| BPML | Business process master list |
| CQMA | Client Quality Management Assessment |
| MIBP | Minimum integrated business process |
| QPI | Quality and Process Improvement |
| RICEF / WRICEF | (Workflows,) reports, interfaces, conversions, enhancements, forms: the custom object types in a package implementation |
| RTM | Requirements Traceability Matrix |
| Stage containment | Detecting and fixing defects in the stage where they were introduced |
| Workstream | A domain of work that runs across all stages |

## Sources

Accenture and primary sources:

- [US-VISIT prime contract, Volume 4 Part D](https://www.dhs.gov/sites/default/files/2026-04/US-VISIT_PrimeContract_Vol4-D.pdf) — Accenture's 2003 proposal to DHS (redacted)
- [Agility in the Age of Enterprise Solutions](https://www.accenture.com/content/dam/accenture/final/a-com-migration/manual/pdf/Accenture-Agility-In-The-Age-Of-Enterprise-POV.pdf) — Accenture, 2021
- [myWizard launch](https://newsroom.accenture.com/news/2016/accenture-launches-intelligent-automation-platform-to-deliver-smarter-more-efficient-application-services-that-improve-business-outcomes) and [2020 release](https://newsroom.accenture.com/news/2020/accenture-introduces-powerful-new-version-of-mywizard-intelligent-automation-platform) — Accenture newsroom
- [Accenture CMMI rollout deck](https://ndia.dtic.mil/wp-content/uploads/2005/cmmi/tuesday/bengzon.pdf) — NDIA CMMI conference, 2005
- [Accenture: An Automation Maturity Journey](https://www.sei.cmu.edu/library/accenture-an-automation-maturity-journey/) — Software Engineering Institute
- [Accenture delivery centres data](https://www.accenture.com/content/dam/accenture/final/a-com-migration/custom/us-en/delivery-centers/data.html)

Public copies of Accenture training material:

- [SAP FI bootcamp, day 5](https://www.slideshare.net/slideshow/sapfibootcamptrainingday5ppt/251746663) — ADS and ADM for SAP slides, source of stage purposes and deliverables

Third-party sources:

- [Umbrex: Accenture Delivery Methods](https://umbrex.com/resources/frameworks/project-management-frameworks/accenture-delivery-methods/)
- [IIHMR dissertation, 2012](https://drs.iihmrdelhi.edu.in/server/api/core/bitstreams/e1002c76-04fd-40c6-802a-9b82787764a3/content) — roles and ADS components
- [Law Insider: Accenture Delivery Methodology for Agile Development](https://www.lawinsider.com/dictionary/accenture-delivery-methodology-for-agile-development)
- [Locus Assignments quality management essay](https://www.locusassignments.com/courses/unit-32-quality-management-assignment) — QPI and certification claims
- [Accenture Delivery Methods Estimator listing](https://accenture-delivery-methods-estimator.updatestar.com/)
