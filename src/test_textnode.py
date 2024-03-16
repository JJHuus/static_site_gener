import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq2(self): #this should fail
        node = TextNode("This is a pollo node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq3(self): #this should fail
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq4(self): #this should fail
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq5(self): #this should fail
        node = TextNode("This is a text node", "italic", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq6(self): #this should fail
        node = TextNode("This is a pollo node", "italic", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq7(self): #this should fail
        node = TextNode(None, "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
