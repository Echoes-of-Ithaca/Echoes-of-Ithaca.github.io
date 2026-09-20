import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove square
html = re.sub(r'<div class="timeline-square" onclick="openGallery\(\'char\', \'soldado-aliado\'\)">Soldado Aliado</div>\s*', '', html)

# Remove gallery
html = re.sub(r'<div id="gallery-char-soldado-aliado" class="timeline-gallery">\s*<div class="gallery-item"><p>Próximamente / Coming Soon</p></div>\s*</div>\s*', '', html)

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
