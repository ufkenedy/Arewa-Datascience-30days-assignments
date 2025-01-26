
### Creating and Modifying Dictionaries

1. **Create an empty dictionary called `dog`**

```python
dog = {}
```

2. **Add name, color, breed, legs, age to the `dog` dictionary**

```python
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
```

3. **Create a `student` dictionary and add various keys**

```python
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'Java'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main Street'
}
```

4. **Get the length of the `student` dictionary**

```python
length_of_student_dict = len(student)
print(length_of_student_dict)
```

5. **Get the value of `skills` and check the data type**

```python
skills = student['skills']
print(skills)
print(type(skills))  # Should be <class 'list'>
```

6. **Modify the `skills` values by adding one or two skills**

```python
student['skills'].extend(['C++', 'JavaScript'])
print(student['skills'])
```

7. **Get the dictionary keys as a list**

```python
keys_list = list(student.keys())
print(keys_list)
```

8. **Get the dictionary values as a list**

```python
values_list = list(student.values())
print(values_list)
```

9. **Change the dictionary to a list of tuples using `items()` method**

```python
student_items = list(student.items())
print(student_items)
```

10. **Delete one of the items in the dictionary**

```python
del student['address']
print(student)
```

11. **Delete one of the dictionaries**

```python
del dog
# Attempting to print 'dog' will raise an error as it no longer exists
```
