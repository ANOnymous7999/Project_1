import sys
from colorama import Fore, Style, init

init(autoreset=True)

def print_info(message):
    print(f"{Fore.BLUE}[*] {message}{Style.RESET_ALL}")

def print_success(message):
    print(f"{Fore.GREEN}[+] {message}{Style.RESET_ALL}")

def print_error(message):
    print(f"{Fore.RED}[!] {message}{Style.RESET_ALL}")

def print_warning(message):
    print(f"{Fore.YELLOW}[!] {message}{Style.RESET_ALL}")

def print_banner():
    banner = rf"""{Fore.CYAN}
  _____           _ _  ____   _____ _____ _   _ _______
 |_   _|         | (_)/ __ \ / ____|_   _| \ | |__   __|
   | |  _ __   __| |_| |  | | (___   | | |  \| |  | |
   | | | '_ \ / _` | | |  | |\___ \  | | | . ` |  | |
  _| |_| | | | (_| | | |__| |____) |_| |_| |\  |  | |
 |_____|_| |_|\__,_|_|\____/|_____/|_____|_| \_|  |_|

    Indian Cyber Crime Investigation OSINT Tool
    """
    print(banner)
