# 👻 GhostMac v2.0

![Kali](https://img.shields.io/badge/Kali-Linux-blue?style=flat&logo=kali-linux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**GhostMac** is an automated, stealth-focused MAC address spoofer designed for Red Team operations on Kali Linux. It allows you to rapidly change your network identity with built-in verification to ensure you never leak your true hardware address.

---

## 🚀 Features
* **👻 Ghost Mode:** Generates a mathematically valid, 100% random MAC address on the fly.
* **🛡️ State Verification:** Uses Regex to verify the system's actual MAC address *before* and *after* the attack.
* **⚡ Automated Execution:** Automatically handles taking the interface offline, injecting the new MAC, and bringing it back online.

---

## 🛠️ Installation & Usage

**1. Clone the repository:**
`git clone https://github.com/Rafiq-root/GhostMac.git`
`cd GhostMac`

**2. Run the tool (Requires Root):**
`sudo python3 ghostmac.py`

---

## ⚠️ Disclaimer
This tool is built for ethical hacking, penetration testing, and educational purposes only. Do not use on networks you do not own or have explicit permission to test.
