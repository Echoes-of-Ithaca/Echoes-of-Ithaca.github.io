with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

# Hide sections initially
html = html.replace('id="section-entornos" class="timeline-section-content" style="padding-top: 4rem; margin-top: 4rem; border-top: 1px solid rgba(212, 175, 55, 0.3);"', 'id="section-entornos" class="timeline-section-content" style="display:none;"')
html = html.replace('id="section-ui" class="timeline-section-content" style="padding-top: 4rem; margin-top: 4rem; border-top: 1px solid rgba(212, 175, 55, 0.3);"', 'id="section-ui" class="timeline-section-content" style="display:none;"')
html = html.replace('id="section-personajes" class="timeline-section-content" style="padding-top: 2rem;"', 'id="section-personajes" class="timeline-section-content" style="display:block;"')

# Add UI subcategories
ui_section = """<div id="section-ui" class="timeline-section-content" style="display:none;">
                    <h2>Diseño e Interfaz</h2>
                    
                    <div class="timeline-squares-grid" id="ui-squares">
                        <div class="timeline-square active" onclick="openGallery('ui', 'menu')">Menú Principal</div>
                        <div class="timeline-square" onclick="openGallery('ui', 'combate')">UI Combate</div>
                    </div>

                    <div class="timeline-gallery-container" id="ui-galleries">
                        <div id="gallery-ui-menu" class="timeline-gallery active">
                            <div class="gallery-item"><p>Próximamente / Coming Soon</p></div>
                        </div>
                        <div id="gallery-ui-combate" class="timeline-gallery">
                            <div class="gallery-item"><p>Próximamente / Coming Soon</p></div>
                        </div>
                    </div>
                </div>"""

import re
html = re.sub(r'<div id="section-ui" class="timeline-section-content".*?</div>\s*</div>', ui_section, html, flags=re.DOTALL)

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
