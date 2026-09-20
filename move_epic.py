import re

# 1. REMOVE FROM PRODUCTION.HTML
with open("production.html", "r", encoding="utf-8") as f:
    prod_html = f.read()

# Remove button
prod_html = re.sub(r'\s*<button class="tab-btn" onclick="switchTab\(\'epic\'\)" id="btn-tab-epic".*?Epic The Musical</button>', '', prod_html)

# Remove content
prod_html = re.sub(r'\s*<!-- Tab 3: Epic The Musical -->\s*<div id="tab-epic".*?(?=</div>\s*</div>\s*</div>\s*<!-- Footer -->)', '', prod_html, flags=re.DOTALL)

with open("production.html", "w", encoding="utf-8") as f:
    f.write(prod_html)

# 2. ADD TO EPIC.HTML
with open("epic.html", "r", encoding="utf-8") as f:
    epic_html = f.read()

new_epic_content = """<div class="epic-container">
                    <!-- Columna Izquierda: Spotify -->
                    <div class="epic-column">
                        <iframe style="border-radius:12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" src="https://open.spotify.com/embed/playlist/3sdEH7HfFE3d4xry5RnnLr?utm_source=generator&theme=0" width="100%" height="450" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
                        <div class="epic-text-box">
                            <h3 data-es="La Inspiración Original" data-en="The Original Inspiration">La Inspiración Original</h3>
                            <p data-es="Esta increíble obra musical ha sido nuestra mayor inspiración y el origen de la idea para crear este videojuego. Escuchar estas canciones nos dio la visión de traer este universo a la vida." data-en="This incredible musical masterpiece has been our biggest inspiration and the origin of the idea to create this video game. Listening to these songs gave us the vision to bring this universe to life.">Esta increíble obra musical ha sido nuestra mayor inspiración y el origen de la idea para crear este videojuego. Escuchar estas canciones nos dio la visión de traer este universo a la vida.</p>
                        </div>
                    </div>

                    <!-- Columna Derecha: YouTube -->
                    <div class="epic-column">
                        <iframe width="100%" height="450" src="https://www.youtube.com/embed/videoseries?list=PLpksQhlStW4NlNIhYFkl-ZrRZwFAlwf4O" title="Epic The Musical Fan Animations" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="border-radius:12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);"></iframe>
                        <div class="epic-text-box">
                            <h3 data-es="El Arte de la Comunidad" data-en="Community Art">El Arte de la Comunidad</h3>
                            <p data-es="Una recopilación de animáticas y arte creado por artistas y fans de todo el mundo. Su talento y pasión por la historia nos motiva a dar lo mejor en nuestro diseño visual." data-en="A compilation of animatics and art created by fans and artists from all over the world. Their talent and passion for the story motivates us to give our best in our visual design.">Una recopilación de animáticas y arte creado por artistas y fans de todo el mundo. Su talento y pasión por la historia nos motiva a dar lo mejor en nuestro diseño visual.</p>
                        </div>
                    </div>
                </div>"""

# Replace inside the container of epic.html
epic_html = re.sub(r'<div class="article-content">.*?</div>\s*</div>\s*</div>', '<div class="article-content">\n                ' + new_epic_content + '\n            </div>\n        </div>\n    </div>', epic_html, flags=re.DOTALL)

with open("epic.html", "w", encoding="utf-8") as f:
    f.write(epic_html)

