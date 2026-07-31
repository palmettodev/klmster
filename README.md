# klmster
SSN Detector for directories
During a recent audit, we found that several files are on the desktop, unsecured, including SSN's.  These files are accessible to many users.

Version 1 focuses on identifying potential U.S. Social Security numbers in common document formats. Future versions may add support for additional PII such as driver's license numbers, passport numbers, and credit card numbers.

## Usage

python scanner.py /home/user/Documents

## Why this tool

Organizations frequently store documents containing U.S. Social Security numbers in shared folders. This utility helps identify files that may contain unprotected SSNs so they can be reviewed and secured.
