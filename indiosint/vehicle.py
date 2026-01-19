from .utils import print_info, print_success, print_error, print_warning, safe_search
import re

def lookup_vehicle(query):
    """
    Search for vehicle registration info or challans related to a name or number.
    If query looks like a vehicle number (e.g. MH01AB1234), it searches specifically for it.
    """
    print_info(f"Analyzing vehicle/challan info for: {query}")

    # Check if query is a vehicle number pattern
    is_veh_num = re.match(r'^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$', query.replace(" ", "").upper())

    queries = []
    if is_veh_num:
        vnum = query.replace(" ", "").upper()
        queries = [
            f'"{vnum}" challan',
            f'"{vnum}" vehicle details',
            f'site:parivahan.gov.in "{vnum}"',
            f'site:echallan.tspolice.gov.in "{vnum}"',
            f'"{vnum}" owner'
        ]
    else:
        # Searching for vehicle info by name
        queries = [
            f'"{query}" vehicle number',
            f'"{query}" registration details',
            f'"{query}" RC status'
        ]

    found_info = []
    for q in queries:
        found_info.extend(safe_search(q, num=3))

    if found_info:
        print_success(f"Potential vehicle/challan records found:")
        for res in set(found_info):
            print(f"  - {res}")
    else:
        print_warning("No public vehicle or challan records found.")

    return {
        "query": query,
        "records": list(set(found_info))
    }
