#!/usr/bin/env python3
import subprocess
import re
import random

def get_current_mac(interface):
    """Reads the current MAC address directly from the system using Regex."""
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
        mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
        
        if mac_search:
            return mac_search.group(0)
        else:
            return None
    except Exception:
        print(f"[-] Error: Could not read interface {interface}.")
        return None

def generate_random_mac():
    """Generates a random, valid locally-administered MAC address."""
    chars = "0123456789abcdef"
    # Starting with '02' ensures the MAC is valid and accepted by most network cards
    random_mac = "02"
    for i in range(5):
        random_mac += ":" + random.choice(chars) + random.choice(chars)
    return random_mac

def change_mac(interface, new_mac):
    """Executes the system commands to spoof the MAC address."""
    print(f"[*] Taking {interface} offline...")
    subprocess.call(["ifconfig", interface, "down"])
    
    print(f"[*] Injecting new MAC address: {new_mac}...")
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    
    print(f"[*] Bringing {interface} back online...")
    subprocess.call(["ifconfig", interface, "up"])

# --- Main Execution ---
print("========================================")
print("          👻 GhostMac v2.0 👻          ")
print("========================================")

# 1. Get user input
interface = input("[?] Target Interface (e.g., eth0, wlan0): ")

# 2. Check the BEFORE state
current_mac = get_current_mac(interface)
if current_mac:
    print(f"[*] Current Identity (MAC): {current_mac}")
else:
    print("[-] Aborting. Interface not found or invalid.")
    exit(1)

# 3. Choose the Attack Mode
print("\n[1] Enter a MAC address manually")
print("[2] Generate a completely random MAC (Ghost Mode)")
choice = input("[?] Select an option (1 or 2): ")

if choice == "2":
    new_mac = generate_random_mac()
    print(f"[*] 👻 Ghost Mode Activated. Generated Identity: {new_mac}")
else:
    new_mac = input("[?] Enter target MAC (e.g., 00:11:22:33:44:55): ")

# 4. Execute the Attack
print("\n[*] Initiating Ghost Protocol...")
change_mac(interface, new_mac)

# 5. Check the AFTER state (The Verification)
final_mac = get_current_mac(interface)

if final_mac == new_mac:
    print(f"\n[+] SUCCESS! Identity successfully spoofed to: {final_mac}")
else:
    print(f"\n[-] FAILED! MAC address is still: {final_mac}")
