import re

with open("epic.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('src="https://www.youtube.com/embed/videoseries?list=PLpksQhlStW4NlNIhYFkl-ZrRZwFAlwf4O"', 'src="https://www.youtube.com/embed/QXeYVV1zcUc?list=PLpksQhlStW4NlNIhYFkl-ZrRZwFAlwf4O&si=dCG7wGKLMVol_W0g"')

with open("epic.html", "w", encoding="utf-8") as f:
    f.write(html)
