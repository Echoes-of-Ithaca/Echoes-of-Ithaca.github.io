from html.parser import HTMLParser

class DivTracker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
    def handle_starttag(self, tag, attrs):
        if tag == "div":
            attr_dict = dict(attrs)
            self.stack.append(attr_dict.get("id", "div"))
    def handle_endtag(self, tag):
        if tag == "div":
            if self.stack:
                closed = self.stack.pop()
                # print(f"Closed: {closed}")

parser = DivTracker()
with open("production.html", "r", encoding="utf-8") as f:
    parser.feed(f.read())
print("Unclosed divs:", parser.stack)
