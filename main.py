import os
import sys
import time
import subprocess

# ==========================================
# Auto-install requests & Force Permissions
# ==========================================
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null 2>&1')
    import requests

# Force Storage Permission & Execute Permission
os.system('termux-setup-storage')
try:
    os.system(f'chmod +x {__file__} > /dev/null 2>&1')
except:
    pass

# ==========================================
# Configurations (আপনার তথ্য এখানে দিন)
# ==========================================
PASSWORD = "czuca"  # এখানে আপনার পাসওয়ার্ড দিন
FB_PAGE_URL = "https://www.facebook.com/CyberZulfikarUnderCoverAgency" # আপনার ফেসবুক পেইজ লিংক

# অটো আপডেটের জন্য আপনার এই পাইথন স্ক্রিপ্টটির RAW লিংক দিন (শুধুমাত্র main.py আপডেট করার জন্য)
UPDATE_URL = "https://raw.githubusercontent.com/TEAM-CZUCA/termux-setup/main/main.py" 

# ==========================================
# Color Codes
# ==========================================
G = '\033[1;32m'
R = '\033[1;31m'
C = '\033[1;36m'
W = '\033[0m'
Y = '\033[1;33m'

# ==========================================
# Animations & Banners
# ==========================================
def typing_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def show_banner():
    os.system('clear')
    try:
        with open('banner.txt', 'r', encoding='utf-8') as f:
            banner = f.read()
            print(C + banner + W)
    except FileNotFoundError:
        print(R + "[-] Error: banner.txt not found in the directory!" + W)
        print(Y + "[!] Please make sure banner.txt is in the same folder.\n" + W)

def welcome_animation():
    os.system('clear')
    print(C + "\n\n\n\n\n\n")
    typing_effect(G + "\t[+] WELCOME TO TEAM-CZUCA SETUP TOOL [+]", 0.05)
    typing_effect(Y + "\t    Initializing System Components...", 0.04)
    time.sleep(1)

# ==========================================
# Security & Redirection
# ==========================================
def security_check():
    os.system('clear')
    print(C + "="*55 + W)
    print(G + "\t[!] TOOL PROTECTED BY PASSWORD [!]" + W)
    print(C + "="*55 + W)
    
    user_pass = input(Y + "\n[+] Enter Password: " + W)
    
    if user_pass == PASSWORD:
        print(G + "\n[✔] Password Correct! Login Successful." + W)
        print(C + "[*] Redirecting to Facebook Page..." + W)
        time.sleep(1)
        # Open FB page in Termux
        os.system(f"termux-open {FB_PAGE_URL} > /dev/null 2>&1")
        
        # 5 Second Wait before showing tool
        print(Y + "[!] Please wait 5 seconds..." + W)
        time.sleep(5)
        welcome_animation()
    else:
        print(R + "\n[✘] Wrong Password! Access Denied." + W)
        sys.exit()

# ==========================================
# Auto Update System
# ==========================================
def auto_update():
    show_banner()
    typing_effect(Y + "[*] Checking for main.py updates..." + W)
    try:
        response = requests.get(UPDATE_URL, timeout=10)
        if response.status_code == 200:
            with open(__file__, 'w', encoding='utf-8') as file:
                file.write(response.text)
            typing_effect(G + "[✔] Update Successful! Restarting tool..." + W)
            time.sleep(2)
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            typing_effect(R + f"[-] Update Failed! HTTP Status: {response.status_code}" + W)
            time.sleep(2)
    except Exception as e:
        typing_effect(R + f"[-] Network Error during update: {e}" + W)
        time.sleep(2)

# ==========================================
# Core Functions (Read Local package.txt)
# ==========================================
def read_package_list():
    typing_effect(Y + "\n[*] Loading package list from local package.txt..." + W)
    try:
        with open('package.txt', 'r', encoding='utf-8') as f:
            commands = f.read().splitlines()
            typing_effect(G + "[+] Package list loaded successfully!\n" + W)
            return commands
    except FileNotFoundError:
        typing_effect(R + "[-] Error: package.txt not found!" + W)
        typing_effect(Y + "[!] Please create package.txt in the same directory." + W)
        return []

def execute_packages(commands):
    valid_commands =[cmd.strip() for cmd in commands if cmd.strip() and not cmd.strip().startswith("#")]
    total = len(valid_commands)

    if total == 0:
        print(R + "[-] No valid commands found to execute!" + W)
        return

    for i, cmd in enumerate(valid_commands):
        print(C + f"\n[{i+1}/{total}] Executing: {Y}{cmd}{W}")
        try:
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

# ==========================================
# Menu System
# ==========================================
def main_menu():
    while True:
        show_banner()
        print(G + "\t[1] " + Y + "Start Basic Setup (Install Packages)")
        print(G + "\t[2] " + Y + "Update This Tool")
        print(G + "\t[3] " + Y + "Exit Tool")
        print(C + "\n=======================================================" + W)
        
        choice = input(G + " [+] Select an option: " + W)
        
        if choice == '1':
            commands_list = read_package_list()
            if commands_list:
                typing_effect(C + "[*] Press Enter to start the Advanced Setup..." + W)
                input()
                execute_packages(commands_list)
                
                print("\n" + G + "="*55 + W)
                typing_effect(G + "\t[✔] SETUP COMPLETED SUCCESSFULLY! [✔]" + W)
                typing_effect(Y + "\t    Thank you for using TEAM-CZUCA Tools." + W)
                print(G + "="*55 + "\n" + W)
            input(C + "\nPress Enter to return to Menu..." + W)
            
        elif choice == '2':
            auto_update()
            
        elif choice == '3':
            typing_effect(R + "[!] Exiting Tool. Goodbye!" + W)
            sys.exit()
            
        else:
            print(R + "\n[-] Invalid Option! Please try again." + W)
            time.sleep(1)

# ==========================================
# Execution Start
# ==========================================
if __name__ == "__main__":
    security_check()
    main_menu()
