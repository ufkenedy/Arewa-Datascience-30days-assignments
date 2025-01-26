
```python
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# Unpacking the first five countries into nordic_countries and the rest into es and ru
*nordic_countries, es, ru = names[:5], names[5], names[6]

print(nordic_countries)  # Output: ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
print(es)               # Output: 'Estonia'
print(ru)               # Output: 'Russia'
```

This code unpacks the first five countries into the `nordic_countries` list and assigns 'Estonia' and 'Russia' to the variables `es` and `ru`, respectively.
