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

def print_result(label, value, color=Fore.CYAN):
    print(f"{color}[{label.upper()}]{Style.RESET_ALL} {value}")

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

def safe_search(query, num=10):
    """A wrapper for google search with better error handling."""
    from googlesearch import search
    try:
        return list(search(query, num_results=num))
    except Exception as e:
        if "429" in str(e):
            print_error("Google Rate Limit hit (429). Try again later or use a VPN.")
        elif "Timeout" in str(e) or "HTTPSConnectionPool" in str(e):
            print_error("Connection timeout. Please check your internet or try a VPN.")
        else:
            print_error(f"Search failed: {e}")
        return []

def extract_emails(text):
    """Extract emails from a block of text."""
    return list(set(re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', text.lower())))

def extract_phones(text):
    """Extract Indian phone numbers from a block of text."""
    # Matches +91, 91, or just 10 digit numbers
    patterns = [
        r'\+91[6-9]\d{9}',
        r'91[6-9]\d{9}',
        r'\b[6-9]\d{9}\b'
    ]
    results = []
    for p in patterns:
        results.extend(re.findall(p, text))
    return list(set(results))

def extract_image_urls(text):
    """Simple extraction of image-like URLs."""
    return re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\.(?:jpg|jpeg|png|gif|webp)', text)
