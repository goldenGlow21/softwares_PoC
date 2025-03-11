# Proof of Concept for: **Totolink A3002R V4_Firmware V4.0.0-B20230531.1404**

---

**Contributor :** Lee Jong Hoon, Yang In Gyu, Jeong Yun Ho, Park Seong Ho, Lim Chan Su

**Date** : 

**Testing Environment** : 

## Vulnerability Info

### Firmware Version

### Vulnerability Type

### 1-Line Description

---

## Vulnerability Acquirement

(취약점 발견까지의 과정 및 조사 내용)

<img width="695" alt="image" src="https://github.com/user-attachments/assets/8049780a-dfe4-49ec-a674-185093a55760" />

While operating the emulator for the firmware and analyzing server vulnerabilities, I found that the shadow, shadow.sample file was using the MD5 hash algorithm

![123123](https://github.com/user-attachments/assets/1d0b2ad1-45cb-43e0-bb57-0ebbecff49a6)

I analyzed init.sh through Ghidra

![1231234](https://github.com/user-attachments/assets/a270e58b-1d68-406f-8e71-cfd238bc6694)



---

## Vulnerability Verification

(취약점 exploit 내용)




![telnet](https://github.com/user-attachments/assets/dca6f395-d7a0-4228-a586-d02b0f66ad6d)

Copy all contents of the shadow.sample file

![ㅋ1](https://github.com/user-attachments/assets/aadbf590-93b4-41ce-a654-d345b82b4876)

Put all the copied values in the hash.txt file and attempt to crack using the John the Ripper tool

![tel](https://github.com/user-attachments/assets/1babdd14-d435-42e4-b639-63df27eb83cb)

As previously analyzed, we identified that Telnet is operating and performed a port scan using the Nmap tool, and confirmed that it is also using Telnet Port 23

---

## Result

![ㅋ2](https://github.com/user-attachments/assets/cfc807a4-b302-46de-a7e1-82aaa49a950a)

Connection successful
