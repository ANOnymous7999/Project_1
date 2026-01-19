import sys
import re
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

def extract_potential_name(url):
    """Try to extract a name or username from a social media URL."""
    parts = url.split('/')
    if 'linkedin.com' in url and 'in/' in url:
        # linkedin.com/in/first-last-12345
        idx = parts.index('in')
        if len(parts) > idx + 1:
            name_part = parts[idx+1]
            return name_part.split('-')[0].capitalize() + " " + name_part.split('-')[1].capitalize() if '-' in name_part else name_part
    elif 'twitter.com' in url or 'x.com' in url or 'instagram.com' in url or 'github.com' in url:
        if len(parts) > 3:
            return parts[3]
    return None

def extract_emails(text):
    """Extract emails from a block of text."""
    return re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', text.lower())
