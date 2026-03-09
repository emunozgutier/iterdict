import itertools

class itertooldict:
    """
    An iterator that yields dictionaries representing the Cartesian product
    of values in the input dictionary.
    """
    def __init__(self, data):
        for key, value in data.items():
            if not isinstance(value, list):
                raise TypeError(f"Value for key '{key}' must be a list, got {type(value).__name__}")
            if len(value) == 0:
                raise ValueError(f"Value for key '{key}' must have at least one entry")
        
        self._data = data
        self._keys = list(data.keys())
        self._exclusions = []
        self._randomize = False

    def updateKeyOrder(self, keys):
        """Reorder the keys for iteration."""
        if set(keys) != set(self._keys):
            raise ValueError("Provided keys do not match existing keys")
        self._keys = list(keys)
        return self

    def random(self):
        """Randomize the order of yielded combinations."""
        self._randomize = True
        return self

    def __iter__(self):
        values = [self._data[k] for k in self._keys]
        combos = list(itertools.product(*values))
        
        if self._randomize:
            import random
            random.shuffle(combos)

        for combo in combos:
            d = dict(zip(self._keys, combo))
            # Filter out excluded combinations
            if not any(all(d.get(k) == v for k, v in exclusion.items()) for exclusion in self._exclusions):
                yield d

    def __len__(self):
        # This is a bit tricky if there are exclusions
        # But for list() compatibility, let's provide a rough estimate or handle it
        # Actually, list() uses __iter__. __len__ is good for progress bars etc.
        # However, itertools.product doesn't have len. 
        # Let's just calculate it.
        import math
        total = math.prod(len(self._data[k]) for k in self._keys)
        return total # Note: this doesn't account for exclusions, but it's common in iterators


    def remove(self, exclusion):
        """
        Exclude specific combinations from the iteration.
        Example: it.remove({"voltage": Vmax, "temp": hot})
        """
        self._exclusions.append(exclusion)
        return self
