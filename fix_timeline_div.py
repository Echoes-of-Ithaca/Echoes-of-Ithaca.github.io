import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add the missing closing div for tab-timeline
html = html.replace('                </div>\n<!-- Tab 2: Producción -->', '                </div>\n            </div>\n<!-- Tab 2: Producción -->')

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
