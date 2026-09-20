import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

new_html = """
                <header class="section-header">
                    <h2 data-es="Evolución del Proyecto" data-en="Project Evolution">Evolución del Proyecto</h2>
                    <p data-es="Selecciona una categoría para explorar la evolución visual." data-en="Select a category to explore visual evolution.">Selecciona una categoría para explorar la evolución visual.</p>
                </header>

                <div class="timeline-main-menu">
                    <div class="main-menu-card active" onclick="openTimelineMain('personajes')" id="menu-personajes">
                        <img src="assets/char_placeholder.jpg" alt="Personajes">
                        <h2 data-es="Personajes" data-en="Characters">Personajes</h2>
                    </div>
                    <div class="main-menu-card" onclick="openTimelineMain('entornos')" id="menu-entornos">
                        <img src="assets/env_placeholder.jpg" alt="Entornos">
                        <h2 data-es="Entornos" data-en="Environments">Entornos</h2>
                    </div>
                    <div class="main-menu-card" onclick="openTimelineMain('ui')" id="menu-ui">
                        <img src="assets/hero_bg.jpg" alt="UI">
                        <h2 data-es="Diseño e Interfaz" data-en="Design & UI">Diseño e Interfaz</h2>
                    </div>
                </div>

                <!-- SECTION: PERSONAJES -->
                <div id="section-personajes" class="timeline-section-content" style="display:block;">
                    <!-- PERSONAJES SQUARES -->
                    <h3 class="timeline-section-title" data-es="Elenco" data-en="Cast">Elenco</h3>
                    <div class="timeline-squares-grid" id="char-squares">
                        <div class="timeline-square active" onclick="openGallery('char', 'odiseo')">Odiseo</div>
                        <div class="timeline-square" onclick="openGallery('char', 'eurylocus')">Eurylocus</div>
                        <div class="timeline-square" onclick="openGallery('char', 'polites')">Polites</div>
                        <div class="timeline-square" onclick="openGallery('char', 'soldado-aliado')">Soldado Aliado</div>
                        <div class="timeline-square" onclick="openGallery('char', 'soldado-enemigo')">Soldado Enemigo</div>
                        <div class="timeline-square" onclick="openGallery('char', 'soldado-miniboss')">Soldado MiniBoss</div>
                    </div>

                    <div class="timeline-gallery-container" id="char-galleries">
                        <div id="gallery-char-odiseo" class="timeline-gallery active">
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Odiseo/Odiseo concept art.png" alt="Concept Art">
                                <p data-es="Concept Art" data-en="Concept Art">Concept Art</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Odiseo/OdiseoColorkeys.png" alt="Color Keys">
                                <p data-es="Color Keys" data-en="Color Keys">Color Keys</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Odiseo/Odiseo Antiguo Modelo 3D.png" alt="Modelo Antiguo">
                                <p data-es="Modelo Antiguo" data-en="Old Model">Modelo Antiguo</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Odiseo/detalle hombros.png" alt="Detalle Hombros">
                                <p data-es="Detalle Hombros" data-en="Shoulders Detail">Detalle Hombros</p>
                            </div>
                            <div class="gallery-item">
                                <img src="assets/Nemea_References/Timeline/Odiseo/Odiseo ArmaduraValores.png" alt="Armadura">
                                <p data-es="Valores Armadura" data-en="Armor Values">Valores Armadura</p>
                            </div>
                        </div>
                        
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

                    <!-- ARMAS SQUARES -->
                    <h3 class="timeline-section-title" data-es="Armamento" data-en="Armory">Armamento</h3>
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
                </div>

                <!-- SECTION: ENTORNOS -->
                <div id="section-entornos" class="timeline-section-content" style="display:none;">
                    <div class="timeline-gallery-container">
                        <div class="gallery-item" style="padding-top: 3rem;"><p>Galería de Entornos Próximamente...</p></div>
                    </div>
                </div>

                <!-- SECTION: UI -->
                <div id="section-ui" class="timeline-section-content" style="display:none;">
                    <div class="timeline-gallery-container">
                        <div class="gallery-item" style="padding-top: 3rem;"><p>Galería de Diseño e Interfaz Próximamente...</p></div>
                    </div>
                </div>
"""

pattern = re.compile(r'<header class="section-header">.*?</div>\s*(?=<!-- Tab 2: Producción -->)', re.DOTALL)
html = pattern.sub(new_html, html)

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
