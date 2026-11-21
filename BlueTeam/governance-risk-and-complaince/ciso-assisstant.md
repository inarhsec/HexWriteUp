# Ciso Assisstant



## CISO Assisstance

{% code title="docker-compose.yml" overflow="wrap" %}
```yml
services:
  backend:
    container_name: backend
    image: ghcr.io/intuitem/ciso-assistant-community/backend:latest
    pull_policy: always
    restart: always
    environment:
      - ALLOWED_HOSTS=backend,localhost,ciso-assistant.local
      - CISO_ASSISTANT_URL=https://ciso-assistant.local:8443
      - DJANGO_DEBUG=True
      - AUTH_TOKEN_TTL=7200
      - HOME=/tmp
      - XDG_CACHE_HOME=/tmp/.cache
      - XDG_CONFIG_HOME=/tmp/.config
      - XDG_DATA_HOME=/tmp/.local/share
      - QDRANT_URL=http://qdrant:6333
    read_only: true
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    tmpfs:
      - /tmp:rw,noexec,nosuid,nodev
    volumes:
      - ./db:/code/db
    user: "1001:1001"
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://backend:8000/api/health/ || exit 1"]
      interval: 15s
      timeout: 10s
      retries: 50
      start_period: 300s
  huey:
    container_name: huey
    image: ghcr.io/intuitem/ciso-assistant-community/backend:latest
    pull_policy: always
    depends_on:
      backend:
        condition: service_healthy
    restart: always
    environment:
      - ALLOWED_HOSTS=backend,localhost,ciso-assistant.local
      - CISO_ASSISTANT_URL=https://ciso-assistant.local:8443
      - DJANGO_DEBUG=False
      - AUTH_TOKEN_TTL=7200
      - HOME=/tmp
      - XDG_CACHE_HOME=/tmp/.cache
      - XDG_CONFIG_HOME=/tmp/.config
      - XDG_DATA_HOME=/tmp/.local/share
      - QDRANT_URL=http://qdrant:6333
    read_only: true
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    tmpfs:
      - /tmp:rw,noexec,nosuid,nodev
    volumes:
      - ./db:/code/db
    entrypoint:
      - /bin/sh
      - -c
      - |
        poetry run python manage.py run_huey -w 2 --scheduler-interval 60
    user: "1001:1001"
  frontend:
    container_name: frontend
    environment:
      - PUBLIC_BACKEND_API_URL=http://backend:8000/api
      - PUBLIC_BACKEND_API_EXPOSED_URL=https://ciso-assistant.local:8443/api
      - PROTOCOL_HEADER=x-forwarded-proto
      - HOST_HEADER=x-forwarded-host
      - ORIGIN=https://ciso-assistant.local:8443
      - HOME=/tmp
      - XDG_CACHE_HOME=/tmp/.cache
      - XDG_CONFIG_HOME=/tmp/.config
      - XDG_DATA_HOME=/tmp/.local/share
    image: ghcr.io/intuitem/ciso-assistant-community/frontend:latest
    pull_policy: always
    read_only: true
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    tmpfs:
      - /tmp:rw,noexec,nosuid,nodev
    restart: always
    depends_on:
      backend:
        condition: service_healthy
    user: "1001:1001"
  qdrant:
    container_name: qdrant
    image: qdrant/qdrant:v1.14.0
    restart: unless-stopped
    volumes:
      - qdrant_data:/qdrant/storage
    ports:
      - 6333:6333
  caddy:
    container_name: caddy
    image: caddy:2.11.2
    restart: unless-stopped
    ports:
      - 8443:8443
    volumes:
      - ./db/caddy:/data/caddy
    command: |
      sh -c 'echo "https://ciso-assistant.local:8443 {
      reverse_proxy /api/* backend:8000
      reverse_proxy /* frontend:3000
      tls internal
      }" > Caddyfile && caddy run'
volumes:
  qdrant_data:
```
{% endcode %}



## SOP: Bulk Import Assets into CISO Assistant (Community Edition) via REST API

This SOP is based on your **Docker-based CISO Assistant Community Edition** deployment and is intended for importing assets such as **Netmagic, Yotta, and NextGen** infrastructure.

> **Security:** Do **not** hardcode or share API tokens or session cookies. If a token or cookie has been exposed, **revoke/regenerate it** before use.

***

## 1. Prerequisites

* CISO Assistant Community Edition running
* Valid user account with permission to create assets
* Python 3.10+ installed
* `pandas` and `requests` packages

Install dependencies:

```bash
pip install pandas requests
```

***

## 2. Prepare the Asset CSV

Example:

```
CISO_Assistant_Assets_FIXED.csv
```

{% file src="../.gitbook/assets/CISO_Assistant_Assets_FIXED.csv" %}

{% file src="../.gitbook/assets/asset.py" %}

{% file src="../.gitbook/assets/CISO_Assistant_Import_Clean.xlsx" %}

Columns:

| name       | description | ip       | source\_sheet |
| ---------- | ----------- | -------- | ------------- |
| FSNAS1611  | NAS Server  | 10.x.x.x | Netmagic      |
| FINNTX1125 | App Server  | 10.x.x.x | Yotta         |

The **`name`** field should be unique within the scope.

***

## 3. Authentication Options

### Preferred: API Token

Obtain an API token from your CISO Assistant instance (or generate one through the backend if supported).

Then use:

```python
HEADERS = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}
```

### Alternative: Browser Session (less suitable for automation)

If using your logged-in browser session:

* `sessionid` (HttpOnly cookie)
* `csrftoken`

These can be viewed in the browser's Developer Tools under **Application → Cookies** or **Network**.

A session-based request typically includes:

```python
cookies = {
    "sessionid": SESSION_ID,
    "csrftoken": CSRF_TOKEN,
}

headers = {
    "X-CSRFToken": CSRF_TOKEN,
    "Referer": "https://ciso-assistant.local:8443/",
}
```

> **Do not copy real session IDs or tokens into documentation or source control.**

***

## 4. Python Import Script

```python
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
```

***

## 5. Run the Import

Place the script and CSV in the same directory:

```
C:\Users\<user>\Downloads\
├── asset.py
└── CISO_Assistant_Assets_FIXED.csv
```

Run:

```bash
python asset.py
```

***

## 6. Handling Duplicate Assets

If you receive:

```
400 Bad Request
"<asset name> is already used in this scope."
```

this indicates the asset already exists. It is safe to **skip** these entries.

***

## 7. Verify the Import

In the CISO Assistant UI:

1. Go to **Assets Management → Assets**
2. Search for sample assets such as:
   * `FSNAS1611`
   * `FINNTX1125`
   * `Payment HSM 01`
3. Confirm they are present.

***

## 8. Troubleshooting

| Error                            | Cause                        | Resolution                                                                       |
| -------------------------------- | ---------------------------- | -------------------------------------------------------------------------------- |
| `401 Invalid token`              | Invalid or expired API token | Generate or configure a valid API token                                          |
| `400 already used in this scope` | Asset already exists         | Skip or update the existing asset                                                |
| `SSL warnings`                   | Self-signed certificate      | Use a trusted certificate in production or suppress warnings only in development |
| `404`                            | Incorrect endpoint           | Verify `https://<host>/api/assets/`                                              |

