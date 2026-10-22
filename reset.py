import os
import requests

email_address = os.environ.get("USER_EMAIL")
url = "https://adsterra.com"

if not email_address:
    print("خطأ: لم يتم تعيين متغير البيئة USER_EMAIL بعد!")
else:
    # إضافة متصفح وهمي لتخطي جدار الحماية
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Content-Type": "application/json"
    }
    
    try:
        # تغيير الطلب إلى GET بدلاً من POST وتمرير البريد
        response = requests.get(url, params={"email": email_address}, headers=headers)
        print("Status Code:", response.status_code)
        print("Response:", response.text[:500]) # طباعة أول 500 حرف فقط للاختصار
    except requests.exceptions.RequestException as e:
        print("حدث خطأ في الاتصال بالشبكة:", e)
