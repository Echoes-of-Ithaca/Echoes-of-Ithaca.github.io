import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

# Append torreon 1.png to gallery-env-edificios
edificios_new = """<div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Environtment/torreon 1.png" alt="Torreón">
                                <p data-es="Torreón" data-en="Keep">Torreón</p>
                            </div>
                        </div>"""
html = html.replace('</p>\n                            </div>\n                        </div>', '</p>\n                            </div>\n                            ' + edificios_new, 1)

# Replace UI Menu
menu_html = """<div id="gallery-ui-menu" class="timeline-gallery active">
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Menu principal/Menu principal.png" alt="Menú Principal">
                                <p data-es="Menú Principal" data-en="Main Menu">Menú Principal</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Menu principal/Menu opciones.png" alt="Menú Opciones">
                                <p data-es="Opciones" data-en="Options">Opciones</p>
                            </div>
                        </div>"""
html = re.sub(r'<div id="gallery-ui-menu" class="timeline-gallery active">\s*<div class="gallery-item"><p>Próximamente / Coming Soon</p></div>\s*</div>', menu_html, html)

# Replace UI Combate
combate_html = """<div id="gallery-ui-combate" class="timeline-gallery">
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/UI combate/UI Combate.png" alt="UI Combate">
                                <p data-es="Interfaz de Combate" data-en="Combat UI">Interfaz de Combate</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/UI combate/UI Dialogos.png" alt="UI Diálogos">
                                <p data-es="Sistema de Diálogos" data-en="Dialog System">Sistema de Diálogos</p>
                            </div>
                        </div>"""
html = re.sub(r'<div id="gallery-ui-combate" class="timeline-gallery">\s*<div class="gallery-item"><p>Próximamente / Coming Soon</p></div>\s*</div>', combate_html, html)


with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
