# Proof of Concept for: **Totolink A3002R V4_Firmware V4.0.0-B20230531.1404**

> https://www.cve.org/CVERecord?id=CVE-2025-55588

---

**Contributor :** Lee Jong Hoon, Yang In Gyu, Jeong Yun Ho, Park Seong Ho, Lim Chan Su

**Vuln. Identified** : 2025.03.03
**CVE Designated** : 2025.8.18

**Testing Environment** : Ubuntu 22.04 LTS / FirmAE

## Vulnerability Info

### Firmware Version

- `TOTOLINK A3002R V4`
- `TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404.web`

### Vulnerability Type
- `Buffer overflow`

### 1-Line Description
- TOTOLINK A3002RV4 has a buffer overflow vulnerability due to insufficient parameter processing at portfw endpoint.
---

## Vulnerability Acquirement
![스크린샷 2025-03-07 150410](https://github.com/user-attachments/assets/2e551d6c-b626-43dc-9696-7d1ae2a6a7c3)

Identified the use of sprintf function on the script, which receives ip_subnet and fw_ip value from user input. It stores the result in a string variable.(c.f. ghidra - formPortFw/FUN_00416588))


---

## Vulnerability Verification

![image](https://github.com/user-attachments/assets/334518a0-a17a-4980-b74d-525d470858b3)

Access the website, enter the values, and click "Apply," then check it using Burp Suite.

![image](https://github.com/user-attachments/assets/e61aecce-1deb-4075-a860-697987d4616c)

Enter "aaaa...." in the fw_ip parameter and click "Send".

---

## Result

![스크린샷 2025-03-11 141454](https://github.com/user-attachments/assets/b08c0782-b919-424c-aca9-359e205ae0c3)

![스크린샷 2025-03-11 141504](https://github.com/user-attachments/assets/61f0d377-c40f-414f-8ff9-e9262295176f)

gdb-multiarch settings
```
set architecture mips
set endian little
set follow-fork-mode parent

b *0x415dd4
target remote 192.168.0.1:1337
```

Upon checking the stack with gdb-multiarch, it was confirmed that the buffer overflow occurred as the stack was filled with numerous "aaaaaa...". Consequently, the Boa web server was terminated, making the website inaccessible.

---

## Video

According to Swind1er, the actual device has ASLR disabled.
https://gist.github.com/Swind1er/ee095fbfe13f77a5b45b39a5aa82bd17

ASLR is disabled by default in the real environment, so use the following command to disable ASLR in the simulation environment:

```
echo 0 > /proc/sys/kernel/randomize_va_space
```

https://github.com/user-attachments/assets/644acf4b-3bfd-4fd2-a159-d41bd5302cc3

In the firmAE emulator
```
cd /var/boa
boa &
```

In the Ubuntu
```
# 'formPortFw_ex.py' and 'busybox-mipsel' file must be in the same location.
python3 formPortFw_ex.py
```


