class htmlnode:
    tag = None
    value = None
    children = []
    props = {}

    def __init__(self, tag1 = None, value1 = None, children1 = [], props1 = {}):
        self.tag = tag1
        self.value = value1
        self.children = children1
        self.props = props1
        """
        An HTMLNode without a tag will just render as raw text
        An HTMLNode without a value will be assumed to have children
        An HTMLNode without children will be assumed to have a value
        An HTMLNode without props simply won't have any attributes
        """
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        output = ""
        items = self.props.items()
        for i in range(0, len(items)):
            output = output + items[i][0] + "=" + items[i][1]
            if i == 0:
                output = output + " "
        return output
    
    def __repr__(self):
        return (
            "\n" +
            f"t {self.tag}" + "\n" + 
            f"v {self.value}" + "\n" + 
            f"c {self.children}" + "\n" + 
            f"p {self.props.items()}" + "\n"
        )
    
    def __eq__(self, other):
        return (
            (self.tag == other.tag) and 
            (self.value == other.value) and 
            (self.children == other.children) and
            (self.props == other.props)
            )