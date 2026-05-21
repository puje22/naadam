import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE = "https://www.devjee.mn"

def get_state_naadams():
    url = f"{BASE}/t"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    events = []

    # All Naadam links
    links = soup.select("a.text-blue-600")

    for link in links:
        title = link.text.strip()

        # Filter: only STATE Naadam
        if "Үндэсний их баяр наадам" not in title:
            continue

        href = link["href"]

        # Strip /round/... to get base event URL
        base = href.split("/round")[0]
        naadam_url = BASE + base

        events.append({
            "title": title,
            "url": naadam_url
        })

    return events

if __name__ == "__main__":
    events = get_state_naadams()
    for event in events:
        print(event)
    print(f"Found {len(events)} state Naadams")

if __name__ == "__main__":
    url = "https://www.devjee.mn/t"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    for a in soup.find_all("a"):
        print(a)

import requests
r = requests.get("https://www.devjee.mn/t")
print(r.text[:2000])