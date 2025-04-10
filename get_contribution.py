import requests
from bs4 import BeautifulSoup

def get_contributions(username):
    url = f"https://github.com/users/{username}/contributions"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    res = requests.get(url, headers=headers) 
    soup = BeautifulSoup(res.text, "html.parser")
    data = []

    for td in soup.find_all("td", {"class": "ContributionCalendar-day"}):
        date = td.get("data-date")
        level = int(td.get("data-level", 0))  # 濃さの出力
        data.append((date, level))

    return data

debug = 1 # debug用
if debug:
    contribs = get_contributions('zawa-kun') # ユーザーネームを入力
    for date, level in contribs[-7:]:  # 直近1週間だけ表示
        print(f"{date}: {level} level")
