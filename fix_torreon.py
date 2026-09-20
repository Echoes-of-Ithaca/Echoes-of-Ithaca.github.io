import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove torreon from wherever it got injected accidentally (likely Odiseo)
torreon_html_to_remove = r'\s*<div class="gallery-item">\s*<img src="assets/Nemea_References/Timeline/Environtment/torreon 1\.png" alt="Torreón">\s*<p data-es="Torreón" data-en="Keep">Torreón</p>\s*</div>'
html = re.sub(torreon_html_to_remove, '', html)

# 2. Add torreon precisely to gallery-env-edificios
edificios_torreon = """
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Environtment/torreon 1.png" alt="Torreón">
                                <p data-es="Torreón" data-en="Keep">Torreón</p>
                            </div>
                        </div>"""
# Replace the end of gallery-env-edificios
html = re.sub(r'(<div id="gallery-env-edificios".*?)(</div>\s*</div>)', r'\1' + edificios_torreon, html, flags=re.DOTALL)

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
