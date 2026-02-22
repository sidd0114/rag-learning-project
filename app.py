import fitz
import re
import json

pdf_file = "Simple_Data_Parsing_and_Document_Structure.pdf"
document = fitz.open(pdf_file)

structured_data = []
current_section = "General"

for page in document:
    text = page.get_text()
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        # Detect ALL CAPS headings
        if line.isupper() and len(line) > 3:
            current_section = line

        # Detect numbered headings like 1, 1.1, 2.3.4
        elif re.match(r"^\d+(\.\d+)*", line):
            current_section = line

        elif line:
            structured_data.append({
                "section": current_section,
                "content": line
            })

with open("structured_output.json", "w") as f:
    json.dump(structured_data, f, indent=4)

print("Improved PDF parsing completed!")