import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

# Make all sections visible by default
html = html.replace('id="section-personajes" class="timeline-section-content" style="display:block;"', 'id="section-personajes" class="timeline-section-content" style="padding-top: 2rem;"')
html = html.replace('id="section-entornos" class="timeline-section-content" style="display:none;"', 'id="section-entornos" class="timeline-section-content" style="padding-top: 4rem; margin-top: 4rem; border-top: 1px solid rgba(212, 175, 55, 0.3);"')
html = html.replace('id="section-ui" class="timeline-section-content" style="display:none;"', 'id="section-ui" class="timeline-section-content" style="padding-top: 4rem; margin-top: 4rem; border-top: 1px solid rgba(212, 175, 55, 0.3);"')

# Update titles for Entornos and UI
html = html.replace('<div class="gallery-item" style="padding-top: 3rem;"><p>Galería de Entornos Próximamente...</p></div>', '<h2>Entornos</h2><div class="gallery-item" style="padding-top: 3rem;"><p>Galería de Entornos Próximamente...</p></div>')
html = html.replace('<div class="gallery-item" style="padding-top: 3rem;"><p>Galería de Diseño e Interfaz Próximamente...</p></div>', '<h2>Diseño e Interfaz</h2><div class="gallery-item" style="padding-top: 3rem;"><p>Galería de Diseño e Interfaz Próximamente...</p></div>')

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
