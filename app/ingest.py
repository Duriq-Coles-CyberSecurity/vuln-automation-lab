import json
import requests
import pandas as pd

CISA_KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

def fetch_cisa_kev():
    print("[*] Fetching CISA KEV feed...")
    response = requests.get(CISA_KEV_URL)
    if response.status_code == 200:
        data = response.json()
        vulnerabilities = data.get("vulnerabilities", [])
        print(f"[+] Successfully fetched {len(vulnerabilities)} vulnerabilities from CISA KEV.")
        return vulnerabilities
    else:
        print(f"[-] Failed to fetch feed: {response.status_code}")
        return []

def normalize_feed(vulns):
    normalized = []
    for v in vulns:
        normalized.append({
            "cve_id": v.get("cveID"),
            "vendor": v.get("vendorProject"),
            "product": v.get("product"),
            "vulnerability_name": v.get("vulnerabilityName"),
            "date_added": v.get("dateAdded"),
            "short_description": v.get("shortDescription"),
            "required_action": v.get("requiredAction"),
            "cisa_kev": True
        })
    return pd.DataFrame(normalized)

if __name__ == "__main__":
    raw_data = fetch_cisa_kev()
    df = normalize_feed(raw_data)
    df.to_csv("feeds/normalized_kev.csv", index=False)
    print("[+] Normalized KEV data saved to feeds/normalized_kev.csv")
