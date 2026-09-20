import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'<img src="assets/(?:char_placeholder\.jpg|env_placeholder\.jpg|hero_bg\.jpg)" alt=".*?">\s*', '', html)

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
