# File: scanner.py

import requests
from typing import List

def search_cves(device_name: str, model: str = "") -> List[str]:
    query = f"{device_name} {model}".strip()
    url = f"https://cve.circl.lu/api/search/{query}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        cves = [item['id'] for item in data.get('data', []) if 'id' in item]
        return cves[:10]
    except Exception:
        return []
