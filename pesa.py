import requests
import zipfile
import io
import os

# Link to the sandbox file (manually copy from your browser session)
url = "https://copilot.microsoft.com/sandbox/data/ClickPesa_API_Documentation.zip"  # Replace with working URL if needed

# Output directory (relative or absolute path)
output_dir = "clickpesa_docs"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

try:
    print("Downloading a ZIP file...")
    response = requests.get(url)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        zip_ref.extractall(output_dir)
        print(f"✅ Done! Files are extracted to '{output_dir}'")

except Exception as e:
    print("❌ Error:", e)
    print("Just testing git rebase conflicts and changes.")
