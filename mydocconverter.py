import re
import os


def find_and_replace_in_md(file_path, replacements):
    """
    Perform find and replace operations in a Markdown file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    for find_text, replace_text in replacements.items():
        # Only apply once per pattern safely
        content = re.sub(find_text, replace_text, content, flags=re.MULTILINE)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"✅ Processed: {file_path}")


def process_directory(directory_path, replacements):
    """
    Recursively find all .md files in a directory and apply replacements.
    """
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                find_and_replace_in_md(file_path, replacements)


if __name__ == "__main__":
    directory = "output_1"  # Change this to your folder path, e.g. "./reports/"

    replacements = {
        r"(?m)^##\s*August 2025": r"August 2025",
        r"(?m)^#\s*Fund Managers' Report": r"Fund Managers' Report",
        r"(?m)^###\s*Asset Allocation \(as % of Total Assets\)": r"## Asset Allocation (as % of Total Assets)",
        r"(?m)^###\s*Fund Statistics": r"## Fund Statistics",
        r"(?m)^###\s*Asset Allocation \(Sector Wise as a % of Total Assets\)": r"## Asset Allocation (Sector Wise as a % of Total Assets)",
        r"(?m)^###\s*Top 10 Holdings \(% of Total Assets\)": r"## Top 10 Holdings (% of Total Assets)",
        r"(?m)^###\s*Monthly Returns": r"## Monthly Returns",
        r"(?m)^###\s*Dispute Resolution/Complaint Handling": r"## Dispute Resolution/Complaint Handling",
        r"(?m)^###\s*Disclaimer": r"## Disclaimer",
        r"(?m)^###\s*Total Expense Ratio Break up": r"## Total Expense Ratio Break up",
        r"(?m)^###\s*Fund:\s*Not Yet Rated": r"Fund: Not Yet Rated",
        r"(?m)^###\s*AMC Rating:.*VIS.*": r"AMC Rating: \"AM1\" by VIS 02-Jan-25",
        r"(?m)^###\s*AMC Rating:.*PACRA.*": r"AMC Rating: \"AM1\" by PACRA 29-August-25",
        r"(?m)^#\s*Alfalah Asset Management Limited Fund Managers' Report": r"Alfalah Asset Management Limited Fund Managers' Report",
        r"(?m)^##\s*Economic &#x26; Capital Markets Review": r"Economic &#x26; Capital Markets Review",
        r"(?m)^###\s*Economic Review &#x26; Outlook": r"Economic Review &#x26; Outlook",
        r"&#x26;": "&",
        r"(?m)^#\s+Investment Objective": "## Investment Objective",
        r"(?m)^#\s+Basic Information": "## Basic Information",
        r"(?m)^#\s+Fund Performance": "## Fund Performance",
        r"(?m)^#\s+Credit Quality \(as % of Total Assets\)": "## Credit Quality (as % of Total Assets)",
        r"(?m)^#\s+Monthly Returns": "## Monthly Returns",
        r"(?m)^#\s+Dispute Resolution/Complaint Handling": "## Dispute Resolution/Complaint Handling",
        r"(?m)^#\s+Disclaimer": "## Disclaimer",
        r"(?m)^#\s+Total Expense Ratio": "## Total Expense Ratio",
        r"(?m)^#\s+Fund Statistics": "## Fund Statistics",
        r"(?m)^#\s+Investment Committee": "## Investment Committee",
        r"(?m)^#\s+TFC/Sukuk Holdings \(% of Total Assets\)": "## TFC/Sukuk Holdings (% of Total Assets)",
        r"(?m)^#\s+Top 10 Holdings \(% of Total Assets\)": "## Top 10 Holdings (% of Total Assets)",
        r"Investment Plans Summary Report for September 2025": "# Investment Plans Summary Report for September 2025",
        r"(?m)^#\s+Economic Review & Outlook": "## Economic Review & Outlook",
        r"(?m)^#\s+Money Market Review & Outlook": "## Money Market Review & Outlook",
        r"(?m)^#\s+Equity Market Review & Outlook": "## Equity Market Review & Outlook",
    }

    process_directory(directory, replacements)
