import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from googlesearch import search
from .utils import print_info, print_success, print_error, print_warning

def lookup_phone(phone_number):
    print_info(f"Analyzing phone number: {phone_number}")
    try:
        # If no plus sign, assume Indian number (+91)
        if not phone_number.startswith('+'):
            if len(phone_number) == 10:
                phone_number = '+91' + phone_number
                print_info(f"Assuming Indian number: {phone_number}")
            else:
                print_error("Invalid phone number format. Use international format (e.g., +91XXXXXXXXXX)")
                return

        parsed_number = phonenumbers.parse(phone_number)

        if not phonenumbers.is_valid_number(parsed_number):
            print_error("Invalid phone number.")
            return

        # Basic Info
        region = geocoder.description_for_number(parsed_number, "en")
        operator = carrier.name_for_number(parsed_number, "en")
        zones = timezone.time_zones_for_number(parsed_number)

        print_success(f"Location: {region}")
        print_success(f"Carrier: {operator if operator else 'Unknown'}")
        print_success(f"Timezones: {', '.join(zones)}")

        # Web Search
        print_info(f"Searching for {phone_number} on the web...")
        search_query = f'"{phone_number}" OR "{phone_number[1:]}"'
        results = []
        try:
            for res in search(search_query, num_results=10):
                results.append(res)
        except Exception as e:
            print_error(f"Search failed: {e}")

        if results:
            print_success(f"Found {len(results)} potential web matches:")
            for res in results:
                print(f"  - {res}")
        else:
            print_warning("No direct web matches found for the phone number.")

        # Leak search for phone
        print_info(f"Checking for potential leaks related to phone: {phone_number}")
        leak_results = []
        try:
            for res in search(f'"{phone_number}" leak OR "{phone_number}" database', num_results=3):
                leak_results.append(res)
        except:
            pass

        if leak_results:
            print_success(f"Found potential leak mentions for phone:")
            for res in leak_results:
                print(f"  - {res}")

        return {
            "phone": phone_number,
            "location": region,
            "carrier": operator,
            "web_matches": results,
            "leaks": leak_results
        }

    except Exception as e:
        print_error(f"Error during phone lookup: {e}")
        return None
