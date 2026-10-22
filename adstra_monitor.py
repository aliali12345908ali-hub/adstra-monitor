import time
import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

TARGET_URL = "https://google.com"
CHECK_INTERVAL = 30

def check_website():
    try:
        response = requests.get(TARGET_URL, timeout=10)
        if response.status_code == 200:
            logging.info(f"الخدمة تعمل بنجاح | Status: {response.status_code}")
        else:
            logging.warning(f"تنبيه: استجابة غير متوقعة | Status: {response.status_code}")
    except requests.RequestException as error:
        logging.error(f"خطأ في الاتصال بالخدمة: {error}")

def main():
    logging.info("تم بدء تشغيل سكريبت المراقبة...")
    while True:
        check_website()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
import requests
import os
import time

# أضف مفتاح الـ API الخاص بـ Adsterra من لوحة التحكم (Profile > API)
ADSTERRA_API_KEY = os.environ.get("ADSTERRA_API_KEY", "YOUR_API_KEY_HERE")

def check_balance():
    url = "https://publishers.adsterra.com/api/v1/publisher/balance"
    headers = {"Authorization": f"Bearer {ADSTERRA_API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            balance = data.get("balance", "0.00")
            print(f"[+] الرصيد الحالي في Adsterra: ${balance}")
        else:
            print("[-] تعذر جلب الرصيد، تحقق من مفتاح API")
    except Exception as e:
        print(f"[-] خطأ أثناء الاتصال: {e}")

if __name__ == "__main__":
    while True:
        check_balance()
        time.sleep(3600)  # فحص وتنبيه كل ساعة


