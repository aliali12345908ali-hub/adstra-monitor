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
