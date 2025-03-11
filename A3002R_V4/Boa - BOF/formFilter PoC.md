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

TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404 펌웨어에는 0x416ddc 함수에 버퍼 오버플로우 취약점이 있습니다. param_1 은 POST요청에서 URL 파라미터를 입력 받습니다. 사용자 입력을 받는 위치에서 strcpy 함수에서 길이에 대한 검증이 없어 버퍼 오버플로우 취약점을 일으킬 수 있습니다.


---

## Vulnerability Verification

![12](https://github.com/user-attachments/assets/6a924fe4-64fe-466f-ab50-dd7d7c622910)

해당 URL Address가 url 파라미터를 입력 받는 위치입니다.

![13](https://github.com/user-attachments/assets/3c5b1401-1298-4604-bca5-3ca422016711)

url 파라미터에 “test” 값이 들어가 있는 것을 확인


---

## Result

![14](https://github.com/user-attachments/assets/530e0d84-d80f-4898-ad87-cd45a79d5f84)

url 파라미터에 수 많은 “a”를 넣습니다

![15](https://github.com/user-attachments/assets/51800dc8-eccb-4f4f-bd9a-5c91066b406c)

Boa 웹 서버가 종료되어 웹 인터페이스에 접근할 수 없는 것을 확인할 수 있습니다.

---

## Video

https://github.com/user-attachments/assets/d0f25fbf-8818-4e63-8cb0-1c39695e9c2d

The video's `python3 ex.py` should be changed to `python3 formFilterPoC.py`.
