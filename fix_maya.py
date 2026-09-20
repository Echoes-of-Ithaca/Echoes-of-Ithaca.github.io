import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the missing closing div for Maya
html = html.replace('Modelado y animación 3D.</p>\n                            </div>\n                        \n                        <div class="tech-card">', 'Modelado y animación 3D.</p>\n                            </div>\n                        </div>\n                        \n                        <div class="tech-card">')

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
