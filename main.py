import argparse
import sys
from indiosint.utils import print_banner, print_info, print_error, print_success, extract_potential_name
from indiosint.phone import lookup_phone
from indiosint.email import lookup_email
from indiosint.name import lookup_name

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="IndiOSINT: Indian Cyber Crime Investigation OSINT Tool")
    parser.add_argument("-p", "--phone", help="Phone number to investigate (e.g., +91XXXXXXXXXX)")
    parser.add_argument("-e", "--email", help="Email address to investigate")
    parser.add_argument("-n", "--name", help="Name to investigate")
    parser.add_argument("-c", "--city", help="City (optional, used with name search)")
    parser.add_argument("-s", "--smart", action="store_true", help="Enable smart mode (auto-connect clues)")
    parser.add_argument("-o", "--output", help="Output file to save results (JSON)")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    results = {}
    found_names = set()
    if args.name: found_names.add(args.name)

    # 1. Phone Investigation
    if args.phone:
        results['phone'] = lookup_phone(args.phone)

    # 2. Email Investigation
    if args.email:
        results['email'] = lookup_email(args.email)
        if results['email'] and results['email'].get('social_profiles'):
            for platform, url in results['email']['social_profiles']:
                p_name = extract_potential_name(url)
                if p_name: found_names.add(p_name)

    # 3. Name Investigation (including found names if smart mode is on)
    if args.name:
        results['name'] = lookup_name(args.name, args.city)

    if args.smart and found_names:
        for name in found_names:
            if name != args.name:
                print_success(f"Smart Mode: Automatically investigating discovered name: {name}")
                results[f'name_{name}'] = lookup_name(name, args.city)

    # Summary
    print("\n" + "="*50)
    print_info("Investigation Complete. Victim Profile Summary:")
    print("="*50)
    for target_type, data in results.items():
        if data:
            if target_type == 'phone':
                print(f"{Fore.CYAN}[PHONE]{Style.RESET_ALL} {data.get('phone')} | {data.get('location')} | {data.get('carrier')}")
                if data.get('leaks'): print(f"  {Fore.RED}[!] Leaks found: {len(data['leaks'])}{Style.RESET_ALL}")
            elif 'email' in target_type:
                print(f"{Fore.CYAN}[EMAIL]{Style.RESET_ALL} {data.get('email')}")
                if data.get('social_profiles'): print(f"  - Profiles: {len(data['social_profiles'])}")
                if data.get('leaks'): print(f"  {Fore.RED}[!] Leaks found: {len(data['leaks'])}{Style.RESET_ALL}")
            elif 'name' in target_type:
                print(f"{Fore.CYAN}[NAME]{Style.RESET_ALL} {data.get('name')}")
                if data.get('news_records'): print(f"  - News/Legal matches: {len(data['news_records'])}")
                if data.get('social_profiles'): print(f"  - Social profiles: {len(data['social_profiles'])}")

    if args.output:
        import json
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=4)
        print_success(f"Results saved to {args.output}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print_error(f"An unexpected error occurred: {e}")
