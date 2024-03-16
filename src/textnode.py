class TextNode:
    text = ""
    text_type = ""
    url = None

    def __init__(self, text1, type1, url1):
        self.text = text1
        self.text_type = type1
        self.url = url1
        return
    
    def __eq__(self, other):
        return (self.text == other.text) and ...
        (self.text_type == other.text_type) and ...
        (self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
