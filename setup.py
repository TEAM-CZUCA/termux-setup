import os
import time

# Banner load
def banner():
    os.system("clear")
    with open("banner.txt", "r") as f:
        print(f.read())

# Install packages
def install_packages():
    print("\n[+] Updating Termux...")
    os.system("pkg update -y && pkg upgrade -y")

    print("\n[+] Installing packages...\n")
    with open("packages.txt", "r") as f:
        packages = f.read().splitlines()

    for pkg in packages:
        print(f"[Installing] {pkg}")
        os.system(f"pkg install {pkg} -y")

    print("\n[✔] All packages installed!")

# Extra setup
def extra():
    print("\n[+] Running extra setup...")
    os.system("termux-setup-storage")
    os.system("pip install --upgrade pip")
    os.system("pip install requests rich")

# Menu
def menu():
    banner()
    print("""
1. Auto Setup (All Tools Install)
2. Update System
3. Exit
""")

    choice = input("Select option: ")

    if choice == "1":
        install_packages()
        extra()
    elif choice == "2":
        os.system("pkg update -y && pkg upgrade -y")
    elif choice == "3":
        exit()
    else:
        print("Invalid!")

if __name__ == "__main__":
    menu()
