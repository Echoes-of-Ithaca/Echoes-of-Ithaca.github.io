import re

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('name: "Andrea Doña",', 'name: "Andrea Doña", image: "assets/Nemea_References/Equipo/Andrea.png",')
content = content.replace('name: "Carlos Suárez",', 'name: "Carlos Suárez", image: "assets/Nemea_References/Equipo/Carlos.jpg",')
content = content.replace('name: "Neus Gutiérrez",', 'name: "Neus Gutiérrez", image: "assets/Nemea_References/Equipo/Neus.jpg",')
content = content.replace('name: "Pau Almendrote",', 'name: "Pau Almendrote", image: "assets/Nemea_References/Equipo/Pau.png",')

# Now update the HTML template rendering
old_img = '<img src="assets/avatar_placeholder.jpg" alt="" class="team-avatar">'
new_img = '<img src="" alt="" class="team-avatar">'
content = content.replace(old_img, new_img)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)
