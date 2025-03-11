# Proof of Concept for: **Totolink A3002R V4_Firmware V4.0.0-B20230531.1404**

---

**Contributor :** Lee Jong Hoon, Yang In Gyu, Jeong Yun Ho, Park Seong Ho, Lim Chan Su

**Date** : 2025.3.8

**Testing Environment** : Ubuntu 22.04 LTS / Kali Linux 2024.4 amd64 / FirmAE

## Vulnerability Info

### Firmware Version

- `TOTOLINK A3002R V4`
- `TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404.web`

### Vulnerability Type

- Command Injection

### 1-Line Description

- `TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404.web` includes Command Injection vulnerability at `bupload.htm` endpoint, that’s used for uploading binary files for firmware update. Attacker can execute arbitrary commands by editing request’s field value.

---

## Vulnerability Acquirement



While inspecting the script, we confirmed that the string stored through v15 is getting executed by system() function. Especially, the script gets input value from user by “echo %s”, and make it as a4. 



If a4 field is empty, the script allocates “off_48A060”’s value to a4. This eventually blocks command injection, so we got to set the value ourself on Burp Suite.



By using self-made search.py, we found web interface that includes formUploadFile. Afterward, we will be conducting exploit by using this interface route to connect.

---

## Vulnerability Verification



On this page, we can select files to upload. Since selecting other abitrary files are blocked by internal logic(e.g. .txt, .php, …), we selected Totolink’s official firmware image file.

After clicking the upload button after selecting the file, use Burp Suite to edit the request packet.



As the picture above, edit the “filename” parameter and inject the command desired. On our case, we injected `test.bin; touch /tmp/malware;` after separating by “;”, which inteded to create malformed file on /tmp route.

---

## Result



After injecting the command, we connected to the shell of emulator and confirmed creation of ‘malware’ file, which indicates success of OS command Injection.
