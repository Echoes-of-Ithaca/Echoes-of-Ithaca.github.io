import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

# Odiseo - Append new model
html = html.replace('</p>\n                            </div>\n                        </div>', '</p>\n                            </div>\n                            <div class="gallery-item">\n                                <img src="assets/Nemea_References/Timeline/Odiseo/Odiseo nuevo modelo 3d.png" alt="Modelo Nuevo">\n                                <p data-es="Modelo Nuevo" data-en="New Model">Modelo Nuevo</p>\n                            </div>\n                        </div>', 1)

# Eurylocus
eurylocus_html = """<div id="gallery-char-eurylocus" class="timeline-gallery">
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Eurylocus/Eurylocus concept art.png" alt="Concept Art">
                                <p data-es="Concept Art" data-en="Concept Art">Concept Art</p>
                            </div>
                        </div>"""
html = re.sub(r'<div id="gallery-char-eurylocus" class="timeline-gallery">.*?</div>\s*</div>', eurylocus_html, html, flags=re.DOTALL)

# Polites
polites_html = """<div id="gallery-char-polites" class="timeline-gallery">
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Polites/Polites concept art.png" alt="Concept Art">
                                <p data-es="Concept Art" data-en="Concept Art">Concept Art</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Polites/TFG DEFENSA.png" alt="Modelo 3D">
                                <p data-es="Modelo 3D" data-en="3D Model">Modelo 3D</p>
                            </div>
                        </div>"""
html = re.sub(r'<div id="gallery-char-polites" class="timeline-gallery">.*?</div>\s*</div>', polites_html, html, flags=re.DOTALL)

# Soldado Enemigo
enemigo_html = """<div id="gallery-char-soldado-enemigo" class="timeline-gallery">
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Soldado enemigo/soldado enemigo concept art.png" alt="Concept Art">
                                <p data-es="Concept Art" data-en="Concept Art">Concept Art</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Soldado enemigo/soldado enemigo color.png" alt="Color Keys">
                                <p data-es="Color" data-en="Color">Color</p>
                            </div>
                        </div>"""
html = re.sub(r'<div id="gallery-char-soldado-enemigo" class="timeline-gallery">.*?</div>\s*</div>', enemigo_html, html, flags=re.DOTALL)

# Soldado MiniBoss
miniboss_html = """<div id="gallery-char-soldado-miniboss" class="timeline-gallery">
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Soldado miniboss/concept art soldado miniboss.png" alt="Concept Art">
                                <p data-es="Concept Art" data-en="Concept Art">Concept Art</p>
                            </div>
                        </div>"""
html = re.sub(r'<div id="gallery-char-soldado-miniboss" class="timeline-gallery">.*?</div>\s*</div>', miniboss_html, html, flags=re.DOTALL)

# Entornos Section
entornos_section = """<!-- SECTION: ENTORNOS -->
                <div id="section-entornos" class="timeline-section-content" style="padding-top: 4rem; margin-top: 4rem; border-top: 1px solid rgba(212, 175, 55, 0.3);">
                    <h2>Entornos</h2>
                    
                    <div class="timeline-squares-grid" id="env-squares">
                        <div class="timeline-square active" onclick="openGallery('env', 'mapa')">Mapa Nivel 1</div>
                        <div class="timeline-square" onclick="openGallery('env', 'edificios')">Edificios</div>
                    </div>

                    <div class="timeline-gallery-container" id="env-galleries">
                        <div id="gallery-env-mapa" class="timeline-gallery active">
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Environtment/mapa concept art.png" alt="Concept Art">
                                <p data-es="Concept Art" data-en="Concept Art">Concept Art</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Environtment/mapa art concept 2.png" alt="Concept Art 2">
                                <p data-es="Concept Art V2" data-en="Concept Art V2">Concept Art V2</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Environtment/mapa blockout 1.png" alt="Blockout">
                                <p data-es="Blockout" data-en="Blockout">Blockout</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Environtment/modelo 3d mapa nivel 1.png" alt="Modelo 3D">
                                <p data-es="Modelo 3D (Work In Progress)" data-en="3D Model (WIP)">Modelo 3D (WIP)</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Environtment/modelo 3d mapa nivel 1 2.png" alt="Modelo 3D 2">
                                <p data-es="Modelo 3D - Detalle" data-en="3D Model - Detail">Modelo 3D - Detalle</p>
                            </div>
                        </div>
                        
                        <div id="gallery-env-edificios" class="timeline-gallery">
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Environtment/Casas concept art.png" alt="Casas Concept">
                                <p data-es="Casas (Concepto)" data-en="Houses (Concept)">Casas (Concepto)</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Environtment/casa concept art 2.png" alt="Casa Detalle">
                                <p data-es="Casa - Detalle" data-en="House - Detail">Casa - Detalle</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Environtment/templo concept art.png" alt="Templo">
                                <p data-es="Templo" data-en="Temple">Templo</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Environtment/torre concept art.png" alt="Torre">
                                <p data-es="Torre" data-en="Tower">Torre</p>
                            </div>
                        </div>
                    </div>
                </div>"""
html = re.sub(r'<!-- SECTION: ENTORNOS -->.*?</div>\s*</div>', entornos_section, html, flags=re.DOTALL)

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
