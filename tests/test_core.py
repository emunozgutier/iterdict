import unittest
from iterdict import iterdict

class TestIterdict(unittest.TestCase):
    def test_basic_product(self):
        data = {"a": [1, 2], "b": ["x", "y"]}
        it = iterdict(data)
        results = list(it)
        expected = [
            {"a": 1, "b": "x"},
            {"a": 1, "b": "y"},
            {"a": 2, "b": "x"},
            {"a": 2, "b": "y"},
        ]
        self.assertEqual(results, expected)

    def test_remove_single(self):
        data = {"voltage": [10, 20], "temp": ["hot", "cold"]}
        it = iterdict(data)
        it.remove({"voltage": 10, "temp": "hot"})
        results = list(it)
        expected = [
            {"voltage": 10, "temp": "cold"},
            {"voltage": 20, "temp": "hot"},
            {"voltage": 20, "temp": "cold"},
        ]
        self.assertEqual(results, expected)

    def test_remove_partial(self):
        data = {"a": [1, 2], "b": ["x", "y"]}
        it = iterdict(data)
        it.remove({"a": 1})  # Should remove all where a=1
        results = list(it)
        expected = [
            {"a": 2, "b": "x"},
            {"a": 2, "b": "y"},
        ]
        self.assertEqual(results, expected)

    def test_validation_not_list(self):
        with self.assertRaises(TypeError):
            iterdict({"a": "not a list"})

    def test_validation_empty_list(self):
        with self.assertRaises(ValueError):
            iterdict({"a": []})

    def test_updateKeyOrder(self):
        data = {"a": [1], "b": [2]}
        it = iterdict(data)
        it.updateKeyOrder(["b", "a"])
        result = list(it)[0]
        self.assertEqual(list(result.keys()), ["b", "a"])

    def test_random(self):
        data = {"a": list(range(10)), "b": list(range(10))}
        it1 = list(iterdict(data))
        it2 = list(iterdict(data).random())
        self.assertNotEqual(it1, it2)

    def test_list_and_enumerate(self):
        data = {"a": [1, 2], "b": [3, 4]}
        it = iterdict(data)
        # Check list compatibility
        l = list(it)
        self.assertEqual(len(l), 4)
        # Check enumerate compatibility
        for i, val in enumerate(iterdict(data)):
            self.assertEqual(val, l[i])


if __name__ == "__main__":
    unittest.main()
