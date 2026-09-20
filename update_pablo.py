import re

with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

pablo_es = "Después de 4 años estudiando diseño y desarrollo de videojuegos, he conseguido encontrar a decenas de personas que comparten la misma pasión que yo, la de crear historias con las que otros puedan disfrutar.<br><br>Y eso me ha llevado a querer ayudar al máximo de personas a dar a conocer su juego y a hacer entender a los equipos cuál es el mejor método para que sus audiencias consigan encontrar sus juegos.<br><br>En este proyecto he aportado tanto en el rol de analista de mercado como de lead artist, ayudando a encontrar el mejor nicho al que el juego debe ser dirigido y ayudando a coordinar a los artistas del equipo, organizar prioridades a la hora de trabajar y a implementar el trabajo colectivo dentro del motor."
pablo_en = "After 4 years studying video game design and development, I've managed to find dozens of people who share the same passion as me, that of creating stories for others to enjoy.<br><br>And that has led me to want to help as many people as possible to make their game known and to help teams understand the best method for their audiences to find their games.<br><br>In this project, I have contributed both as a market analyst and lead artist, helping to find the best niche for the game to target and helping to coordinate the team's artists, organize priorities when working, and implement the collective work within the engine."

# Use regex to find Pablo's object and replace bio_es and bio_en
pattern = r'(name:\s*"Pablo Longaron",.*?bio_es:\s*").*?(",\s*bio_en:\s*").*?(",\s*linkedin:)'
replacement = rf'\g<1>{pablo_es}\g<2>{pablo_en}\g<3>'

new_js = re.sub(pattern, replacement, js, flags=re.DOTALL)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(new_js)
