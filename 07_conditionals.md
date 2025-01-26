
### Exercises: Level 1

1. **User Input for Age**

```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")
```

2. **Compare Ages**

```python
my_age = 25  # Example age
your_age = int(input("Enter your age: "))

if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {difference} years older than you.")
else:
    print("We are the same age.")
```

3. **Compare Two Numbers**

```python
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")
```

### Exercises: Level 2

1. **Grade Students Based on Scores**

```python
score = int(input("Enter the student's score: "))

if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 79:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
else:
    print("Grade: F")
```

2. **Check the Season**

```python
month = input("Enter the month: ").strip().capitalize()

if month in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif month in ['December', 'January', 'February']:
    print("The season is Winter.")
elif month in ['March', 'April', 'May']:
    print("The season is Spring.")
elif month in ['June', 'July', 'August']:
    print("The season is Summer.")
else:
    print("Invalid month.")
```

3. **Check and Modify Fruit List**

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").strip().lower()

if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print(f"Updated fruit list: {fruits}")
```

### Exercises: Level 3

1. **Person Dictionary Tasks**

```python
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if 'skills' key exists
if 'skills' in person:
    # Print the middle skill
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print(f"Middle skill: {middle_skill}")

    # Check if 'Python' skill exists
    has_python = 'Python' in skills
    print(f"Has Python skill: {has_python}")

    # Check developer type
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer.")
    elif set(skills) == {'Node', 'Python', 'MongoDB'}:
        print("He is a backend developer.")
    elif set(skills) >= {'React', 'Node', 'MongoDB'}:
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")

# Check if married and lives in Finland
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
```
