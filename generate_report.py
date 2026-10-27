import json
import os

def generate_system_report():
    print("=" * 50)
    print("[*] Adastra Autonomous OS - Executive System Report")
    print("=" * 50)
    
    pipeline_file = "new_clients_pipeline.json"
    
    if os.path.exists(pipeline_file):
        with open(pipeline_file, "r") as f:
            try:
                leads = json.load(f)
            except json.JSONDecodeError:
                leads = []
        
        print(f"[+] Total Active Leads in Pipeline: {len(leads)}")
        print("-" * 50)
        for i, lead in enumerate(leads, 1):
            print(f"  {i}. Lead ID: {lead.get('lead_id', 'N/A')}")
            print(f"     Status: {lead.get('status', 'N/A')}")
            print(f"     Potential Value: {lead.get('potential_value', 'N/A')}")
            print(f"     Timestamp: {lead.get('timestamp', 'N/A')}")
            print("-" * 30)
    else:
        print("[!] No active lead pipeline found yet.")
        
    print("[*] System Status: Autonomous & Fully Operational.")
    print("=" * 50)

if __name__ == "__main__":
    generate_system_report()
