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

- `TOTOLINK-A3002R-Ge-V4.0.0-B20230531` includes OS Commend Injection vulnerability. This occurs at “macstr, bandstr, clientoff” parameters of /bin/boa.

---

## Vulnerability Acquirement



While inspecting boa by Ghidra, we acquired OS Command Injection vulnerability at the part where handling `macstr` and `bandstr` parameters.(c.f. FUN_0045a1f8)



Using self-made search.py, we confirmed multi_ap_popup_client_details.htm including map_del_device.

---

## Vulnerability Verification



Connecting the vulnerable web interface, we couldn’t acquire any “Apply” buttons. After further inspection, we found that buttons and input forms were hidden by CSS options of this page.



Using web browser’s dev tools, we disabled display parameter which was initially set to ‘none’.



After re-configuring CSS, we could acquire “Apply” buttons. 



Using Burp Suite to put in arbitrary value, we could test various user inputs.



On Burp Suite, offer “;echo%20123456%20>/tmp/hacked” value to “macstr” parameter, and add any string values to “clientoff” parameter, which eventually leads to “bandstr” parameter.

---

## Result



After that, we could confirm the command injection by inspecting the file we have created by command we injected.



We also confirmed that “rm” command also works the same.
