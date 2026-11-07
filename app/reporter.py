import pandas as pd

def generate_report():
    print("[*] Generating automated executive report...")
    df = pd.read_csv("output/prioritized_risks.csv")
    
    html_content = """
    <html>
    <head>
        <title>Vulnerability Automation PoC - Executive Report</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            table { border-collapse: collapse; width: 100%; margin-top: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>Cyber Threat Intelligence & Vulnerability Management - PoC Report</h1>
        <p>Automated risk-scored vulnerability findings across enterprise assets.</p>
    """
    
    html_content += df.to_html(index=False)
    html_content += """
    </body>
    </html>
    """
    
    with open("output/executive_report.html", "w") as f:
        f.write(html_content)
    print("[*] Executive report successfully generated at output/executive_report.html")

if __name__ == "__main__":
    generate_report()
