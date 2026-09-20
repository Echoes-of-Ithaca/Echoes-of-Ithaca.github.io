import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove prod-graphic and make text center maybe
html = re.sub(r'<div class="prod-graphic">.*?</div>\s*</div>\s*</div>', '</div>\n                    </div>', html, flags=re.DOTALL)
html = html.replace('<div class="prod-methodology">', '<div class="prod-methodology" style="display: block; text-align: center; max-width: 800px; margin: 0 auto;">')
html = html.replace('<div class="prod-text">', '<div class="prod-text" style="width: 100%;">')

# 2. Change Hack'n'Plan to Jira
html = html.replace("HACK'N'PLAN", 'JIRA')
html = html.replace('data-en="JIRA"', 'data-en="JIRA"')
html = html.replace('Utilizado para la planificación, documentación y seguimiento del progreso del juego.', 'Utilizado para la planificación y seguimiento del progreso de los Sprints.')
html = html.replace('Used for planning, documenting, and tracking game progress.', 'Used for planning and tracking Sprint progress.')

# 3. Add Substance Painter and Blender
blender_painter_html = """
                        <div class="tech-card">
                            <div class="tech-logo" style="background:#ea7600; color:white;">Bl</div>
                            <div class="tech-info">
                                <h4>Blender</h4>
                                <p data-es="Modelado 3D adicional y renderizado." data-en="Additional 3D modeling and rendering.">Modelado 3D adicional y renderizado.</p>
                            </div>
                        </div>
                        <div class="tech-card">
                            <div class="tech-logo" style="background:#e42426; color:white;">Sp</div>
                            <div class="tech-info">
                                <h4>Substance Painter</h4>
                                <p data-es="Texturizado 3D PBR." data-en="PBR 3D Texturing.">Texturizado 3D PBR.</p>
                            </div>
                        </div>"""

html = html.replace('</div>\n                    </div>\n                </div>\n\n                <div class="tech-category">\n                    <h3 data-es="PROGRAMMING', blender_painter_html + '\n                    </div>\n                </div>\n\n                <div class="tech-category">\n                    <h3 data-es="PROGRAMMING')

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
