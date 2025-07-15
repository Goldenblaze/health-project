from getpass import getpass  # Hides typed API key

print("MEDICAL ASSISTANT SETUP")
google_key = getpass("Paste your Google API key (hidden typing): ")

with open(".env", "w") as f:
    f.write(f"GOOGLE_API_KEY={google_key}\n")

print("✅ .env file created! Never share this file.")

