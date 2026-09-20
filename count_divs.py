from html.parser import HTMLParser

class DivCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.div_depth = 0
        self.in_timeline = False
        self.timeline_depth = 0
        self.production_found = False
        self.production_in_timeline = False

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            self.div_depth += 1
            attr_dict = dict(attrs)
            if attr_dict.get("id") == "tab-timeline":
                self.in_timeline = True
                self.timeline_depth = self.div_depth
            if attr_dict.get("id") == "tab-production":
                self.production_found = True
                if self.in_timeline:
                    self.production_in_timeline = True

    def handle_endtag(self, tag):
        if tag == "div":
            if self.in_timeline and self.div_depth == self.timeline_depth:
                self.in_timeline = False
            self.div_depth -= 1

parser = DivCounter()
with open("production.html", "r", encoding="utf-8") as f:
    parser.feed(f.read())

print("Production found:", parser.production_found)
print("Production in timeline:", parser.production_in_timeline)
