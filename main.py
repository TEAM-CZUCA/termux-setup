import os
import sys
import time
import subprocess

# Auto-install requests if not found
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null 2>&1')
    import requests

# ==========================================
# এখানে আপনার package.txt এর RAW লিংক দিন
PACKAGE_URL = "https://raw.githubusercontent.com/TEAM-CZUCA/termux-setup/main/package.txt"
# ==========================================

# Color Codes
G = '\033[1;32m'
R = '\033[1;31m'
C = '\033[1;36m'
W = '\033[0m'
Y = '\033[1;33m'

def typing_effect(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def show_banner():
    os.system('clear')
    try:
        with open('banner.txt', 'r') as f:
            banner = f.read()
            print(C + banner + W)
    except FileNotFoundError:
        print(R + "[-] Error: banner.txt not found in the directory!" + W)
    
    print(G + "\t[+] Tools Maker: " + Y + "LEVIATHAN DRIFT 419" + G + " [+]\n" + W)
    print(C + "="*55 + W)

def fetch_package_list():
    typing_effect(Y + "[*] Connecting to server to fetch package list..." + W)
    try:
        response = requests.get(PACKAGE_URL, timeout=10)
        if response.status_code == 200:
            typing_effect(G + "[+] Package list fetched successfully!\n" + W)
            return response.text.splitlines()
        else:
            typing_effect(R + f"[-] Failed to fetch! HTTP Status Code: {response.status_code}" + W)
            sys.exit()
    except Exception as e:
        typing_effect(R + f"[-] Network Error: {e}" + W)
        typing_effect(Y + "[!] Please check your internet connection or the URL." + W)
        sys.exit()

def execute_packages(commands):
    # Filter out empty lines and comments
    valid_commands = [cmd.strip() for cmd in commands if cmd.strip() and not cmd.strip().startswith("#")]
    total = len(valid_commands)
    
    for i, cmd in enumerate(valid_commands):
        print(C + f"\n[{i+1}/{total}] Executing: {Y}{cmd}{W}")
        
        try:
            # Advanced subprocess for real-time output reading
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in process.stdout:
                sys.stdout.write(W + line.decode('utf-8', errors='ignore'))
            process.wait()
            
            if process.returncode == 0:
                print(G + f"\n[✔] SUCCESS: {cmd}" + W)
            else:
                print(R + f"\n[✘] FAILED: {cmd} (Exit code: {process.returncode})" + W)
        except Exception as e:
            print(R + f"\n[-] ERROR executing {cmd}: {e}" + W)
        
        print(C + "-"*55 + W)

def main():
    show_banner()
    
    if "আপনার_ইউজারনেম" in PACKAGE_URL:
        typing_effect(R + "[-] WARNING: You haven't added the package.txt URL in main.py!" + W)
        typing_effect(Y + "[!] Edit main.py and change PACKAGE_URL to your RAW link." + W)
        sys.exit()
        
    commands_list = fetch_package_list()
    
    typing_effect(C + "[*] Press Enter to start the Advanced Setup..." + W)
    input()
    
    execute_packages(commands_list)
    
    print("\n" + G + "="*55 + W)
    typing_effect(G + "\t[✔] SETUP COMPLETED SUCCESSFULLY! [✔]" + W)
    typing_effect(Y + "\t    Thank you for using TEAM-CZUCA Tools." + W)
    print(G + "="*55 + "\n" + W)

if __name__ == "__main__":
    main()
