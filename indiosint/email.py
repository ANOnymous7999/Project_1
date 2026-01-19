from googlesearch import search
from .utils import print_info, print_success, print_error, print_warning
import requests

def lookup_email(email):
    print_info(f"Analyzing email: {email}")

    # Check common social media platforms via search
    platforms = {
        "LinkedIn": f"site:linkedin.com/in/ \"{email}\"",
        "Twitter": f"site:twitter.com \"{email}\"",
        "Facebook": f"site:facebook.com \"{email}\"",
        "Instagram": f"site:instagram.com \"{email}\"",
        "GitHub": f"site:github.com \"{email}\"",
    }

    print_info(f"Searching for {email} across social media...")
    found_profiles = []

    for platform, query in platforms.items():
        try:
            for res in search(query, num_results=2):
                found_profiles.append((platform, res))
        except Exception as e:
            print_error(f"Error searching {platform}: {e}")

    if found_profiles:
        print_success(f"Potential social media profiles found:")
        for platform, link in found_profiles:
            print(f"  - [{platform}] {link}")
    else:
        print_warning("No social media profiles found via direct email search.")

    # General search
    print_info(f"Performing general web search for {email}...")
    try:
        general_results = []
        for res in search(f'"{email}"', num_results=5):
            general_results.append(res)

        if general_results:
            print_success(f"Found {len(general_results)} potential web matches:")
            for res in general_results:
                print(f"  - {res}")
        else:
            print_warning("No general web matches found.")
    except Exception as e:
        print_error(f"General search failed: {e}")

    # Mentioning Breach checking
    print_info("Note: For deep breach analysis, consider using HaveIBeenPwned or DeHashed (requires API keys).")
