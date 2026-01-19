# IndiOSINT

IndiOSINT is an Open Source Intelligence (OSINT) tool specifically designed for Indian cyber crime investigation. It helps investigators find information related to names, emails, and phone numbers by leveraging various search techniques and Indian-specific sources.

## Features

- **Phone Intelligence**: Basic info, web search, and cross-linking to emails/images.
- **Email Intelligence**: Social media discovery, leak detection, and associated phone number extraction.
- **Smart Chaining**: Automatically investigates discovered identifiers (names, emails) from search results.
- **Deep Scraping**: Extracts additional metadata and images from discovered social media profiles.
- **Vehicle Intelligence**: Searches for Indian vehicle registration details and traffic challans.
- **Intelligence Engine**: Uses a weighted scoring model to cross-verify and validate connected data.
- **Indian Focus**: Optimized for Indian phone formats, news, and legal databases.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py -h
```

### Examples

- **Phone Search**:
  ```bash
  python main.py -p +919xxxxxxxxx
  ```

- **Email Search**:
  ```bash
  python main.py -e example@domain.com
  ```

- **Name Search**:
  ```bash
  python main.py -n "John Doe" -c "Mumbai"
  ```

- **Vehicle Search**:
  ```bash
  python main.py -v "MH01AB1234"
  ```

- **Smart Mode with Intelligence Validation**:
  ```bash
  python main.py -e victim@example.com -s -o investigation_report.json
  ```

- **Update the tool**:
  ```bash
  python main.py --update
  ```

## Disclaimer

This tool is for educational and investigative purposes only. Always respect privacy and follow legal guidelines when performing OSINT.
