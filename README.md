# IndiOSINT

IndiOSINT is an Open Source Intelligence (OSINT) tool specifically designed for Indian cyber crime investigation. It helps investigators find information related to names, emails, and phone numbers by leveraging various search techniques and Indian-specific sources.

## Features

- **Phone Intelligence**: Basic info (carrier, region) and web search for Indian phone numbers.
- **Email Intelligence**: Social media profile discovery and general web search.
- **Name Search**: Targeted searching across Indian news outlets, legal databases (`IndianKanoon`, `LiveLaw`), and social media.
- **Indian Focus**: Automatically handles Indian phone formatting and prioritizes Indian sources.

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
  python main.py -p +919876543210
  ```

- **Email Search**:
  ```bash
  python main.py -e example@domain.com
  ```

- **Name Search**:
  ```bash
  python main.py -n "John Doe" -c "Mumbai"
  ```

## Disclaimer

This tool is for educational and investigative purposes only. Always respect privacy and follow legal guidelines when performing OSINT.
