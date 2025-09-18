import re
import docx2txt
import pdfplumber
import os

def extract_text(file_path: str) -> str:
    """
    Extracts raw text from PDF or DOCX files.
    Supports .pdf and .docx formats.
    """
    text = ""
    if file_path.lower().endswith(".pdf"):
        try:
            with pdfplumber.open(file_path) as pdf:
                text = "".join(page.extract_text() or "" for page in pdf.pages)
        except Exception as e:
            print(f"[!] PDF extraction failed: {e}")
    elif file_path.lower().endswith(".docx"):
        try:
            text = docx2txt.process(file_path)
        except Exception as e:
            print(f"[!] DOCX extraction failed: {e}")
    else:
        raise ValueError("Unsupported file format. Use .pdf or .docx")
    return text


def extract_contacts(text: str):
    """
    Extracts emails, phone numbers, LinkedIn profiles, and other URLs from raw text.
    Returns a dictionary with results.
    """
    results = {
        "emails": [],
        "phones": [],
        "linkedin": [],
        "urls": []
    }

    # Email regex
    results["emails"] = re.findall(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text
    )

    # Phone regex (handles +91, (), spaces, -, etc.)
    results["phones"] = re.findall(
        r"\+?\d[\d\s().-]{7,}\d", text
    )

    # LinkedIn regex
    results["linkedin"] = re.findall(
        r"(https?://[a-z]{2,3}\.linkedin\.com/[^\s]+)", text
    )

    # General URL regex
    results["urls"] = re.findall(
        r"(https?://[^\s]+)", text
    )

    return results


if __name__ == "__main__":
    file_path = input("Enter resume file path (.pdf/.docx): ").strip('"')

    if not os.path.exists(file_path):
        print(f"[!] File not found: {file_path}")
        exit(1)

    text = extract_text(file_path)

    if not text.strip():
        print("[!] No text could be extracted. Check if the file is scanned (OCR may be needed).")
        exit(1)

    print("\n----- Extracted Text Sample -----")
    print(text[:600], "...\n")  # show only first 600 chars
    print("--------------------------------")

    contacts = extract_contacts(text)

    print("\n===== Extracted Contacts =====")
    print("Emails   :", contacts["emails"])
    print("Phones   :", contacts["phones"])
    print("LinkedIn :", contacts["linkedin"])
    print("Other URLs:", contacts["urls"])
