#!/usr/bin/env python3
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC, use --help for info.")
    return options

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    
    # 1. Take the interface down (Disconnects WiFi briefly)
    subprocess.call(["ifconfig", interface, "down"])
    
    # 2. Change the MAC address
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    
    # 3. Bring the interface back up
    subprocess.call(["ifconfig", interface, "up"])

# --- Main Execution ---
if __name__ == "__main__":
    options = get_arguments()
    change_mac(options.interface, options.new_mac)
