import os
import re
from docx import Document


SSN_REGEX = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")


def get_files(directory):
    """Return all .txt and .docx files."""
    files = []

    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith((".txt", ".docx")):
                files.append(os.path.join(root, filename))

    return files


def read_txt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()


def read_docx(path):
    doc = Document(path)

    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)


def scan_text(text):
    return SSN_REGEX.findall(text)


def scan_file(path):

    if path.endswith(".txt"):
        text = read_txt(path)

    elif path.endswith(".docx"):
        text = read_docx(path)

    else:
        return []

    return scan_text(text)


def main():

    directory = input("Directory to scan: ").strip()

    print(f"\nScanning {directory}\n")

    files = get_files(directory)

    findings = 0

    for file in files:

        matches = scan_file(file)

        if matches:

            findings += len(matches)

            print("=" * 50)
            print(file)

            for ssn in matches:
                print(f"Potential SSN: {ssn}")

    print("\nFinished.")

    print(f"Files scanned: {len(files)}")
    print(f"Matches found: {findings}")


if __name__ == "__main__":
    main()
