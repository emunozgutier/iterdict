# iterdict

A missing feature of `itertools`: labeled product of multiple choices from a dictionary.

## Installation

```bash
pip install iterdict
```

## Usage

`iterdict` takes a dictionary where values are iterables and yields dictionaries representing their Cartesian product.

```python
from iterdict import iterdict

data = {
    "voltage": ["Vmax", "Vmin"],
    "temp": ["hot", "cold"]
}

for combo in iterdict(data):
    print(combo)

# Output:
# {'voltage': 'Vmax', 'temp': 'hot'}
# {'voltage': 'Vmax', 'temp': 'cold'}
# {'voltage': 'Vmin', 'temp': 'hot'}
# {'voltage': 'Vmin', 'temp': 'cold'}
```

### Excluding Combinations

You can use the `.remove()` method to exclude specific combinations or patterns.

```python
it = iterdict(data)
it.remove({"voltage": "Vmax", "temp": "hot"})

for combo in it:
    print(combo)
# {'voltage': 'Vmax', 'temp': 'cold'}
# {'voltage': 'Vmin', 'temp': 'hot'}
# {'voltage': 'Vmin', 'temp': 'cold'}
```

You can also remove based on partial matches:

### Randomizing Order

You can randomize the order of the generated combinations:

```python
it = iterdict(data).random()
for combo in it:
    print(combo) # Order will be shuffled
```

### Updating Key Order

You can specify the order of keys in the resulting dictionaries:

```python
it = iterdict(data)
it.updateKeyOrder(["temp", "voltage"])
for combo in it:
    print(combo) # {'temp': 'hot', 'voltage': 'Vmax'}, ...
```

### Compatibility with list() and enumerate()

`iterdict` works seamlessly with standard Python functions:

```python
# Convert to list
all_combos = list(iterdict(data))

# Use with enumerate
for i, combo in enumerate(iterdict(data)):
    print(f"{i}: {combo}")
```
