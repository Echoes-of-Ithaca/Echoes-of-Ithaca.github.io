import re

with open("epic.html", "r", encoding="utf-8") as f:
    html = f.read()

old_iframe = '<iframe width="100%" height="450" src="https://www.youtube.com/embed/QXeYVV1zcUc?list=PLpksQhlStW4NlNIhYFkl-ZrRZwFAlwf4O&si=dCG7wGKLMVol_W0g" title="Epic The Musical Fan Animations" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="border-radius:12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);"></iframe>'
new_iframe = '<iframe width="100%" height="450" src="https://www.youtube-nocookie.com/embed/QXeYVV1zcUc?list=PLpksQhlStW4NlNIhYFkl-ZrRZwFAlwf4O" title="Epic The Musical" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius:12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);"></iframe>'

html = html.replace(old_iframe, new_iframe)

with open("epic.html", "w", encoding="utf-8") as f:
    f.write(html)
