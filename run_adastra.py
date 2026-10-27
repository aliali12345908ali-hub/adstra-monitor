import time
import datetime

email = "Aliali12345908ali@gmail.com"

print("=" * 40)
print("🚀 Adastra Sovereign Digital Enterprise 🚀")
print("=" * 40)
print(f"الحساب المرتبط: {email}")
print("النظام يعمل الآن في الخلفية لتسجيل البيانات والتقارير...")
print("=" * 40)

try:
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{now}] تم حفظ تقرير النظام بنجاح لـ: {email}\n"
        
        with open("adastra_logs.txt", "a") as f:
            f.write(log_entry)
            
        print(f"تم تحديث السجل وحفظه محلياً: {now}")
        time.sleep(10)
except KeyboardInterrupt:
    print("\nتم إيقاف النظام بأمان يا زعيم.")

# --- Adastra SEO Routes Integration ---
# Ensure robots.txt and sitemap.xml are served to search engines
import os

def serve_seo_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read(), 200, {'Content-Type': 'text/plain' if 'robots' in filename else 'application/xml'}
    return "Not Found", 404
