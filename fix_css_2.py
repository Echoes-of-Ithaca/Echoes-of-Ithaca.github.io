import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix tech-box
css = re.sub(r'\.tech-box \{.*?\n\}', '''.tech-box {
    background: rgba(28, 22, 25, 0.8);
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    border: 2px solid var(--color-primary);
    transition: transform 0.3s;
}''', css, flags=re.DOTALL)

# Fix tech-card
css = re.sub(r'\.tech-card \{.*?\n\}', '''.tech-card {
    display: flex;
    align-items: center;
    background: rgba(15, 12, 14, 0.8);
    border-radius: 8px;
    padding: 1.5rem;
    border: 1px solid rgba(212, 175, 55, 0.3);
    box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    transition: transform 0.3s;
}''', css, flags=re.DOTALL)

# Also fix tech-info h4 colors if needed
css = re.sub(r'\.tech-info h4 \{.*?\n\}', '''.tech-info h4 {
    margin: 0 0 0.5rem 0;
    font-size: 1.2rem;
    color: var(--color-primary);
}''', css, flags=re.DOTALL)

css = css.replace('.tech-info p {\n    margin: 0;\n    color: var(--color-text);\n    font-size: 0.95rem;\n    line-height: 1.4;\n}', '.tech-info p {\n    margin: 0;\n    color: var(--color-text-light);\n    font-size: 0.95rem;\n    line-height: 1.4;\n}')

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)
