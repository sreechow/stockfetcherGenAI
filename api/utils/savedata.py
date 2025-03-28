
import re
import json

def save_to_json(text):
    # Step 1: Decode escaped newlines
    clean_text = text.replace('\\n', '\n')

    # Step 2: Split into entries using regex (by "1.", "2." etc.)
    entries = re.split(r'\n\d+\.\s', clean_text)
   

    # Step 3: Extract structured data
    results = []
    for entry in entries:
        if not entry.strip():
            continue

        name_match = re.search(r'\*\*(.*?)\*\*', entry)
        projection_match = re.search(r'\*\*.*?\*\*:\s*(.*?)(?:\s*\(\[)', entry)
        url_match = re.search(r'\((https?://[^\)]+)\)', entry)

        name = name_match.group(1).strip() if name_match else ""
        projection = projection_match.group(1).strip() if projection_match else ""
        link = url_match.group(1).strip() if url_match else ""

        if not (name or projection or link):
            continue

        results.append({
            "Company Name": name,
            "Projection": projection,
            "Link": link
        })

    # Step 4: Write to JSON file
    with open("company_projections.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print('successfully stored the data to company_projections.json')

#text = """Based on recent analyses, here are some NASDAQ-listed healthcare companies with notable projected revenue growth:\n\n1. **Veracyte, Inc. (VCYT)**: Specializes in genomic diagnostics, with a projected earnings growth of 137.3% year-over-year. ([nasdaq.com](https://www.nasdaq.com/articles/your-portfolio-missing-these-5-high-growth-healthcare-stocks?utm_source=openai))\n\n2. **Globus Medical, Inc. (GMED)**: Focuses on musculoskeletal solutions, anticipating a 28% year-over-year earnings growth. ([nasdaq.com](https://www.nasdaq.com/articles/your-portfolio-missing-these-5-high-growth-healthcare-stocks?utm_source=openai))\n\n3. **Encompass Health Corporation (EHC)**: Provides post-acute healthcare services, with a projected 17.6% year-over-year earnings growth. ([nasdaq.com](https://www.nasdaq.com/articles/your-portfolio-missing-these-5-high-growth-healthcare-stocks?utm_source=openai))\n\n4."""
#save_to_csv(text)