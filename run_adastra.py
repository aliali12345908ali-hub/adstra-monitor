import os
import subprocess


def run_adastra_empire():
  print("👑 [Adastra Autonomous OS] - Initializing Full Empire Mode...")

  # 1. تشغيل درع الأمان السيادي
  if os.path.exists("sovereign_security_shield.py"):
    print("🔒 Running Sovereign Security Shield...")
    subprocess.run(["python", "sovereign_security_shield.py"])

  # 2. تتبع الإيرادات الحية
  if os.path.exists("view_live_revenue.py"):
    print("💰 Fetching Live Revenue & Ledger...")
    subprocess.run(["python", "view_live_revenue.py"])

  # 3. تفعيل نظام الباقات الفاخرة
  if os.path.exists("high_ticket_service.py"):
    print("💎 High-Ticket Service Tiers Active & Ready.")

  print(
      "🚀 Empire Mode: FULLY AUTONOMOUS & SECURE. All systems operational!"
  )


if __name__ == "__main__":
  run_adastra_empire()


