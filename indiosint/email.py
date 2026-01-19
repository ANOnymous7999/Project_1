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
        "Pinterest": f"site:pinterest.com \"{email}\"",
        "Quora": f"site:quora.com \"{email}\"",
        "Reddit": f"site:reddit.com \"{email}\"",
        "Flickr": f"site:flickr.com \"{email}\"",
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

    # Breach/Leak Search
    print_info(f"Checking for potential leaks/breaches related to {email}...")
    leak_queries = [
        f'site:pastebin.com "{email}"',
        f'site:ghostbin.com "{email}"',
        f'site:leaked.site "{email}"',
        f'site:breachforums.is "{email}"',
        f'"{email}" leak',
        f'"{email}" database'
    ]

    found_leaks = []
    for q in leak_queries:
        try:
            for res in search(q, num_results=2):
                found_leaks.append(res)
        except Exception:
            pass

    if found_leaks:
        print_success(f"Potential leak mentions found:")
        for res in set(found_leaks):
            print(f"  - [LEAK MENTION] {res}")
    else:
        print_warning("No public leak mentions found in common paste sites.")

    return {
        "email": email,
        "social_profiles": found_profiles,
        "leaks": found_leaks,
        "web_matches": general_results
    }
