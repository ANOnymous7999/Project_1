from googlesearch import search
from .utils import print_info, print_success, print_error, print_warning

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
        try:
            results = list(search(q, num_results=2))
            if results:
                for res in results:
                    print_success(f"Social Media match: {res}")
                    social_matches.append(res)
        except Exception as e:
             print_error(f"Search failed for query {q}: {e}")

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
        try:
            results = list(search(q, num_results=2))
            if results:
                for res in results:
                    print_success(f"News/Record match: {res}")
                    news_matches.append(res)
        except Exception as e:
            print_error(f"Search failed for query {q}: {e}")

    # 3. General Search
    print_info("Performing general web search...")
    general_matches = []
    try:
        results = list(search(query_name, num_results=5))
        if results:
            print_success(f"General matches found:")
            for res in results:
                print(f"  - {res}")
                general_matches.append(res)
        else:
            print_warning("No general matches found.")
    except Exception as e:
        print_error(f"General search failed: {e}")

    return {
        "name": name,
        "city": city,
        "social_profiles": social_matches,
        "news_records": news_matches,
        "web_matches": general_matches
    }
