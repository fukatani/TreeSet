import unittest
from treemap import TreeMap


class TestTreeMap(unittest.TestCase):
    def test_keys(self):
        empty = TreeMap()
        self.assertEqual([], list(empty.keys()))

        non_empty = TreeMap({5: "a", 4: "b", 3: "c"})
        self.assertSequenceEqual([3, 4, 5], list(non_empty.keys()))

    def test_add_item(self):
        tm = TreeMap()
        tm["b"] = "B"
        tm["a"] = "A"
        self.assertSequenceEqual(["a", "b"], list(tm.keys()))

    def test_remove_item(self):
        tm = TreeMap({"c": "C", "b": "B", "a": "A"})
        del tm["b"]
        self.assertSequenceEqual(["a", "c"], list(tm.keys()))

    def test_items(self):
        tm = TreeMap({"c": "C", "b": "B", "a": "A"})
        keys = [k for k, v in tm.items()]
        self.assertSequenceEqual(["a", "b", "c"], keys)

    def test_iteration(self):
        tm = TreeMap({"c": "C", "b": "B", "a": "A"})
        keys = [k for k in tm]
        self.assertSequenceEqual(["a", "b", "c"], keys)


if __name__ == '__main__':
    unittest.main()
