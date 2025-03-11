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



Confirming the usage of system() function on line 55, we inspected the page that is using formMapDel.



We hereby confirmed multi_ap_popup_device_del.htm, and therefore re-searched for pages that are using multi_ap_popup_device_del.htm.



As a result, we could find web interface route.

---

## Vulnerability Verification



After connecting to the web interface, we can navigate by following route: “EasyMesh → multi_ap_setting_topology_mod.htm → multi_ap_popup_device_del.htm”.

However, if we try to get into the “EasyMesh” menu, the emulated web interface shows us nothing but blank page. We tantatively concluded that this option fails due to mechanical problems of emulator.



If we use url page to directly connect to “192.168.0.1/multi_ap_…”, it seems that this page is allocated for deleting mesh node. However, if we click delete button, only error-response popup appears, since zero nodes were added to the mesh.(or even selected)



Thereby we decided to send packets from any page that sends apply request to the server.



After clicking the “apply” button, we checked Burp Suite and changed packet components as intended. If you want to try it yourself, you can follow the picture below this statement.(Upper picture shows the initial state.)



Changing the “url” and “post” parameters as we are sending on EasyMesh, we forwarded packet.

---

## Result



We hereby confirmed /tmp/hacked file’s generation, which indicates seccess of Command Injection attack.
