import pandas as pd

def calculate_risk():
    print("[*] Calculating contextual risk scores...")
    df = pd.read_csv("output/correlated_vulnerabilities.csv")
    
    # Mock attributes for calculation
    df["cvss_base"] = 10.0  # e.g., Log4Shell
    df["epss_score"] = 0.95 # High exploitation probability
    
    # Multipliers
    exposure_multiplier = {"Internet-Facing": 2.0, "Internal": 1.0}
    
    scores = []
    for idx, row in df.iterrows():
        exposure_mult = exposure_multiplier.get(row["exposure"], 1.0)
        kev_multiplier = 2.0 if row["cisa_kev"] else 1.0
        
        # Risk Formula
        base_risk = (row["cvss_base"] * row["epss_score"] * kev_multiplier)
        final_score = base_risk * row["business_criticality"] * exposure_mult
        scores.append(round(final_score, 2))
        
    df["final_risk_score"] = scores
    df.sort_values(by="final_risk_score", ascending=False, inplace=True)
    df.to_csv("output/prioritized_risks.csv", index=False)
    print("[+] Risk calculation complete. Results saved to output/prioritized_risks.csv")

if __name__ == "__main__":
    calculate_risk()
