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


<img width="356" alt="image" src="https://github.com/user-attachments/assets/1d121588-51fc-4692-82f9-be6d2efd5ca6" />

While inspecting boa by Ghidra, we acquired OS Command Injection vulnerability at the part where handling `macstr` and `bandstr` parameters.(c.f. FUN_0045a1f8)

<img width="800" alt="image" src="https://github.com/user-attachments/assets/0ebedda5-58a9-4981-98ba-c9e1c12652bb" />

Using self-made search.py, we confirmed multi_ap_popup_client_details.htm including map_del_device.

---

## Vulnerability Verification

<img width="512" alt="image" src="https://github.com/user-attachments/assets/01445003-3db6-4288-8c89-bb3e7db04708" />

Connecting the vulnerable web interface, we couldn’t acquire any “Apply” buttons. After further inspection, we found that buttons and input forms were hidden by CSS options of this page.

<img width="506" alt="image" src="https://github.com/user-attachments/assets/0ec397f6-818f-42e1-90cb-2d70c10a046e" />

Using web browser’s dev tools, we disabled display parameter which was initially set to ‘none’.

<img width="512" alt="image" src="https://github.com/user-attachments/assets/dd4c2d3d-90f9-4fb8-aa68-557efe5794ad" />

After re-configuring CSS, we could acquire “Apply” buttons. 

<img width="539" alt="image" src="https://github.com/user-attachments/assets/bd8ad58b-513f-4637-b497-1d70bd5b7974" />

Using Burp Suite to put in arbitrary value, we could test various user inputs.

<img width="306" alt="image" src="https://github.com/user-attachments/assets/837e89f5-b4eb-46b7-8ab8-0c5d158fc444" />

On Burp Suite, offer “;echo%20123456%20>/tmp/hacked” value to “macstr” parameter, and add any string values to “clientoff” parameter, which eventually leads to “bandstr” parameter.

---

## Result

<img width="141" alt="image" src="https://github.com/user-attachments/assets/ac43d032-2f49-4445-bd5b-810727007176" />

After that, we could confirm the command injection by inspecting the file we have created by command we injected.

<img width="713" alt="image" src="https://github.com/user-attachments/assets/858436e6-e664-4410-95ec-d9a15c51ec36" />

We also confirmed that “rm” command also works the same.
