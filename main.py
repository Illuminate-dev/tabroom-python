import csv

import requests
from bs4 import BeautifulSoup

URL = "https://www.tabroom.com/index/results/toc_bids.mhtml"

event_code_map = {
    "Lincoln Douglas": 102,
    "Policy": 103,
    "Public Forum": 104,
    "Worlds Schools": 105,
    "Dramatic Interp": 204,
    "Duo Interp": 206,
    "Extemp": 202,
    "Humorous Interp": 205,
    "Informative Speaking": 208,
    "Oral Interp of Literature": 216,
    "Original Oratory": 203,
    "Program Oral Interp": 207,
    "Congressional Debate": 301,
}


def main():
    response = requests.post(
        URL, data={"code": event_code_map["Policy"], "year": "2025"}
    )
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find(id=str(event_code_map["Policy"]))
    policy_teams = []

    for row in table.tbody.find_all("tr"):
        school = row.contents[1].get_text().strip()
        state = row.contents[3].get_text().strip()
        entry = row.contents[5].get_text().strip()
        bids = row.contents[7].get_text().strip()
        policy_teams.append(
            {"school": school, "state": state, "entry": entry, "bids": bids}
        )

    policy_teams = sorted(policy_teams, key=lambda x: x["bids"], reverse=True)

    with open("output.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=policy_teams[0].keys())
        writer.writeheader()
        writer.writerows(policy_teams)

    # print(soup.prettify())


if __name__ == "__main__":
    main()
