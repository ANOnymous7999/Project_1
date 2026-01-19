import argparse
import sys
from indiosint.utils import print_banner, print_info, print_error
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

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.phone:
        lookup_phone(args.phone)

    if args.email:
        lookup_email(args.email)

    if args.name:
        lookup_name(args.name, args.city)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print_error(f"An unexpected error occurred: {e}")
