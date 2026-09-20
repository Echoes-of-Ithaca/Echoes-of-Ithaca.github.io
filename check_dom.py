from bs4 import BeautifulSoup

with open("production.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

prod = soup.find(id="tab-production")
timeline = soup.find(id="tab-timeline")

if prod in timeline.descendants:
    print("YES! tab-production is INSIDE tab-timeline!")
else:
    print("NO! tab-production is a sibling.")
