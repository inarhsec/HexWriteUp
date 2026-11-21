import pandas as pd
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ======================================================
# CONFIGURATION
# ======================================================
API_URL = "https://ciso-assistant.local:8443/api/assets/"
TOKEN = "9aa762e19cd191c97a8b483a9c7edb972c27c79854c99d9b4d0aa5e6c5ccfd89"

FOLDER_ID = "53265023-d86a-42a4-b38d-d9c6d439e794"  # Finacus Solution

EXCEL_FILE = "CISO_Assistant_Import_Clean.xlsx"
# or:
# EXCEL_FILE = "CISO_Assistant_Import_Clean.csv"

HEADERS = {
    "Authorization": f"Token {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# ======================================================
# LOAD FILE
# ======================================================
if EXCEL_FILE.lower().endswith(".xlsx"):
    df = pd.read_excel(EXCEL_FILE)
else:
    df = pd.read_csv(EXCEL_FILE)

df.columns = [str(c).strip().lower() for c in df.columns]

print(f"Loaded {len(df)} rows")

success = 0
skip = 0
fail = 0

for _, row in df.iterrows():

    # ----- Name -----
    name = str(row.get("name", "")).strip()

    if (
        not name
        or name.lower() in ("nan", "none")
        or "\n" in name
        or "dtype: object" in name.lower()
    ):
        skip += 1
        continue

    # Skip numeric-only names
    try:
        float(name)
        skip += 1
        continue
    except Exception:
        pass

    # ----- Description -----
    description = ""
    if "description" in df.columns:
        value = row.get("description")
        if pd.notna(value):
            description = str(value).strip()

    payload = {
        "name": name[:200],
        "description": description[:1000],
        "folder": FOLDER_ID,
        "type": "SP"
    }

    try:
        r = requests.post(
            API_URL,
            headers=HEADERS,
            json=payload,
            verify=False,
            timeout=30,
        )

        if r.status_code in (200, 201):
            print(f"[OK] {name}")
            success += 1

        elif (
            r.status_code == 400
            and "already used in this scope" in r.text
        ):
            print(f"[SKIP] {name} already exists")
            skip += 1

        else:
            print(f"[FAIL] {name}")
            print(r.status_code)
            print(r.text)
            fail += 1

    except Exception as e:
        print(f"[ERROR] {name}: {e}")
        fail += 1

print("\n==============================")
print("Imported :", success)
print("Skipped  :", skip)
print("Failed   :", fail)
print("==============================")