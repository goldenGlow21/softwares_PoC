## **취약점 종류**
    - Incorrect Access Control

## **Vendor**
    - Totolink

## **영향받은 제품/버전**
    - TOTOLINK A3002R V4
    - TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404.web

## **Affected component**
    - Root Privilege
    - All file accessible as root
    - telnetd

## **Attack vector**
    - Scanning port status using Nmap after emulating the firmware, we acquired port 23 and telnet service running.
    - The attacker can gain hard-coded credentials from `~/etc/shadow.sample`
    - The credential is hashed by vulnerable algorithm, MD5
    - Using basic tools to unhash the hash value, attacker gains password, “123456”
    - After that, attacker can connect to telnet, using command `telnet 192.168.0.1`
    - As `~/etc/shadow.sample` indicates, attacker can gain access to root privilege by using credential, `root:123456`

## **Suggested description of the vulnerability for use in the CVE**
    - TOTOLINK-A3002R-Ge-V4.0.0-B20230531.1404 firmware is exposing its default credential, which allows attackers to gain access for telnet and root shell privilege afterward.

## **Discoverer(s)/Credits**
    - Park Seong Ho
    - Lee Jong Hoon
    - Lim Chan Su
    - Yang In Gyu
    - Jeong Yun Ho

## **Additional information**
    - After gaining root shell privilege, we confirmed that the attacker can change file mode(`chmod +x`), change root password without any additional authentication. Given root privilege, the attacker is considered to perform any actions desired.