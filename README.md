# itertooldict

A missing feature of `itertools`: labeled product of multiple choices from a dictionary.

## Installation

```bash
pip install itertooldict
```

## Usage

`itertooldict` takes a dictionary where values are iterables and yields dictionaries representing their Cartesian product. It behaves exactly like `itertools.product` but for dictionaries.

> [!TIP]
> While it works with standard dictionaries in Python 3.7+, using `collections.OrderedDict` is preferred to ensure consistent key ordering across all environments when no `keyorder` is specified.

```python
from itertooldict import itertooldict
from collections import OrderedDict

data = OrderedDict([
    ("voltage", ["Vmax", "Vmin"]),
    ("temp", ["hot", "cold"])
])

for combo in itertooldict(data):
    print(combo)

# Output:
# {'voltage': 'Vmax', 'temp': 'hot'}
# {'voltage': 'Vmax', 'temp': 'cold'}
# {'voltage': 'Vmin', 'temp': 'hot'}
# {'voltage': 'Vmin', 'temp': 'cold'}
```

### Specifying Key Order

You can use the `keyorder` argument to specify the order of keys in the resulting dictionaries and the order in which the product is calculated.

```python
data = {"a": [1, 2], "b": ["x", "y"]}
# Iterate with 'b' as the outer loop and 'a' as the inner loop
for combo in itertooldict(data, keyorder=["b", "a"]):
    print(combo)
# {'b': 'x', 'a': 1}
# {'b': 'x', 'a': 2}
# {'b': 'y', 'a': 1}
# {'b': 'y', 'a': 2}
```

### Compatibility with list() and enumerate()

`itertooldict` works seamlessly with standard Python functions:

```python
# Convert to list
all_combos = list(itertooldict(data))

# Use with enumerate
for i, combo in enumerate(itertooldict(data)):
    print(f"{i}: {combo}")
```
