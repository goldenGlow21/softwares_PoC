# Proof of Concept for: **Totolink A3002R V4_Firmware V4.0.0-B20230531.1404**

> https://www.cve.org/CVERecord?id=CVE-2025-55585

---

**Contributor :** Lee Jong Hoon, Yang In Gyu, Jeong Yun Ho, Park Seong Ho, Lim Chan Su

**Vuln. Identificated** : 2025.02.26
**CVE Designated** : 2025.8.18

**Testing Environment** : Ubuntu 22.04 LTS / Kali Linux 2024.4 amd64 / FirmAE

## Vulnerability Info

### Firmware Version
TOTOLINK A3002R V4
TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404.web

### Vulnerability Type
Eval Injection

### 1-Line Description
Checked the use of the eval() function on several pages and exploited the vulnerability to get sessionid

---

## Vulnerability Acquirement

### Shell Analysis
<img width="715" alt="image" src="https://github.com/user-attachments/assets/a266d47c-a948-46b9-9239-f058d7369ad9" />

Identify the use of the eval() function during static analysis by connecting to the shell

<img width="671" alt="image" src="https://github.com/user-attachments/assets/c3595f4f-14b5-494c-aebb-722d9028273e" />

top.location.href → This means that you get all the top URLs of your current browser
<br>
.split(”#”) → "#" divide it on the basis of
<br>
[1] → It's literally an array index

<img width="813" alt="image" src="https://github.com/user-attachments/assets/d7dede8a-4003-4f12-a2d6-d268c3220725" />

Check other htm pages to see if they also use the eval() function

### 
<img width="792" alt="image" src="https://github.com/user-attachments/assets/8b90d832-4e34-4976-9992-2f9bbe331839" />

I first tried using alert("XSS") to see if the eval() function works properly

---

## Vulnerability Verification

### crack
<img width="760" alt="image" src="https://github.com/user-attachments/assets/1789a1fb-073b-4ac5-98ed-6cf8029934f8" />

When confirmed with the developer tool, it was confirmed that the value was treated as hidden in the sessionCheck field

<img width="764" alt="image" src="https://github.com/user-attachments/assets/49979621-7b94-42be-aec0-b0a3fc69369a" />

Attempting to get a value from the sessioncheck field

---

## Result

<img width="490" alt="image" src="https://github.com/user-attachments/assets/754d8242-979b-4fe5-b24c-8799738ae655" />

Successful exploitation of sessionid when accessing page, XSS vulnerability succeeded through eval() function
<br>
In addition, eval() was possible on a total of 7 pages.
<br>
: title.htm, wlstatbl.htm, moblie/wizard.asp, portfw.htm, arptbl.htm, reboot.htm, saveconf.htm

