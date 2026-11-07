title: Vulnerability Assessment Automation Lab description: Cybersecurity engineering home lab demonstrating automated vulnerability intelligence and risk prioritization.
Vulnerability Assessment Automation Lab
Cybersecurity Engineering | Threat Intelligence | Vulnerability Management

A practical Ubuntu-based cybersecurity engineering project demonstrating how vulnerability intelligence can be collected, normalized, correlated against assets, prioritized, and transformed into automated security reports.

View GitHub Repository
Project Mission

The objective is to build a scalable vulnerability assessment automation platform that reduces manual effort in vulnerability intelligence collection and risk prioritization.

The proof of concept mirrors key capabilities of an enterprise vulnerability management workflow.
Core Capabilities
01 — Threat Intelligence Ingestion

Collect vulnerability intelligence from the CISA Known Exploited Vulnerabilities catalog.

    Retrieve public vulnerability intelligence.
    Normalize CVE records.
    Extract vendor and product information.
    Identify known exploited vulnerabilities.

02 — Asset Correlation

Associate selected vulnerabilities with an internal asset inventory.

    Simulated enterprise asset inventory.
    Hostname and software identification.
    Business criticality assessment.
    Environment and exposure classification.

03 — Contextual Risk Scoring

Prioritize vulnerability findings using contextual risk attributes.

    CVSS severity.
    EPSS exploitation probability.
    CISA KEV status.
    Asset business criticality.
    Network exposure.

04 — Automated Reporting

Generate structured vulnerability outputs.

    Normalized vulnerability CSV.
    Correlated asset-vulnerability CSV.
    Prioritized risk CSV.
    Executive HTML report.

Lab Architecture
text

         CISA KEV INTELLIGENCE
                  |
                  v
          PYTHON INGESTION
                  |
                  v
          DATA NORMALIZATION
                  |
                  v
          ASSET CORRELATION
                  |
                  v
          CONTEXTUAL RISK
              ENGINE
                  |
                  v
          RISK PRIORITIZATION
                  |
                  v
          AUTOMATED REPORTING
                  |
                  v
             CSV / HTML

Technology Stack
Technology	Function
Ubuntu	Host operating system
Python	Automation engine
Pandas	Data processing
Requests	Threat feed ingestion
Docker	Containerization
Docker Compose	Service orchestration
PostgreSQL	Planned data persistence
Redis	Planned caching
GitHub	Source control and documentation
Project Development Status
Component	Status
Ubuntu environment	Implemented
Docker infrastructure	Configured
CISA KEV ingestion	Implemented
Asset correlation	Demonstration implemented
Risk scoring	Demonstration implemented
HTML reporting	Implemented
PostgreSQL integration	Planned
Redis integration	Planned
FastAPI integration	Planned
Dashboard development	Planned
Project Deliverables

The pipeline is designed to generate:

    normalized_kev.csv
    correlated_vulnerabilities.csv
    prioritized_risks.csv
    executive_report.html

Development Roadmap

Phase 1 — Foundation

Ubuntu, Docker, Python environment and project structure.

Phase 2 — Threat Intelligence

CISA KEV ingestion and vulnerability normalization.

Phase 3 — Asset Intelligence

Asset inventory and vulnerability correlation.

Phase 4 — Risk Prioritization

Contextual risk calculation and vulnerability ranking.

Phase 5 — Reporting

Automated CSV and HTML executive reporting.

Phase 6 — Enterprise Expansion

PostgreSQL, Redis, NVD, EPSS, FastAPI and dashboard integration.
Repository

Explore the source code, configuration, and implementation:

GitHub — Vulnerability Assessment Automation Lab
Disclaimer

This project is an educational proof of concept intended for authorized defensive cybersecurity assessment. It uses a simulated asset inventory and demonstration risk-scoring values. It is not a production vulnerability management platform.

Project: Vulnerability Assessment Automation Lab

Platform: Ubuntu Linux

Focus: Cybersecurity Engineering and Vulnerability Management
