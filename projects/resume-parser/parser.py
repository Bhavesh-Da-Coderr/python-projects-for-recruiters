import re
import docx2txt
import pdfplumber
import os
import glob

def extract_text(file_path: str) -> str:
    """Extracts text from PDF or DOCX files."""
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
    """Extracts emails, phones, LinkedIn, and URLs."""
    results = {
        "emails": re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text),
        "phones": re.findall(r"\+?\d[\d\s().-]{7,}\d", text),
        "linkedin": re.findall(r"(https?://[a-z]{2,3}\.linkedin\.com/[^\s]+)", text),
        "urls": re.findall(r"(https?://[^\s]+)", text),
    }
    return results

def resolve_file_path(path: str) -> str:
    """If folder is given, pick the first .docx or .pdf inside."""
    if os.path.isdir(path):
        files = glob.glob(os.path.join(path, "*.docx")) + glob.glob(os.path.join(path, "*.pdf"))
        if not files:
            raise FileNotFoundError(f"No .docx or .pdf file found in folder: {path}")
        return files[0]  # pick the first file
    return path

if __name__ == "__main__":
    file_path = input("Enter resume file path (.pdf/.docx or folder): ").strip('"')
    file_path = resolve_file_path(file_path)

    text = extract_text(file_path)
    if not text.strip():
        print("[!] No text could be extracted. Check if the file is scanned (OCR may be needed).")
        exit(1)

    print("\n----- Extracted Text Sample -----")
    print(text[:600], "...\n")  # first 600 chars
    print("--------------------------------")

    contacts = extract_contacts(text)
    print("\n===== Extracted Contacts =====")
    print("Emails   :", contacts["emails"])
    print("Phones   :", contacts["phones"])
    print("LinkedIn :", contacts["linkedin"])
    print("Other URLs:", contacts["urls"])
