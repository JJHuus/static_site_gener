import unittest

from htmlnode import htmlnode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = htmlnode("tag", 0, ["help", 1], {"test": True, "test2": False})
        node2 = htmlnode("tag", 0, ["help", 1], {"test": True, "test2": False})
        self.assertEqual(node, node2)
    def test_eq2(self): #tag1
        node = htmlnode("tag1", 0, ["help", 1], {"test": True, "test2": False})
        node2 = htmlnode("tag", 0, ["help", 1], {"test": True, "test2": False})
        self.assertEqual(node, node2)
    def test_eq3(self): #"value"
        node = htmlnode("tag", "value", ["help", 1], {"test": True, "test2": False})
        node2 = htmlnode("tag", 0, ["help", 1], {"test": True, "test2": False})
        self.assertEqual(node, node2)
    def test_eq4(self): #"1"
        node = htmlnode("tag", 0, ["help", "1"], {"test": True, "test2": False})
        node2 = htmlnode("tag", 0, ["help", 1], {"test": True, "test2": False})
        self.assertEqual(node, node2)
    def test_eq5(self): #"True"
        node = htmlnode("tag", 0, ["help", 1], {"test": "True", "test2": False})
        node2 = htmlnode("tag", 0, ["help", 1], {"test": True, "test2": False})
        self.assertEqual(node, node2)
    def test_eq6(self): #"False"
        node = htmlnode("tag", 0, ["help", 1], {"test": True, "test2": "False"})
        node2 = htmlnode("tag", 0, ["help", 1], {"test": True, "test2": False})
        self.assertEqual(node, node2)
   


if __name__ == "__main__":
    unittest.main()
