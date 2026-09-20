import re

with open("production.html", "r", encoding="utf-8") as f:
    html = f.read()

# Characters
html = html.replace('>Odiseo</div>', ' data-es="Odiseo" data-en="Odysseus">Odiseo</div>')
html = html.replace('>Eurylocus</div>', ' data-es="Eurylocus" data-en="Eurylochus">Eurylocus</div>')
html = html.replace('>Polites</div>', ' data-es="Polites" data-en="Polites">Polites</div>')
html = html.replace('>Soldado Enemigo</div>', ' data-es="Soldado Enemigo" data-en="Enemy Soldier">Soldado Enemigo</div>')
html = html.replace('>Soldado MiniBoss</div>', ' data-es="Soldado MiniBoss" data-en="MiniBoss Soldier">Soldado MiniBoss</div>')

# Weapons
html = html.replace('>Arco</div>', ' data-es="Arco" data-en="Bow">Arco</div>')
html = html.replace('>Espada</div>', ' data-es="Espada" data-en="Sword">Espada</div>')
html = html.replace('>Ballesta</div>', ' data-es="Ballesta" data-en="Crossbow">Ballesta</div>')
html = html.replace('>Armadura</div>', ' data-es="Armadura" data-en="Armor">Armadura</div>')

# Environments
html = html.replace('>Mapa Nivel 1</div>', ' data-es="Mapa Nivel 1" data-en="Level 1 Map">Mapa Nivel 1</div>')
html = html.replace('>Edificios</div>', ' data-es="Edificios" data-en="Buildings">Edificios</div>')

# UI
html = html.replace('>Menú Principal</div>', ' data-es="Menú Principal" data-en="Main Menu">Menú Principal</div>')
html = html.replace('>UI Combate</div>', ' data-es="UI Combate" data-en="Combat UI">UI Combate</div>')

with open("production.html", "w", encoding="utf-8") as f:
    f.write(html)
