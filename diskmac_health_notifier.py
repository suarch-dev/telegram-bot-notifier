import requests, os, subprocess, logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logging.info("Checking disk status for: Macbook")

try:
    # Get disk usage percenta
    percentage = int(subprocess.run(["df", "-h", "/"], capture_output=True, text=True).stdout.split("\n")[1].split()[4].replace("%", ""))
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    # print(porcentaje)
    if percentage < 80:
        notifier = requests.post(url, json={"chat_id": chat_id, "text": f"Alert! Disk usage at {percentage}%"})
        logging.info(f"status_code: {notifier.status_code}")
        if notifier.status_code >= 400:
            logging.info(notifier.json())
        logging.warning(f"High disk usage detected! {percentage}%")
    else:
        #requests.post(url, json={"chat_id": chat_id, "text": f"Salud del disco buena: {porcentaje}%"})
        logging.info(f"Disk health is good {percentage}%.")
except Exception as e:
    logging.error(e)