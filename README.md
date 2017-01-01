# code-katas

### 1.  Multiply two numbers. (Kyu 8)
##### - Module: multiply.py
##### - Tests: test_multiply.py
##### - Link: https://www.codewars.com/kata/multiply/train/python

```python
"""Submitted by bit2pixel."""
multiply = lambda x, y: x * y

```


### 2.  Reverse words if longer than 4 letters. (Kyu 6)
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

### 3.  Validate a 4 or 6 digit pin number. (Kyu 7)
##### - Module: validate_pin.py
##### - Tests: test_validate_pin.py
##### - Link: https://www.codewars.com/kata/regex-validate-pin-code/train/python

```python
"""Submitted by suic."""

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

```

### 4.  Convert string to Jaden Case. (Kyu 7)
##### - Module: to_jaden_case.py
##### - Tests: test_to_jaden_case.py
##### - Link: https://www.codewars.com/kata/jaden-casing-strings/train/python

```python
"""Submitted by Azuaron."""

def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())

```

### 5.  Calculate needed years to achieve investment goals. (Kyu 7)
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

### 6.  Determine if three sides can make a triangle. (Kyu 7)
##### - Module: is_triangle.py
##### - Tests: test_is_triangle.py
##### - Link: https://www.codewars.com/kata/is-this-a-triangle/train/python

```python
"""Submitted by PilgrimShadow."""

def is_triangle(a, b, c):
  return abs(a-b) < c < a+b

```

### 7.  Return sorted string with unique elements from two input strings. (Kyu 7)
##### - Module: longest.py
##### - Tests: test_longest.py
##### - Link: https://www.codewars.com/kata/two-to-one/train/python

```python
"""Submitted by Staticor."""

def longest(s1, s2):
    return ''.join(sorted((set(s1+s2))))

```

### 8.  Return sum of all numbers in a string. (Kyu 7)
##### - Module: sum_from_string.py
##### - Tests: test_sum_from_string.py
##### - Link: https://www.codewars.com/kata/sum-up-the-random-string/train/python

```python
"""Submitted by JustyFY."""

import re
def sum_from_string(string):
    d = re.findall("\d+",string)
    return sum(int(i) for i in d)

```

### 9.  Return the nth value in the series. (Kyu 7)
##### - Module: sum_terms.py
##### - Tests: test_sum_terms.py
##### - Description: Return the nth value in a series.  The 0th value is 0
#####   the 1st value is 1 and the rest is iterative, each time adding 1/(1+(3*n))


### 10.  Determine if input string has valid parentheses.
##### - Module: parenthetics.py
##### - Test: test_parenthetics.py
##### - Description: Return 0 if input string has proper parenthetics.
#####               Return 1 if it has unclosed open paren
#####               Return -1 if it has unopened close paren.

### 11.  Return a sorted deck of cards.
##### - Module: sort_cards.py
##### - Test: test_sort_cards.py
##### - Description: Return a sorted list of cards given an input deck based on rank (Ace low).