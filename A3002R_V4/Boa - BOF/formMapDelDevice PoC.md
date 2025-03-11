# Proof of Concept for: **Totolink A3002R V4_Firmware V4.0.0-B20230531.1404**

---

**Contributor :** Lee Jong Hoon, Yang In Gyu, Jeong Yun Ho, Park Seong Ho, Lim Chan Su

**Date** : 2025/03/03

**Testing Environment** : Ubuntu 22.04 LTS

## Vulnerability Info

### Firmware Version
• TOTOLINK A3002R V4
• TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404.web

### Vulnerability Type
• Buffer overflow

### 1-Line Description
• TOTOLINK A3002RV4 has a buffer overflow vulnerability due to insufficient parameter processing at formMapDelDevice endpoint.

---

## Vulnerability Acquirement

![1](https://github.com/user-attachments/assets/a4087303-a058-4b4a-922b-fb85fd4a1f8b)


TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404 펌웨어에는 `0x45a1f8` 함수에 버퍼 오버플로우 취약점이 있습니다. `param_1`은 hostname 파라미터에서  입력을 받습니다.  해당 파라미터의 엔드포인트는 “formMapDelDevice”이며 multi_ap_popup_client_details.htm URl에서 동작합니다. 

---

## Vulnerability Verification

![2](https://github.com/user-attachments/assets/a1d6c427-468d-415c-8f26-52a5d6b31d08)

POST 요청을 위해 해당 파라미터를 전송하는 `multi_ap_popup_client_details.htm` 에 접속하여 전송버튼을 개발자 도구로 비활성화 합니다.

![3](https://github.com/user-attachments/assets/c7d45c05-3386-46d4-a7c5-9942d7b4a4b5)

display : none; 비활성화


![4](https://github.com/user-attachments/assets/91468c7c-6e89-4b46-a29d-03fb144b2da7)

hostname 파라미터를 전송하는 입력창이 나옵니다.

![5](https://github.com/user-attachments/assets/ec9c971b-d827-4d41-8df0-1bd8aaf6d44b)

해당 창에 임의의 값을 입력하면 hostname 파라미터에 값이 들어가는 것을 확인


---

## Result

![6](https://github.com/user-attachments/assets/936e28a5-bbe9-415f-9d95-8fbcbe3b7f53)

hostname 파라미터에 오버플로우가 일어날 만큼의 많은 “a”를 집어 넣으면 boa 웹 서버가 강제로 종료되며 웹 서비스를 이용할 수 없습니다.

![7](https://github.com/user-attachments/assets/c1ee60a1-600a-4ffa-9fa9-531dbf497125)

Boa 웹 서버가 종료되어 웹 인터페이스에 접근할 수 없는 것을 확인할 수 있습니다.


## Video

https://github.com/user-attachments/assets/994b56d0-48d0-4012-abcc-376f2b86998c

The video's `python3 ex.py` should be changed to `python3 formDelDevicePoC.py`.
