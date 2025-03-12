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


A buffer overflow vulnerability exists in the `0x45a1f8` function of the `TOTOLINK A3002R-Ge V4.0.0-B20230531.1404` firmware. The `param_1` variable receives input from the `hostname` parameter. This parameter is processed by the `formMapDelDevice` endpoint, which operates within the `multi_ap_popup_client_details.htm` URL.

---

## Vulnerability Verification

![2](https://github.com/user-attachments/assets/a1d6c427-468d-415c-8f26-52a5d6b31d08)

To send a POST request with this parameter access `multi_ap_popup_client_details.htm` and disable the submit button using developer tools.

![3](https://github.com/user-attachments/assets/c7d45c05-3386-46d4-a7c5-9942d7b4a4b5)

Modify the button’s style by removing `display: none;` to make it visible.


![4](https://github.com/user-attachments/assets/91468c7c-6e89-4b46-a29d-03fb144b2da7)

A text input field for the `hostname` parameter appears.

![5](https://github.com/user-attachments/assets/ec9c971b-d827-4d41-8df0-1bd8aaf6d44b)

Entering arbitrary values in this field confirms that the input is passed to the `hostname` parameter.


---

## Result

![6](https://github.com/user-attachments/assets/936e28a5-bbe9-415f-9d95-8fbcbe3b7f53)

Injecting an excessive number of `"a"` characters into the `hostname` parameter causes a buffer overflow, forcing the Boa web server to crash.

![7](https://github.com/user-attachments/assets/c1ee60a1-600a-4ffa-9fa9-531dbf497125)

As a result, the web interface becomes inaccessible.


## Video

https://github.com/user-attachments/assets/994b56d0-48d0-4012-abcc-376f2b86998c

The video's `python3 ex.py` should be changed to `python3 formDelDevicePoC.py`.
