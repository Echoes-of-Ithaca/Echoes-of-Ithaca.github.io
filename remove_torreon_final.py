import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

torreon_html_to_remove = r'\s*<div class="gallery-item">\s*<img src="assets/Nemea_References/Timeline/Environtment/torreon 1\.png" alt="Torreón">\s*<p data-es="Torreón" data-en="Keep">Torreón</p>\s*</div>'
html = re.sub(torreon_html_to_remove, '', html)

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
