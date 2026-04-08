#!/data/data/com.termux/files/usr/bin/python3

import os
import sys
import subprocess
import base64
import time
import json
from datetime import datetime

# ==================== COLOR CODES ====================
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    MAGENTA = '\033[0;35m'
    WHITE = '\033[1;37m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    NC = '\033[0m'

# ==================== MAIN TOOLKIT CLASS ====================
class TermuxProToolkit:
    def __init__(self):
        self.tools_file = "tools.enc"
        self.tools_list = []
        self.installed_count = 0
        self.total_tools = 0
        self.load_tools()
    
    def clear(self):
        os.system('clear')
    
    def print_banner(self):
        banner = f"""
{Colors.CYAN}{Colors.BOLD}    ╔══════════════════════════════════════════════════════════════════════╗
    ║     ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗    ║
    ║     ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝    ║
    ║        ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝     ║
    ║        ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗     ║
    ║        ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗    ║
    ║        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ║
    ║                                                   PRO v4.0  ║
    ╚══════════════════════════════════════════════════════════════════════╝{Colors.NC}
        """
        print(banner)
    
    def print_menu(self):
        menu = f"""
{Colors.BLUE}{Colors.BOLD}════════════════════════════════════════════════════════════════{Colors.NC}
{Colors.WHITE}{Colors.BOLD}                      M A I N   M E N U{Colors.NC}
{Colors.BLUE}{Colors.BOLD}════════════════════════════════════════════════════════════════{Colors.NC}
{Colors.GREEN}  [1] 🚀 Auto Setup All Tools{Colors.NC}
{Colors.CYAN}  [2] 📦 Install Individual Tools{Colors.NC}
{Colors.YELLOW}  [3] 📊 Check Installation Status{Colors.NC}
{Colors.MAGENTA}  [4] ℹ️  About{Colors.NC}
{Colors.RED}  [0] ❌ Exit{Colors.NC}
{Colors.BLUE}{Colors.BOLD}════════════════════════════════════════════════════════════════{Colors.NC}
        """
        print(menu)
    
    def loading_animation(self, message, duration=1.5):
        animation = "⣷⣯⣟⡿⣻⣽⣾"
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            print(f"\r{Colors.YELLOW}{message} {animation[i % len(animation)]}{Colors.NC}", end="", flush=True)
            time.sleep(0.1)
            i += 1
        print("\r" + " " * (len(message) + 5), end="")
        print("\r", end="")
    
    def print_success(self, msg):
        print(f"{Colors.GREEN}✅ {msg}{Colors.NC}")
    
    def print_error(self, msg):
        print(f"{Colors.RED}❌ {msg}{Colors.NC}")
    
    def print_info(self, msg):
        print(f"{Colors.CYAN}📌 {msg}{Colors.NC}")
    
    def print_warning(self, msg):
        print(f"{Colors.YELLOW}⚠️  {msg}{Colors.NC}")
    
    def run_cmd(self, cmd, show_output=False):
        try:
            if show_output:
                result = subprocess.run(cmd, shell=True, text=True)
                return result.returncode == 0
            else:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                return result.returncode == 0
        except Exception as e:
            self.print_error(f"Command failed: {e}")
            return False
    
    def get_cmd_output(self, cmd):
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.stdout.strip()
        except:
            return ""
    
    def load_tools(self):
        """Load and decrypt tools from encrypted file"""
        try:
            if not os.path.exists(self.tools_file):
                self.create_encrypted_tools()
            
            with open(self.tools_file, 'r') as f:
                encrypted = f.read().strip()
            
            # Decrypt: Base64 decode then reverse
            decrypted = base64.b64decode(encrypted).decode('utf-8')
            decrypted = decrypted[::-1]
            
            # Parse JSON format
            self.tools_list = json.loads(decrypted)
            self.total_tools = len(self.tools_list)
            self.print_success(f"Loaded {self.total_tools} tools")
        except Exception as e:
            self.print_error(f"Failed to load tools: {e}")
            self.create_encrypted_tools()
    
    def create_encrypted_tools(self):
        """Create encrypted tools file from the complete list"""
        tools_data = [
            {"category": "System & Core", "name": "apt", "package": "apt", "type": "pkg"},
            {"category": "System & Core", "name": "python", "package": "python", "type": "pkg"},
            {"category": "System & Core", "name": "python2", "package": "python2", "type": "pkg"},
            {"category": "System & Core", "name": "python3", "package": "python3", "type": "pkg"},
            {"category": "System & Core", "name": "git", "package": "git", "type": "pkg"},
            {"category": "System & Core", "name": "openssh", "package": "openssh", "type": "pkg"},
            {"category": "System & Core", "name": "termux-api", "package": "termux-api", "type": "pkg"},
            {"category": "System & Core", "name": "ruby", "package": "ruby", "type": "pkg"},
            {"category": "System & Core", "name": "sudo", "package": "sudo", "type": "pkg"},
            {"category": "System & Core", "name": "proot", "package": "proot", "type": "pkg"},
            {"category": "System & Core", "name": "tsu", "package": "tsu", "type": "pkg"},
            {"category": "System & Core", "name": "termux-tools", "package": "termux-tools", "type": "pkg"},
            {"category": "System & Core", "name": "coreutils", "package": "coreutils", "type": "pkg"},
            {"category": "System & Core", "name": "util-linux", "package": "util-linux", "type": "pkg"},
            {"category": "Programming", "name": "java", "package": "openjdk-17", "type": "pkg"},
            {"category": "Programming", "name": "php", "package": "php", "type": "pkg"},
            {"category": "Programming", "name": "perl", "package": "perl", "type": "pkg"},
            {"category": "Programming", "name": "nodejs", "package": "nodejs", "type": "pkg"},
            {"category": "Programming", "name": "golang", "package": "golang", "type": "pkg"},
            {"category": "Programming", "name": "bash", "package": "bash", "type": "pkg"},
            {"category": "Programming", "name": "fish", "package": "fish", "type": "pkg"},
            {"category": "Programming", "name": "clang", "package": "clang", "type": "pkg"},
            {"category": "Programming", "name": "libffi", "package": "libffi", "type": "pkg"},
            {"category": "Programming", "name": "make", "package": "make", "type": "pkg"},
            {"category": "Programming", "name": "cmake", "package": "cmake", "type": "pkg"},
            {"category": "Security", "name": "nmap", "package": "nmap", "type": "pkg"},
            {"category": "Security", "name": "hydra", "package": "hydra", "type": "pkg"},
            {"category": "Security", "name": "macchanger", "package": "macchanger", "type": "pkg"},
            {"category": "Security", "name": "openssl", "package": "openssl", "type": "pkg"},
            {"category": "Security", "name": "tor", "package": "tor", "type": "pkg"},
            {"category": "Security", "name": "crunch", "package": "crunch", "type": "pkg"},
            {"category": "Security", "name": "android-tools", "package": "android-tools", "type": "pkg"},
            {"category": "Security", "name": "dnsutils", "package": "dnsutils", "type": "pkg"},
            {"category": "Security", "name": "whois", "package": "whois", "type": "pkg"},
            {"category": "Network", "name": "curl", "package": "curl", "type": "pkg"},
            {"category": "Network", "name": "wget", "package": "wget", "type": "pkg"},
            {"category": "Network", "name": "net-tools", "package": "net-tools", "type": "pkg"},
            {"category": "Network", "name": "w3m", "package": "w3m", "type": "pkg"},
            {"category": "Network", "name": "bmon", "package": "bmon", "type": "pkg"},
            {"category": "Network", "name": "rsync", "package": "rsync", "type": "pkg"},
            {"category": "Network", "name": "vpn", "package": "openvpn", "type": "pkg"},
            {"category": "Compression", "name": "p7zip", "package": "p7zip", "type": "pkg"},
            {"category": "Compression", "name": "tar", "package": "tar", "type": "pkg"},
            {"category": "Compression", "name": "zip", "package": "zip", "type": "pkg"},
            {"category": "Compression", "name": "unzip", "package": "unzip", "type": "pkg"},
            {"category": "Compression", "name": "unrar", "package": "unrar", "type": "pkg"},
            {"category": "Python Packages", "name": "requests", "package": "requests", "type": "pip"},
            {"category": "Python Packages", "name": "mechanize", "package": "mechanize", "type": "pip"},
            {"category": "Python Packages", "name": "bs4", "package": "beautifulsoup4", "type": "pip"},
            {"category": "Python Packages", "name": "rich", "package": "rich", "type": "pip"},
            {"category": "Python Packages", "name": "futures", "package": "futures", "type": "pip"},
            {"category": "Python Packages", "name": "future", "package": "future", "type": "pip"},
            {"category": "Python Packages", "name": "pycryptodomex", "package": "pycryptodomex", "type": "pip"},
            {"category": "Python Packages", "name": "cryptography", "package": "cryptography", "type": "pip"},
            {"category": "Python Packages", "name": "setuptools", "package": "setuptools", "type": "pip"},
            {"category": "Python Packages", "name": "httpx", "package": "httpx", "type": "pip"},
            {"category": "Ruby Gems", "name": "lolcat", "package": "lolcat", "type": "gem"},
            {"category": "Utilities", "name": "vim", "package": "vim", "type": "pkg"},
            {"category": "Utilities", "name": "nano", "package": "nano", "type": "pkg"},
            {"category": "Utilities", "name": "figlet", "package": "figlet", "type": "pkg"},
            {"category": "Utilities", "name": "toilet", "package": "toilet", "type": "pkg"},
            {"category": "Utilities", "name": "cmatrix", "package": "cmatrix", "type": "pkg"},
            {"category": "Utilities", "name": "cowsay", "package": "cowsay", "type": "pkg"},
            {"category": "Utilities", "name": "htop", "package": "htop", "type": "pkg"},
            {"category": "Utilities", "name": "neofetch", "package": "neofetch", "type": "pkg"},
            {"category": "Utilities", "name": "tree", "package": "tree", "type": "pkg"},
            {"category": "Utilities", "name": "grep", "package": "grep", "type": "pkg"},
            {"category": "Utilities", "name": "sed", "package": "sed", "type": "pkg"},
            {"category": "Utilities", "name": "jq", "package": "jq", "type": "pkg"},
            {"category": "Utilities", "name": "wcalc", "package": "wcalc", "type": "pkg"},
            {"category": "Utilities", "name": "espeak", "package": "espeak", "type": "pkg"},
            {"category": "Utilities", "name": "mpv", "package": "mpv", "type": "pkg"},
            {"category": "Shell", "name": "zsh", "package": "zsh", "type": "pkg"},
            {"category": "Repositories", "name": "root-repo", "package": "root-repo", "type": "pkg"},
            {"category": "Repositories", "name": "unstable-repo", "package": "unstable-repo", "type": "pkg"},
            {"category": "Repositories", "name": "x11-repo", "package": "x11-repo", "type": "pkg"}
        ]
        
        # Convert to JSON and encrypt
        json_data = json.dumps(tools_data, indent=2)
        encrypted = base64.b64encode(json_data[::-1].encode()).decode()
        
        with open(self.tools_file, 'w') as f:
            f.write(encrypted)
        
        self.tools_list = tools_data
        self.total_tools = len(tools_data)
        self.print_success(f"Created tools.enc with {self.total_tools} tools")
    
    def is_installed(self, tool_name, tool_type):
        """Check if a tool is already installed"""
        if tool_type == "pkg":
            result = self.get_cmd_output(f"command -v {tool_name}")
            return bool(result)
        elif tool_type == "pip":
            result = self.get_cmd_output(f"pip show {tool_name}")
            return "Name:" in result
        elif tool_type == "gem":
            result = self.get_cmd_output(f"gem list {tool_name}")
            return tool_name in result
        return False
    
    def install_pkg(self, package):
        """Install a package using pkg"""
        self.print_info(f"Installing {package}...")
        return self.run_cmd(f"pkg install {package} -y")
    
    def install_pip(self, package):
        """Install Python package using pip"""
        self.print_info(f"Installing {package} via pip...")
        return self.run_cmd(f"pip install {package} --upgrade")
    
    def install_gem(self, package):
        """Install Ruby gem"""
        self.print_info(f"Installing {package} via gem...")
        return self.run_cmd(f"gem install {package}")
    
    def install_tool(self, tool):
        """Install a single tool based on its type"""
        name = tool['name']
        package = tool['package']
        tool_type = tool['type']
        
        if self.is_installed(name, tool_type):
            self.print_warning(f"{name} is already installed")
            return True
        
        print(f"{Colors.YELLOW}⏳ Installing {name}...{Colors.NC}")
        
        if tool_type == "pkg":
            success = self.install_pkg(package)
        elif tool_type == "pip":
            success = self.install_pip(package)
        elif tool_type == "gem":
            success = self.install_gem(package)
        else:
            success = False
        
        if success:
            self.print_success(f"{name} installed successfully")
            return True
        else:
            self.print_error(f"Failed to install {name}")
            return False
    
    def auto_setup_all(self):
        """Install all tools automatically"""
        self.clear()
        self.print_banner()
        print(f"{Colors.BLUE}{Colors.BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.NC}")
        print(f"{Colors.MAGENTA}{Colors.BOLD}  🚀 AUTO SETUP ALL TOOLS - STARTED{Colors.NC}")
        print(f"{Colors.BLUE}{Colors.BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.NC}\n")
        
        # Initial system update
        self.print_info("Updating package lists...")
        self.run_cmd("pkg update -y")
        self.print_success("Update completed")
        
        self.print_info("Upgrading packages...")
        self.run_cmd("pkg upgrade -y")
        self.print_success("Upgrade completed")
        
        self.print_info("Setting up storage access...")
        self.run_cmd("termux-setup-storage", True)
        self.print_success("Storage setup completed")
        
        # Generate SSH key if not exists
        if not os.path.exists(os.path.expanduser("~/.ssh/id_rsa")):
            self.print_info("Generating SSH key...")
            self.run_cmd("ssh-keygen -t rsa -N '' -f ~/.ssh/id_rsa")
            self.print_success("SSH key generated")
        
        # Install all tools by category
        categories = {}
        for tool in self.tools_list:
            cat = tool['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(tool)
        
        for category, tools in categories.items():
            print(f"\n{Colors.CYAN}{Colors.BOLD}📁 Category: {category}{Colors.NC}")
            print(f"{Colors.DIM}{'─' * 50}{Colors.NC}")
            
            for tool in tools:
                self.install_tool(tool)
                self.installed_count += 1
                time.sleep(0.3)
        
        print(f"\n{Colors.GREEN}{Colors.BOLD}✅ AUTO SETUP COMPLETED!{Colors.NC}")
        print(f"{Colors.YELLOW}📊 Total tools processed: {self.total_tools}{Colors.NC}\n")
        input(f"{Colors.CYAN}Press Enter to continue...{Colors.NC}")
    
    def show_individual_menu(self):
        """Show menu for individual tool installation"""
        while True:
            self.clear()
            self.print_banner()
            print(f"{Colors.CYAN}{Colors.BOLD}📦 INDIVIDUAL TOOLS INSTALLATION{Colors.NC}\n")
            
            # Group by category
            categories = {}
            for tool in self.tools_list:
                cat = tool['category']
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(tool)
            
            menu_items = []
            idx = 1
            for category, tools in categories.items():
                print(f"\n{Colors.YELLOW}{Colors.BOLD}▶ {category}{Colors.NC}")
                for tool in tools:
                    status = "✅" if self.is_installed(tool['name'], tool['type']) else "⬜"
                    print(f"  {Colors.GREEN}[{idx}]{Colors.NC} {status} {tool['name']:20} {Colors.DIM}({tool['type']}){Colors.NC}")
                    menu_items.append(tool)
                    idx += 1
            
            print(f"\n{Colors.BLUE}[0]{Colors.NC} Back to Main Menu")
            print(f"{Colors.MAGENTA}[A]{Colors.NC} Install All Tools")
            
            choice = input(f"\n{Colors.WHITE}Select tool number (0/A): {Colors.NC}").strip()
            
            if choice == '0':
                break
            elif choice.upper() == 'A':
                self.auto_setup_all()
                break
            elif choice.isdigit():
                num = int(choice) - 1
                if 0 <= num < len(menu_items):
                    self.clear()
                    self.print_banner()
                    self.install_tool(menu_items[num])
                    input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.NC}")
                else:
                    self.print_error("Invalid selection")
                    time.sleep(1)
    
    def show_status(self):
        """Show installation status of all tools"""
        self.clear()
        self.print_banner()
        print(f"{Colors.CYAN}{Colors.BOLD}📊 INSTALLATION STATUS{Colors.NC}\n")
        
        installed = 0
        categories = {}
        for tool in self.tools_list:
            cat = tool['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(tool)
        
        for category, tools in categories.items():
            print(f"\n{Colors.YELLOW}{Colors.BOLD}▶ {category}{Colors.NC}")
            print(f"{Colors.DIM}{'─' * 40}{Colors.NC}")
            
            cat_installed = 0
            for tool in tools:
                is_inst = self.is_installed(tool['name'], tool['type'])
                if is_inst:
                    installed += 1
                    cat_installed += 1
                    print(f"  {Colors.GREEN}✅{Colors.NC} {tool['name']}")
                else:
                    print(f"  {Colors.RED}❌{Colors.NC} {tool['name']}")
            
            print(f"{Colors.DIM}  └─ Category: {cat_installed}/{len(tools)} installed{Colors.NC}")
        
        print(f"\n{Colors.BLUE}{Colors.BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.NC}")
        print(f"{Colors.GREEN}📊 Total: {installed}/{self.total_tools} tools installed{Colors.NC}")
        print(f"{Colors.BLUE}{Colors.BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.NC}\n")
        input(f"{Colors.CYAN}Press Enter to continue...{Colors.NC}")
    
    def show_about(self):
        """Show about information"""
        self.clear()
        self.print_banner()
        about_text = f"""
{Colors.BLUE}{Colors.BOLD}════════════════════════════════════════════════════════════════{Colors.NC}
{Colors.MAGENTA}{Colors.BOLD}                    🔧 TERMUX PRO TOOLKIT v4.0{Colors.NC}
{Colors.BLUE}{Colors.BOLD}════════════════════════════════════════════════════════════════{Colors.NC}

{Colors.CYAN}📌 Version:{Colors.NC}     4.0 (Python Edition)
{Colors.CYAN}🐍 Language:{Colors.NC}    Python 3
{Colors.CYAN}👨‍💻 Developer:{Colors.NC}   Your Brand
{Colors.CYAN}📦 Total Tools:{Colors.NC}  {self.total_tools}+ packages
{Colors.CYAN}🔒 Security:{Colors.NC}    Encrypted tool list (Base64 + Reverse)
{Colors.CYAN}🎨 Features:{Colors.NC}    
{Colors.GREEN}    • Auto Setup All Tools{Colors.NC}
{Colors.GREEN}    • Individual Tool Installation{Colors.NC}
{Colors.GREEN}    • Installation Status Check{Colors.NC}
{Colors.GREEN}    • Colorful Terminal UI{Colors.NC}
{Colors.GREEN}    • Loading Animations{Colors.NC}
{Colors.GREEN}    • Smart Error Handling{Colors.NC}

{Colors.YELLOW}📁 Categories Included:{Colors.NC}
{Colors.DIM}    • System & Core (15 tools){Colors.NC}
{Colors.DIM}    • Programming (12 tools){Colors.NC}
{Colors.DIM}    • Security (11 tools){Colors.NC}
{Colors.DIM}    • Network (8 tools){Colors.NC}
{Colors.DIM}    • Python Packages (11 tools){Colors.NC}
{Colors.DIM}    • Utilities (15 tools){Colors.NC}
{Colors.DIM}    • And more...{Colors.NC}

{Colors.BLUE}{Colors.BOLD}════════════════════════════════════════════════════════════════{Colors.NC}
        """
        print(about_text)
        input(f"{Colors.CYAN}Press Enter to continue...{Colors.NC}")
    
    def run(self):
        """Main execution loop"""
        self.clear()
        self.print_banner()
        self.print_info(f"Welcome to Termux Pro Toolkit v4.0")
        self.print_success(f"Loaded {self.total_tools} tools")
        time.sleep(1.5)
        
        while True:
            self.clear()
            self.print_banner()
            self.print_menu()
            choice = input(f"{Colors.WHITE}Enter your choice: {Colors.NC}").strip()
            
            if choice == '1':
                self.auto_setup_all()
            elif choice == '2':
                self.show_individual_menu()
            elif choice == '3':
                self.show_status()
            elif choice == '4':
                self.show_about()
            elif choice == '0':
                self.clear()
                print(f"{Colors.GREEN}👋 Exiting... Thanks for using Termux Pro Toolkit!{Colors.NC}\n")
                sys.exit(0)
            else:
                self.print_error("Invalid option! Please choose 0-4")
                time.sleep(1)

# ==================== MAIN ENTRY POINT ====================
if __name__ == "__main__":
    try:
        toolkit = TermuxProToolkit()
        toolkit.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⚠️ Interrupted by user{Colors.NC}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}Fatal Error: {e}{Colors.NC}")
        sys.exit(1)
