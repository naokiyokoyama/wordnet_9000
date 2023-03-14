# wordnet_9000

## Installation
    
```bash
pip install -e .
```

## Quickstart

```bash
python -m wordnet_9000.example
# Give either 0, 1, or 2 words
# If 0: prints all ancestors of a random word
# If 1: prints all ancestors of that word
# If 2: determines whether either is an ancestor of the other
```
Examples:
```bash
$ python -m wordnet_9000.example dog
Word: dog
Parents:
canine
carnivore
placental
mammal
vertebrate
chordate
animal
organism
living thing
whole
object
$ python -m wordnet_9000.example animal
Word: animal
Parents:
organism
living thing
whole
object
$ python -m wordnet_9000.example dog animal
animal is an ancestor of dog
````
## Usage

```python
from wordnet_9000 import Wordnet9000
w = Wordnet9000()
result = w.is_ancestor("dog", "animal")
# result contains:
# 0 if "dog" is an ancestor of "animal"
# 1 if "animal" is an ancestor of "dog"
# -1 if neither are an ancestor of the other
```
