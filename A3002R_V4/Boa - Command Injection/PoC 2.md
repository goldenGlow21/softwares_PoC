# Proof of Concept for: **Totolink A3002R V4_Firmware V4.0.0-B20230531.1404**

---

**Contributor :** Lee Jong Hoon, Yang In Gyu, Jeong Yun Ho, Park Seong Ho, Lim Chan Su

**Date** : 2025.03.08

**Testing Environment** : Ubuntu 22.04 LTS / Kali Linux 2024.4 amd64 / FirmAE

## Vulnerability Info

### Firmware Version

- `TOTOLINK A3002R V4`
- `TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404.web`

### Vulnerability Type

- Command Injection

### 1-Line Description

- `TOTOLINK-A3002R-Ge-V4.0.0-B20230531` includes OS Command Injection vulnerability, which occurs from “devicemac” parameter of `boa` ’s `formMapDel` endpoint.

---

## Vulnerability Acquirement

<img width="470" alt="image" src="https://github.com/user-attachments/assets/4613a01e-5a5b-448f-83ce-89c26ff84481" />

Confirming the usage of system() function on line 55, we inspected the page that is using formMapDel.

<img width="800" alt="image" src="https://github.com/user-attachments/assets/6f028c42-6a4b-4fe6-9fab-2a5e39ccda71" />

We hereby confirmed multi_ap_popup_device_del.htm, and therefore re-searched for pages that are using multi_ap_popup_device_del.htm.

<img width="800" alt="image" src="https://github.com/user-attachments/assets/c15c4c2a-3632-4b44-ba07-a67dfbaa14b8" />

As a result, we could find web interface route.

---

## Vulnerability Verification

<img width="504" alt="image" src="https://github.com/user-attachments/assets/cdf1cbed-7180-477c-8e96-2507e67adb00" />

After connecting to the web interface, we can navigate by following route: “EasyMesh → multi_ap_setting_topology_mod.htm → multi_ap_popup_device_del.htm”.

However, if we try to get into the “EasyMesh” menu, the emulated web interface shows us nothing but blank page. We tantatively concluded that this option fails due to mechanical problems of emulator.

<img width="511" alt="image" src="https://github.com/user-attachments/assets/8fa13c29-1f98-41b0-841e-9abc3675a0b1" />

If we use url page to directly connect to “192.168.0.1/multi_ap_…”, it seems that this page is allocated for deleting mesh node. However, if we click delete button, only error-response popup appears, since zero nodes were added to the mesh.(or even selected)

<img width="468" alt="image" src="https://github.com/user-attachments/assets/93ebfb3c-c7ef-47ef-bcb0-32b617098613" />

Thereby we decided to send packets from any page that sends apply request to the server.

<img width="301" alt="image" src="https://github.com/user-attachments/assets/d132fc75-0ff1-4385-b92d-18fe9bc2278d" />

After clicking the “apply” button, we checked Burp Suite and changed packet components as intended. If you want to try it yourself, you can follow the picture below this statement.(Upper picture shows the initial state.)

<img width="299" alt="image" src="https://github.com/user-attachments/assets/69d31736-3dad-48f3-b371-ed2d46677ba8" />

Changing the “url” and “post” parameters as we are sending on EasyMesh, we forwarded packet.

---

## Result

<img width="671" alt="image" src="https://github.com/user-attachments/assets/ad7491bd-39ce-41d5-a1f1-ed53ca49bdcc" />

We hereby confirmed /tmp/hacked file’s generation, which indicates seccess of Command Injection attack.
