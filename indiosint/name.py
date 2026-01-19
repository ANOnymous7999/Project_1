from .utils import print_info, print_success, print_error, print_warning, extract_emails, extract_phones, extract_image_urls, safe_search

def lookup_name(name, city=None):
    query_name = f'"{name}"'
    if city:
        query_name += f' AND "{city}"'

    print_info(f"Analyzing name: {name} {'in ' + city if city else ''}")

    # 1. Social Media Search
    print_info("Searching for social media profiles...")
    social_queries = [
        f'site:linkedin.com/in/ {query_name}',
        f'site:facebook.com {query_name}',
        f'site:twitter.com {query_name}',
        f'site:instagram.com {query_name}',
        f'site:github.com {query_name}',
        f'site:pinterest.com {query_name}',
        f'site:quora.com {query_name}',
        f'site:reddit.com {query_name}'
    ]

    social_matches = []
    for q in social_queries:
        results = safe_search(q, num=2)
        if results:
            for res in results:
                print_success(f"Social Media match: {res}")
                social_matches.append(res)

    # 2. Indian News & Public Records
    print_info("Searching for mentions in Indian news and records...")
    news_queries = [
        f'site:timesofindia.indiatimes.com {query_name}',
        f'site:ndtv.com {query_name}',
        f'site:indianexpress.com {query_name}',
        f'site:hindustantimes.com {query_name}',
        f'site:livelaw.in {query_name}',      # Indian legal news
        f'site:barandbench.com {query_name}', # Indian legal news
        f'site:indiankanoon.org {query_name}'  # Indian legal records - VERY IMPORTANT for cyber crime
    ]

    news_matches = []
    for q in news_queries:
        results = safe_search(q, num=2)
        if results:
            for res in results:
                print_success(f"News/Record match: {res}")
                news_matches.append(res)

    # 3. General Search
    print_info("Performing general web search...")
    general_matches = []
    results = safe_search(query_name, num=5)
    if results:
        print_success(f"General matches found:")
        for res in results:
            print(f"  - {res}")
            general_matches.append(res)
    else:
        print_warning("No general matches found.")

    # Extraction from all matches
    all_text = " ".join(social_matches + news_matches + general_matches)
    found_emails = extract_emails(all_text)
    found_phones = extract_phones(all_text)
    found_images = extract_image_urls(all_text)

    if found_emails: print_success(f"Found associated emails: {found_emails}")
    if found_phones: print_success(f"Found associated phones: {found_phones}")

    return {
        "name": name,
        "city": city,
        "social_profiles": social_matches,
        "news_records": news_matches,
        "web_matches": general_matches,
        "associated_emails": found_emails,
        "associated_phones": found_phones,
        "images": found_images
    }
