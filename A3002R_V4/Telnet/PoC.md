# Proof of Concept for: **Totolink A3002R V4_Firmware V4.0.0-B20230531.1404**

---

**Contributor :** Lee Jong Hoon, Yang In Gyu, Jeong Yun Ho, Park Seong Ho, Lim Chan Su

**Date** : 2025.2.23

**Testing Environment** : Ubuntu 22.04 LTS / Kali Linux 2024.4 amd64 / FirmAE

## Vulnerability Info

### Firmware Version
TOTOLINK A3002R V4
TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404.web

### Vulnerability Type
Telnet & Hardcoding Vulnerability
### 1-Line Description
Using a hard-coded shadow.sample file, connect to Telnet running on the system

---

## Vulnerability Acquirement

### Shell Analysis
<img width="695" alt="image" src="https://github.com/user-attachments/assets/8049780a-dfe4-49ec-a674-185093a55760" />

While operating the emulator for the firmware and analyzing server vulnerabilities, I found that the shadow, shadow.sample file was using the MD5 hash algorithm

<img width="729" alt="스크린샷 2025-03-11 오후 12 34 22" src="https://github.com/user-attachments/assets/7ed18022-22db-43e2-9dfd-f223542f398a" />

Telnetd found in /bin directory, but further investigation required

![ㅣ1](https://github.com/user-attachments/assets/cc0c4272-ddae-4f28-ac27-1696889c817f)

Kernel starts init and init runs busybox

![ㅣ2](https://github.com/user-attachments/assets/b8002dca-f814-4139-8b19-9a972c2e22fd)

refer to /etc/inittab in busybox

### Ghidra
![ㅣ3](https://github.com/user-attachments/assets/b303741b-0be4-40fa-885f-32bba2148dfb)

/etc/inittab called etc/init.d/rcS in the function FUN_004436f0

![1541](https://github.com/user-attachments/assets/ad8939b2-3d49-4cc3-bc14-667be1c596d8)

/etc/init.d/rcS calls init.sh (gw all)
<br>
gw all: gateway all

![123123](https://github.com/user-attachments/assets/1d0b2ad1-45cb-43e0-bb57-0ebbecff49a6)

Perform sysconf on init.sh and i have further investigated into FUN_00404d98

![1231234](https://github.com/user-attachments/assets/a270e58b-1d68-406f-8e71-cfd238bc6694)

I identified telnetd, the damon of telnet, in the function FUN_00404d98.
So I thought I should try Telnet access through the information on the shadow or shadow.sample.

---

## Vulnerability Verification

### Try to Exploit
![telnet](https://github.com/user-attachments/assets/dca6f395-d7a0-4228-a586-d02b0f66ad6d)

Check the show.sample file

![ㅋ1](https://github.com/user-attachments/assets/aadbf590-93b4-41ce-a654-d345b82b4876)

Put all the copied values in the hash.txt file and attempt to crack using the John the Ripper tool

![tel](https://github.com/user-attachments/assets/1babdd14-d435-42e4-b639-63df27eb83cb)

As previously analyzed, we identified that Telnet is operating and therefore performed a port scan using the Nmap tool, and confirmed that it is also using Telnet Port 23

---

## Result

![ㅋ2](https://github.com/user-attachments/assets/cfc807a4-b302-46de-a7e1-82aaa49a950a)

Connection successful!!
