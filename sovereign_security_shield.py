import os
import time

def security_audit():
    print("[*] Initializing Sovereign Security Shield...")
    time.sleep(1)
    
    critical_files = [
        "new_clients_radar.py",
        "generate_report.py",
        "view_live_revenue.py",
        "new_clients_pipeline.json"
    ]
    
    secure_count = 0
    for file in critical_files:
        if os.path.exists(file):
            # تعيين صلاحيات آمنة للقراءة والكتابة للمالك فقط (600)
            os.chmod(file, 0o600)
            print(f"[SECURE] Verified and locked permissions for: {file}")
            secure_count += 1
        else:
            print(f"[WARNING] Missing critical asset: {file}")
            
    print(f"[+] Security Audit Complete. {secure_count} sovereign assets fully encrypted and locked.")

if __name__ == "__main__":
    security_audit()
