from .utils import print_info, print_success, print_error, print_warning, extract_phones, extract_image_urls, safe_search
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
        results = safe_search(query, num=2)
        for res in results:
            found_profiles.append((platform, res))

    if found_profiles:
        print_success(f"Potential social media profiles found:")
        for platform, link in found_profiles:
            print(f"  - [{platform}] {link}")
    else:
        print_warning("No social media profiles found via direct email search.")

    # General search
    print_info(f"Performing general web search for {email}...")
    general_results = safe_search(f'"{email}"', num=5)

    if general_results:
        print_success(f"Found {len(general_results)} potential web matches:")
        for res in general_results:
            print(f"  - {res}")
    else:
        print_warning("No general web matches found.")

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
        found_leaks.extend(safe_search(q, num=2))

    if found_leaks:
        print_success(f"Potential leak mentions found:")
        for res in set(found_leaks):
            print(f"  - [LEAK MENTION] {res}")
    else:
        print_warning("No public leak mentions found in common paste sites.")

    # Cross-linking: Search for phone with email
    print_info(f"Searching for phone numbers associated with {email}...")
    associated_phones = []
    found_images = []
    search_res = safe_search(f'"{email}" "91" OR "{email}" "+91"', num=5)
    for res in search_res:
        associated_phones.extend(extract_phones(res))
        found_images.extend(extract_image_urls(res))

    if associated_phones:
        print_success(f"Potential associated phones found: {list(set(associated_phones))}")

    return {
        "email": email,
        "social_profiles": found_profiles,
        "leaks": found_leaks,
        "web_matches": general_results,
        "associated_phones": list(set(associated_phones)),
        "images": list(set(found_images))
    }
