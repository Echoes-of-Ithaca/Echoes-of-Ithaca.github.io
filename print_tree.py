from html.parser import HTMLParser

class TreePrinter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.in_timeline = False
        self.timeline_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            attr_dict = dict(attrs)
            div_id = attr_dict.get("id", "")
            if div_id == "tab-timeline":
                self.in_timeline = True
                self.timeline_depth = self.depth
            
            if self.in_timeline:
                print("  " * (self.depth - self.timeline_depth) + f"<{div_id}>")
            
            self.depth += 1

    def handle_endtag(self, tag):
        if tag == "div":
            self.depth -= 1
            if self.in_timeline and self.depth == self.timeline_depth:
                self.in_timeline = False

parser = TreePrinter()
with open("production.html", "r", encoding="utf-8") as f:
    parser.feed(f.read())
