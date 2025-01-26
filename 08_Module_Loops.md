### Exercises: Level 1

1. **Iterate 0 to 10 using for loop and while loop**

```python
# Using for loop
for i in range(11):
    print(i)

# Using while loop
i = 0
while i <= 10:
    print(i)
    i += 1
```

2. **Iterate 10 to 0 using for loop and while loop**

```python
# Using for loop
for i in range(10, -1, -1):
    print(i)

# Using while loop
i = 10
while i >= 0:
    print(i)
    i -= 1
```

3. **Print a triangle pattern**

```python
for i in range(1, 8):
    print('#' * i)
```

4. **Create a grid pattern using nested loops**

```python
for _ in range(8):
    for _ in range(8):
        print('#', end=' ')
    print()
```

5. **Print multiplication pattern**

```python
for i in range(11):
    print(f"{i} x {i} = {i * i}")
```

6. **Iterate through a list and print items**

```python
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)
```

7. **Print only even numbers from 0 to 100**

```python
for i in range(0, 101, 2):
    print(i)
```

8. **Print only odd numbers from 0 to 100**

```python
for i in range(1, 101, 2):
    print(i)
```

### Exercises: Level 2

1. **Sum of all numbers from 0 to 100**

```python
total_sum = sum(range(101))
print(f"The sum of all numbers is {total_sum}.")
```

2. **Sum of all evens and odds from 0 to 100**

```python
even_sum = sum(range(0, 101, 2))
odd_sum = sum(range(1, 101, 2))
print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")
```

### Exercises: Level 3


2. **Reverse a fruit list using a loop**

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for fruit in reversed(fruits):
    reversed_fruits.append(fruit)

print(reversed_fruits)
```
