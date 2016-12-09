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

### 3.  Validate a 4 or 6 digit pin number.
##### - Module: validate_pin.py
##### - Tests: test_validate_pin.py
##### - Link: https://www.codewars.com/kata/regex-validate-pin-code/train/python

```python
"""Submitted by suic."""

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

```

### 4.  Convert string to Jaden Case.
##### - Module: to_jaden_case.py
##### - Tests: test_to_jaden_case.py
##### - Link: https://www.codewars.com/kata/jaden-casing-strings/train/python

```python
"""Submitted by Azuaron."""

def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())

```

### 5.  Calculate needed years to achieve investment goals.
##### - Module: calculate_years.py
##### - Tests: test_calculate_years.py
##### - Link: https://www.codewars.com/kata/money-money-money/train/python

```python
"""Submitted by pidi4."""

def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal = principal * (1 + 1 * interest * (1 - tax))
        years += 1
    return years

```