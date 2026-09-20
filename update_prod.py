import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

new_timeline_html = """
                <!-- PERSONAJES -->
                <h3 class="timeline-section-title" data-es="Personajes" data-en="Characters">Personajes</h3>
                <div class="timeline-squares-grid" id="char-squares">
                    <div class="timeline-square active" onclick="openGallery('char', 'odiseo')">Odiseo</div>
                    <div class="timeline-square" onclick="openGallery('char', 'eurylocus')">Eurylocus</div>
                    <div class="timeline-square" onclick="openGallery('char', 'polites')">Polites</div>
                    <div class="timeline-square" onclick="openGallery('char', 'soldado-aliado')">Soldado Aliado</div>
                    <div class="timeline-square" onclick="openGallery('char', 'soldado-enemigo')">Soldado Enemigo</div>
                    <div class="timeline-square" onclick="openGallery('char', 'soldado-miniboss')">Soldado MiniBoss</div>
                </div>

                <div class="timeline-gallery-container" id="char-galleries">
                    <!-- Odiseo Gallery -->
                    <div id="gallery-char-odiseo" class="timeline-gallery active">
                        <div class="gallery-item">
                            <img src="assets/Nemea_References/Timeline/Odiseo/Odiseo concept art.png" alt="Concept Art">
                            <p data-es="Concept Art" data-en="Concept Art">Concept Art</p>
                        </div>
                        <div class="gallery-item">
                            <img src="assets/Nemea_References/Timeline/Odiseo/Odiseo Antiguo Modelo 3D.png" alt="Modelo Antiguo">
                            <p data-es="Modelo Antiguo" data-en="Old Model">Modelo Antiguo</p>
                        </div>
                        <div class="gallery-item">
                            <img src="assets/Nemea_References/Timeline/Odiseo/Odiseo ArmaduraValores.png" alt="Modelo Nuevo">
                            <p data-es="Detalles Nuevo" data-en="New Details">Detalles Nuevo</p>
                        </div>
                    </div>
                    
                    <!-- Others placeholders -->
                    <div id="gallery-char-eurylocus" class="timeline-gallery">
                        <div class="gallery-item"><p>Próximamente / Coming Soon</p></div>
                    </div>
                    <div id="gallery-char-polites" class="timeline-gallery">
                        <div class="gallery-item"><p>Próximamente / Coming Soon</p></div>
                    </div>
                    <div id="gallery-char-soldado-aliado" class="timeline-gallery">
                        <div class="gallery-item"><p>Próximamente / Coming Soon</p></div>
                    </div>
                    <div id="gallery-char-soldado-enemigo" class="timeline-gallery">
                        <div class="gallery-item"><p>Próximamente / Coming Soon</p></div>
                    </div>
                    <div id="gallery-char-soldado-miniboss" class="timeline-gallery">
                        <div class="gallery-item"><p>Próximamente / Coming Soon</p></div>
                    </div>
                </div>

                <!-- ARMAS -->
                <h3 class="timeline-section-title" data-es="Armas" data-en="Weapons">Armas</h3>
                <div class="timeline-squares-grid" id="weapon-squares">
                    <div class="timeline-square active" onclick="openGallery('weapon', 'arco')">Arco</div>
                    <div class="timeline-square" onclick="openGallery('weapon', 'espada')">Espada</div>
                    <div class="timeline-square" onclick="openGallery('weapon', 'ballesta')">Ballesta</div>
                    <div class="timeline-square" onclick="openGallery('weapon', 'armadura')">Armadura</div>
                </div>

                <div class="timeline-gallery-container" id="weapon-galleries">
                    <div id="gallery-weapon-arco" class="timeline-gallery active">
                        <div class="gallery-item">
                            <img src="assets/Nemea_References/Timeline/Armas/ARco odiseo Concept Art.png" alt="Arco">
                            <p data-es="Concept Art" data-en="Concept Art">Concept Art</p>
                        </div>
                    </div>
                    <div id="gallery-weapon-espada" class="timeline-gallery">
                        <div class="gallery-item">
                            <img src="assets/Nemea_References/Timeline/Armas/Espada Odiseo Concept Art.png" alt="Espada">
                            <p data-es="Concept Art" data-en="Concept Art">Concept Art</p>
                        </div>
                    </div>
                    <div id="gallery-weapon-ballesta" class="timeline-gallery">
                        <div class="gallery-item">
                            <img src="assets/Nemea_References/Timeline/Armas/Ballesta de brazo concept Art.png" alt="Ballesta">
                            <p data-es="Concept Art" data-en="Concept Art">Concept Art</p>
                        </div>
                    </div>
                    <div id="gallery-weapon-armadura" class="timeline-gallery">
                        <div class="gallery-item">
                            <img src="assets/Nemea_References/Timeline/Armas/Armadura Odiseo Concept Art.png" alt="Armadura">
                            <p data-es="Concept Art" data-en="Concept Art">Concept Art</p>
                        </div>
                    </div>
                </div>
"""

pattern = re.compile(r'<div class="evolution-grid">.*?</div>\s*(?=</div>\s*<!-- Tab 2: Producción -->)', re.DOTALL)
html = pattern.sub(new_timeline_html, html)

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
