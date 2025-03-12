# Proof of Concept for: **Totolink A3002R V4_Firmware V4.0.0-B20230531.1404**

---

**Contributor :** Lee Jong Hoon, Yang In Gyu, Jeong Yun Ho, Park Seong Ho, Lim Chan Su

**Date** : 2025/03/03

**Testing Environment** : Ubuntu 22.04 LTS

## Vulnerability Info

### Firmware Version

- `TOTOLINK A3002R V4`

- `TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404.web`

### Vulnerability Type

• Buffer overflow

### 1-Line Description
• TOTOLINK A3002RV4 has a buffer overflow vulnerability due to insufficient parameter processing at formFilter endpoint.

---

## Vulnerability Acquirement

![11](https://github.com/user-attachments/assets/fcb5ae1a-23e7-4950-8673-761fc0fa1eca)

A buffer overflow vulnerability exists in the 0x416ddc function of the TOTOLINK A3002R-Ge V4.0.0-B20230531.1404 firmware. The param_1 variable receives input from the URL parameter in a POST request. However, there is no length validation in the strcpy function handling this input, leading to a potential buffer overflow vulnerability.


---

## Vulnerability Verification

![12](https://github.com/user-attachments/assets/6a924fe4-64fe-466f-ab50-dd7d7c622910)

The URL parameter in the following address is where the user input is processed.

![13](https://github.com/user-attachments/assets/3c5b1401-1298-4604-bca5-3ca422016711)

Observing that the url parameter contains the value "test".


---

## Result

![14](https://github.com/user-attachments/assets/530e0d84-d80f-4898-ad87-cd45a79d5f84)

Injecting a large number of "a" characters into the url parameter.

![15](https://github.com/user-attachments/assets/51800dc8-eccb-4f4f-bd9a-5c91066b406c)

The Boa web server crashes, making the web interface inaccessible.

---

## Video

https://github.com/user-attachments/assets/d0f25fbf-8818-4e63-8cb0-1c39695e9c2d

The video's `python3 ex.py` should be changed to `python3 formFilterPoC.py`.
