import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace('background: #fff;', 'background: rgba(28, 22, 25, 0.8);\n    border: 1px solid var(--color-primary);')
css = css.replace('box-shadow: 0 4px 15px rgba(0,0,0,0.05);', 'box-shadow: 0 4px 15px rgba(0,0,0,0.5);')
css = css.replace('box-shadow: 0 4px 10px rgba(0,0,0,0.05);', 'box-shadow: 0 4px 10px rgba(0,0,0,0.5);')
css = css.replace('color: #333;', 'color: var(--color-text);')
css = css.replace('color: #222;', 'color: var(--color-primary);')

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)
