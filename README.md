# klmster
SSN Detector for directories.

During a recent audit, we found that several files are on the desktop, unsecured, including SSN's.  These files are accessible to many users.

Version 1 focuses on identifying potential U.S. Social Security numbers in common document formats. Future versions may add support for additional PII such as driver's license numbers, passport numbers, and credit card numbers.

## Usage

python scanner.py /home/user/Documents

## Why this tool

Organizations frequently store documents containing U.S. Social Security numbers in shared folders. This utility helps identify files that may contain unprotected SSNs so they can be reviewed and secured.

## Features

- Scan .txt files
- Scan .docx files
- Recursive directory scanning
- Detect SSNs in the formats:
  - XXX-XX-XXXX
  - XXXXXXXXX
- Cross-platform (Linux, Windows, macOS)

## Requirements

- Python 3.10+
- pip

## Installation

```bash
git clone https://github.com/palmettodev/klmster.git
cd ssn-finder

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Usage

```bash
python scanner.py test_files
```

## Example Output

```
Scanning test_files...

Found:
test_files/ssn.docx

Potential SSN:
***-**-4321

Scan complete.
```
