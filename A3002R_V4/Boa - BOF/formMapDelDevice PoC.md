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

![image.png](attachment:63d42f52-28e4-4beb-baee-14b4502e87d2:image.png)

TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404 펌웨어에는 `0x45a1f8` 함수에 버퍼 오버플로우 취약점이 있습니다. `param_1`은 hostname 파라미터에서  입력을 받습니다.  해당 파라미터의 엔드포인트는 “formMapDelDevice”이며 multi_ap_popup_client_details.htm URl에서 동작합니다. 

---

## Vulnerability Verification

![image.png](attachment:ece1325f-3567-409d-a7ce-492dcab2267b:image.png)

POST 요청을 위해 해당 파라미터를 전송하는 `multi_ap_popup_client_details.htm` 에 접속하여 전송버튼을 개발자 도구로 비활성화 합니다.

![image.png](attachment:7cf346e8-7aa8-428e-80d0-5fdbd3d32293:image.png)
display : none; 비활성화


![image.png](attachment:f3046b65-a97b-4b56-b3e1-998393a2e77b:image.png)
hostname 파라미터를 전송하는 입력창이 나옵니다.

![image.png](attachment:15ce3d61-ed0e-4322-8d19-fee97266c5b2:image.png)
해당 창에 임의의 값을 입력하면 hostname 파라미터에 값이 들어가는 것을 확인


---

## Result

![image.png](attachment:94498d76-0341-4d29-a70b-7a27bd1824bc:image.png)
hostname 파라미터에 오버플로우가 일어날 만큼의 많은 “a”를 집어 넣으면 boa 웹 서버가 강제로 종료되며 웹 서비스를 이용할 수 없습니다.

![image.png](attachment:ef505756-785b-4c3f-9a58-f34f15690999:image.png)
Boa 웹 서버가 종료되어 웹 인터페이스에 접근할 수 없는 것을 확인할 수 있습니다.


## Video

https://github.com/user-attachments/assets/994b56d0-48d0-4012-abcc-376f2b86998c

The video's `python3 ex.py` should be changed to `python3 formDelDevicePoC.py`.
