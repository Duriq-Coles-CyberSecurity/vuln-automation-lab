# vuln-automation-lab
Python-based vulnerability intelligence ingestion, asset correlation, risk scoring, and automated reporting PoC.
# Vulnerability Assessment Automation Lab

**Cybersecurity Engineering | Ubuntu | Python | Docker | Threat Intelligence**

A practical proof of concept demonstrating automated vulnerability intelligence ingestion, asset correlation, contextual risk scoring, and security reporting.

## Project Overview

This project explores how vulnerability management workflows can be automated using publicly available threat intelligence and a simulated enterprise asset inventory.

The PoC consists of four core components:

1. **Threat Intelligence Ingestion:** Collect vulnerability data from the CISA Known Exploited Vulnerabilities (KEV) catalog.
2. **Asset Correlation:** Associate selected vulnerabilities with a simulated internal asset inventory.
3. **Risk Scoring:** Prioritize findings using CVSS, EPSS, CISA KEV status, asset criticality, and exposure.
4. **Automated Reporting:** Generate CSV outputs and an HTML executive report.

## Architecture

```text
CISA KEV
   |
   v
Threat Intelligence Ingestion
   |
   v
Data Normalization
   |
   v
Asset Correlation
   |
   v
Contextual Risk Scoring
   |
   v
Prioritized Vulnerabilities
   |
   v
HTML / CSV Reporting
