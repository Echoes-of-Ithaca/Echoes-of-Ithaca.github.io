import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the two closing divs that prematurely close tab-production
html = html.replace('                    </div>\n                    </div>\n                    </div>\n\n                <!-- Production Tools (3 cols) -->', '                    </div>\n                    </div>\n\n                <!-- Production Tools (3 cols) -->')

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
