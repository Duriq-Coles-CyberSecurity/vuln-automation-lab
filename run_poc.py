import subprocess

if __name__ == "__main__":
    print("=== STARTING VULNERABILITY AUTOMATION POC ===")
    
    # Step 1: Ingest Feeds
    subprocess.run(["python3", "app/ingest.py"])
    
    # Step 2: Correlate Assets
    subprocess.run(["python3", "app/correlate.py"])
    
    # Step 3: Run Risk Scoring
    subprocess.run(["python3", "app/risk_engine.py"])
    
    # Step 4: Generate Report
    subprocess.run(["python3", "app/reporter.py"])
    
    print("=== POC EXECUTION COMPLETE. CHECK THE output/ DIRECTORY ===")
