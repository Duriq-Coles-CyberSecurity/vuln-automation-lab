Vulnerability Assessment Automation Lab

Cybersecurity Engineering | Vulnerability Management | Threat Intelligence

A Python-based proof of concept demonstrating automated vulnerability intelligence ingestion, asset correlation, contextual risk scoring, and security reporting.

1. Project Overview

This project explores how vulnerability management workflows can be automated using publicly available threat intelligence and a simulated enterprise asset inventory.

The objective is to demonstrate how security teams can collect vulnerability intelligence, identify relevant asset exposure, prioritize risks, and generate actionable security reports.

Core Components
Threat Intelligence Ingestion
Retrieve vulnerability intelligence from the CISA Known Exploited Vulnerabilities (KEV) catalog.
Normalize vulnerability records.
Extract CVE identifiers, vendors, products, and remediation guidance.
Asset Correlation
Maintain a simulated enterprise asset inventory.
Associate selected vulnerabilities with affected assets.
Consider asset ownership, environment, exposure, and business criticality.
Risk Scoring
Incorporate CVSS severity.
Consider EPSS exploitation probability.
Apply CISA KEV prioritization.
Account for business criticality and network exposure.
Automated Reporting
Generate normalized vulnerability CSV files.
Produce correlated asset-vulnerability records.
Generate prioritized risk outputs.
Create an executive HTML report.
2. Lab Architecture
text
             CISA KEV FEED
                   |
                   v
          THREAT INTELLIGENCE
               INGESTION
                   |
                   v
           DATA NORMALIZATION
                   |
                   v
            ASSET CORRELATION
                   |
                   v
          CONTEXTUAL RISK ENGINE
                   |
                   v
          RISK PRIORITIZATION
                   |
                   v
          AUTOMATED REPORTING
                   |
                   v
               CSV / HTML

3. Technology Stack
Technology	Purpose
Ubuntu Linux	Lab operating system
Python 3	Automation and processing
Pandas	Data normalization and analysis
Requests	Threat intelligence collection
Docker	Containerization
Docker Compose	Infrastructure orchestration
PostgreSQL	Planned persistent storage
Redis	Planned caching and job staging
Git	Version control
GitHub	Source code hosting and documentation
4. Repository Structure
text
vuln-automation-lab/
├── app/
│   ├── ingest.py
│   ├── correlate.py
│   ├── risk_engine.py
│   ├── reporter.py
│   ├── assets.csv
│   └── requirements.txt
├── feeds/
├── db/
├── output/
├── docs/
├── docker-compose.yaml
├── requirements.txt
├── run_poc.py
├── README.md
└── .gitignore

5. Installation and Configuration
Prerequisites
Ubuntu Linux 22.04 or later.
Python 3.11 or later.
Docker Engine.
Docker Compose.
Clone the Repository
bash
git clone https://github.com/Duriq-Coles-CyberSecurity/vuln-automation-lab.git
cd vuln-automation-lab

Create a Python Virtual Environment
bash
python3 -m venv venv
source venv/bin/activate

Install Dependencies
bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Start Docker Infrastructure
bash
docker compose up -d
docker compose ps

6. Execute the Vulnerability Automation Pipeline

Run the complete proof of concept from the project root directory:

bash
python3 run_poc.py


The pipeline executes four stages:

Stage	Script	Function
1	ingest.py	CISA KEV ingestion
2	correlate.py	Asset correlation
3	risk_engine.py	Risk prioritization
4	reporter.py	HTML report generation
7. Risk Scoring Methodology

The demonstration risk engine uses the following formula:

Final Risk Score = CVSS × EPSS × KEV Multiplier × Asset Criticality × Exposure Multiplier

The current demonstration uses:

Risk Attribute	Example Value
CVSS	10.0
EPSS	0.95
CISA KEV multiplier	2.0
Asset criticality	2
Internal exposure multiplier	1.0

These are demonstration values, not live enrichment results.

The formula illustrates how vulnerability severity can be combined with exploitation likelihood and business context.

8. Expected Output Files

Following successful execution, the pipeline should generate:

text
feeds/
└── normalized_kev.csv

output/
├── correlated_vulnerabilities.csv
├── prioritized_risks.csv
└── executive_report.html

Output Descriptions
normalized_kev.csv: Standardized CISA KEV vulnerability records.
correlated_vulnerabilities.csv: Demonstration asset-vulnerability matches.
prioritized_risks.csv: Risk-ranked vulnerability findings.
executive_report.html: Automatically generated executive summary.
9. Implementation Status
Component	Status
Ubuntu lab environment	Implemented
Docker infrastructure configuration	Configured
CISA KEV ingestion	Implemented
Vulnerability normalization	Implemented
Demonstration asset correlation	Implemented
Demonstration risk scoring	Implemented
HTML report generation	Implemented
PostgreSQL application integration	Planned
Redis application integration	Planned
Live CVSS enrichment	Planned
Live EPSS enrichment	Planned
Advanced software version matching	Planned
FastAPI integration	Planned
10. Future Development Roadmap
Phase 1: Threat Intelligence Expansion
Integrate the NVD vulnerability database.
Retrieve live EPSS scores.
Expand vulnerability metadata.
Phase 2: Advanced Asset Correlation
Implement CPE-based software identification.
Improve software version matching.
Expand asset inventory attributes.
Phase 3: Database Integration
Implement PostgreSQL persistence.
Introduce historical vulnerability tracking.
Integrate Redis caching.
Phase 4: API and Automation
Develop FastAPI endpoints.
Introduce scheduled ingestion.
Explore workflow orchestration.
Phase 5: Security Dashboard
Develop vulnerability analytics.
Visualize risk trends.
Improve executive reporting.
11. Security Disclaimer

This project is an educational cybersecurity engineering proof of concept intended for authorized defensive security assessment.

The asset inventory and correlation results are simulated. The current risk engine uses demonstration CVSS and EPSS values and does not represent a production vulnerability assessment platform.

Do not use demonstration results as a substitute for validated vulnerability intelligence or production risk assessments.

12. Project Information

Project: Vulnerability Assessment Automation Lab

Platform: Ubuntu Linux

Language: Python

Focus Areas:

Cybersecurity Engineering
Vulnerability Management
Threat Intelligence
Security Automation
Risk Prioritization

Repository:

https://github.com/Duriq-Coles-CyberSecurity/vuln-automation-lab
