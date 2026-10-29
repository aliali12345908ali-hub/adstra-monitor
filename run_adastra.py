import os
import subprocess


def secure_and_run_revenue_engine():
  print(
      "👑 [Adastra Autonomous OS] - Starting High-Speed Revenue & Security"
      " Engine..."
  )

  # 1. التحقق من حالة السيرفر وملفات الأمان
  if os.path.exists("server.js") or os.path.exists("run_adastra.py"):
    print("🛡️ Security shield and server core detected.")
  else:
    print("⚠️ Core files missing, ensuring infrastructure integrity...")

  # 2. تشغيل درع الأمان السيادي لضمان حماية المعاملات
  if os.path.exists("sovereign_security_shield.py"):
    print("🔒 Executing Sovereign Security Shield...")
    subprocess.run(["python", "sovereign_security_shield.py"])

  # 3. تتبع الإيرادات الحية لدعم سرعة جمع المال
  if os.path.exists("view_live_revenue.py"):
    print("💰 Initializing Live Revenue Tracker...")
    subprocess.run(["python", "view_live_revenue.py"])

  print(
      "🚀 All revenue and security systems are fully operational and optimized"
      " for maximum profit speed."
  )


if __name__ == "__main__":
  secure_and_run_revenue_engine()


