import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix prod-methodology
css = css.replace('background: white;', 'background: rgba(28, 22, 25, 0.8);')

# Fix tech-grid overlapping
css = css.replace('grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));', 'grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));')

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)
