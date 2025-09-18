import os
import subprocess

def clear_screen():
    """Clears terminal screen for better UX."""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_project(script_path):
    """Runs a Python script."""
    if os.path.exists(script_path):
        subprocess.run(["python", script_path], check=True)
    else:
        print(f"[!] Script not found: {script_path}")

def main():
    projects = {
        "1": {"name": "Smart Resume Parser", "path": "projects/resume-parser/parser.py"},
        "2": {"name": "Personal Finance Tracker", "path": "projects/personal-finance/main.py"},
        "3": {"name": "AI Chatbot with Memory", "path": "projects/chatbot/chatbot.py"},
        "4": {"name": "Job Scraper & Analyzer", "path": "projects/job-scraper/analyze.py"},
        "5": {"name": "Stock Price Predictor", "path": "projects/stock-predictor/predictor.py"},
        "0": {"name": "Exit", "path": None}
    }

    while True:
        clear_screen()
        print("=== Python Projects for Recruiters ===\n")
        for key, proj in projects.items():
            print(f"[{key}] {proj['name']}")
        choice = input("\nSelect a project to run: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice in projects:
            print(f"\nRunning {projects[choice]['name']}...\n")
            run_project(projects[choice]["path"])
            input("\nPress Enter to return to main menu...")
        else:
            print("[!] Invalid choice. Try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
