# code-katas

### 1.  Multiply two numbers.
##### - Module: multiply.py
##### - Tests: test_multiply.py
##### - Link: https://www.codewars.com/kata/multiply/train/python

```python
"""Submitted by bit2pixel."""
multiply = lambda x, y: x * y

```


### 2.  Reverse words if longer than 4 letters.
##### - Module: spin_words.py
##### - Tests: test_spin_words.py
##### - Link: https://www.codewars.com/kata/stop-gninnips-my-sdrow/train/python

```python
"""Submitted by superxiao."""
import re

def spin_words(sentence):
    # Your code goes here
    return re.sub(r"\w{5,}", lambda w: w.group(0)[::-1], sentence)

```