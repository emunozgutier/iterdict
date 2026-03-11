import unittest
from collections import OrderedDict
from itertooldict import itertooldict

class TestIterdict(unittest.TestCase):
    def test_ordered_dict(self):
        data = OrderedDict([("a", [1, 2]), ("b", ["x", "y"])])
        results = list(itertooldict(data))
        expected = [
            {"a": 1, "b": "x"},
            {"a": 1, "b": "y"},
            {"a": 2, "b": "x"},
            {"a": 2, "b": "y"},
        ]
        self.assertEqual(results, expected)
        # Ensure key order is preserved in the yielded dicts
        for res in results:
            self.assertEqual(list(res.keys()), ["a", "b"])

    def test_basic_product(self):
        data = {"a": [1, 2], "b": ["x", "y"]}
        results = list(itertooldict(data))
        expected = [
            {"a": 1, "b": "x"},
            {"a": 1, "b": "y"},
            {"a": 2, "b": "x"},
            {"a": 2, "b": "y"},
        ]
        self.assertEqual(results, expected)

    def test_nested_list(self):
        data = {'a': [[1, 2, 3], [3, 2, 1]], 'b': [1, 0]}
        results = list(itertooldict(data))
        expected = [
            {'a': [1, 2, 3], 'b': 1},
            {'a': [1, 2, 3], 'b': 0},
            {'a': [3, 2, 1], 'b': 1},
            {'a': [3, 2, 1], 'b': 0},
        ]
        self.assertEqual(results, expected)

    def test_keyorder(self):
        data = {"a": [1, 2], "b": ["x", "y"]}
        results = list(itertooldict(data, keyorder=["b", "a"]))
        expected = [
            {"b": "x", "a": 1},
            {"b": "x", "a": 2},
            {"b": "y", "a": 1},
            {"b": "y", "a": 2},
        ]
        self.assertEqual(results, expected)
        for res in results:
            self.assertEqual(list(res.keys()), ["b", "a"])

    def test_keyorder_validation(self):
        data = {"a": [1], "b": [2]}
        with self.assertRaises(ValueError):
            list(itertooldict(data, keyorder=["a"])) # Missing 'b'
        with self.assertRaises(ValueError):
            list(itertooldict(data, keyorder=["a", "c"])) # Wrong key 'c'

    def test_validation_not_dict(self):
        with self.assertRaises(TypeError):
            list(itertooldict("not a dict"))

    def test_list_and_enumerate(self):
        data = {"a": [1, 2], "b": [3, 4]}
        results = list(itertooldict(data))
        self.assertEqual(len(results), 4)
        for i, val in enumerate(itertooldict(data)):
            self.assertEqual(val, results[i])

if __name__ == "__main__":
    unittest.main()
