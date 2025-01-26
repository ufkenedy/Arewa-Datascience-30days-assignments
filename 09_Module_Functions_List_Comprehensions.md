### Exercises: Level 1

1. **Function to Add Two Numbers**

```python
def add_two_numbers(a, b):
    return a + b
```

2. **Function to Calculate Area of a Circle**

```python
import math

def area_of_circle(r):
    return math.pi * r * r
```

3. **Function to Add All Numbers**

```python
def add_all_nums(*args):
    if not all(isinstance(i, (int, float)) for i in args):
        return "All items must be numbers"
    return sum(args)
```

4. **Function to Convert Celsius to Fahrenheit**

```python
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
```

5. **Function to Check Season**

```python
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'
```

6. **Function to Calculate Slope**

```python
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
```

7. **Function to Solve Quadratic Equation**

```python
import cmath

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return root1, root2
```

8. **Function to Print List**

```python
def print_list(lst):
    for item in lst:
        print(item)
```

9. **Function to Reverse List**

```python
def reverse_list(lst):
    reversed_list = []
    for item in reversed(lst):
        reversed_list.append(item)
    return reversed_list
```

10. **Function to Capitalize List Items**

```python
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]
```

11. **Function to Add Item to List**

```python
def add_item(lst, item):
    lst.append(item)
    return lst
```

12. **Function to Remove Item from List**

```python
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
```

13. **Function to Sum Numbers in a Range**

```python
def sum_of_numbers(n):
    return sum(range(n + 1))
```

14. **Function to Sum Odd Numbers**

```python
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)
```

15. **Function to Sum Even Numbers**

```python
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)
```

### Exercises: Level 2

1. **Function to Count Evens and Odds**

```python
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."
```

2. **Function to Calculate Factorial**

```python
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

3. **Function to Check if Empty**

```python
def is_empty(param):
    return not param
```

4. **Functions for Statistical Calculations**

```python
import statistics

def calculate_mean(lst):
    return statistics.mean(lst)

def calculate_median(lst):
    return statistics.median(lst)

def calculate_mode(lst):
    return statistics.mode(lst)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    return statistics.variance(lst)

def calculate_std(lst):
    return statistics.stdev(lst)
```

### Exercises: Level 3

1. **Function to Check if Prime**

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

2. **Function to Check Unique Items**

```python
def all_unique(lst):
    return len(lst) == len(set(lst))
```

3. **Function to Check Data Types**

```python
def all_same_type(lst):
    return len(set(type(item) for item in lst)) == 1
```

4. **Function to Check Valid Python Variable Name**

```python
import keyword

def is_valid_variable(var):
    return var.isidentifier() and not keyword.iskeyword(var)
```
