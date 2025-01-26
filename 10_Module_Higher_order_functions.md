### Exercises: Level 1

1. **Difference Between Map, Filter, and Reduce**

   - **Map**: Applies a given function to each item in an iterable (like a list) and returns a new iterable with the transformed items.
   - **Filter**: Applies a function to each item in an iterable and returns a new iterable containing only the items for which the function returns `True`.
   - **Reduce**: Applies a function cumulatively to the items of an iterable, reducing the iterable to a single value. It’s available in Python’s `functools` module.

2. **Difference Between Higher Order Function, Closure, and Decorator**

   - **Higher Order Function**: A function that takes one or more functions as arguments, or returns a function as its result.
   - **Closure**: A function object that remembers values in enclosing scopes even if they are not present in memory.
   - **Decorator**: A special type of higher-order function that modifies the behavior of another function or method.

3. **Call Function Before Map, Filter, or Reduce**

   These functions can be called directly by passing a function and an iterable. Example usage:

   ```python
   from functools import reduce

   # Example function to use with map
   def square(x):
       return x * x

   numbers = [1, 2, 3, 4, 5]
   squared_numbers = map(square, numbers)
   print(list(squared_numbers))  # [1, 4, 9, 16, 25]
   ```

4. **Print Each Country in Countries List**

   ```python
   countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
   for country in countries:
       print(country)
   ```

5. **Print Each Name in Names List**

   ```python
   names = ['Alice', 'Bob', 'Charlie']
   for name in names:
       print(name)
   ```

6. **Print Each Number in Numbers List**

   ```python
   numbers = [1, 2, 3, 4, 5]
   for number in numbers:
       print(number)
   ```

### Exercises: Level 2

1. **Map to Uppercase Countries**

   ```python
   countries_upper = list(map(str.upper, countries))
   print(countries_upper)
   ```

2. **Map to Square Numbers**

   ```python
   numbers_squared = list(map(lambda x: x**2, numbers))
   print(numbers_squared)
   ```

3. **Map to Uppercase Names**

   ```python
   names_upper = list(map(str.upper, names))
   print(names_upper)
   ```

4. **Filter Countries Containing 'land'**

   ```python
   countries_with_land = list(filter(lambda x: 'land' in x.lower(), countries))
   print(countries_with_land)
   ```

5. **Filter Countries with Exactly Six Characters**

   ```python
   countries_six_chars = list(filter(lambda x: len(x) == 6, countries))
   print(countries_six_chars)
   ```

6. **Filter Countries with Six or More Letters**

   ```python
   countries_six_or_more = list(filter(lambda x: len(x) >= 6, countries))
   print(countries_six_or_more)
   ```

7. **Filter Countries Starting with 'E'**

   ```python
   countries_starting_e = list(filter(lambda x: x.startswith('E'), countries))
   print(countries_starting_e)
   ```

8. **Chain List Iterators**

   ```python
   from functools import reduce

   result = reduce(lambda acc, x: acc + x, filter(lambda x: len(x) > 5, map(str.upper, countries)))
   print(result)
   ```

9. **Function to Get String Lists**

   ```python
   def get_string_lists(lst):
       return list(filter(lambda x: isinstance(x, str), lst))
   ```

10. **Reduce to Sum Numbers**

    ```python
    total_sum = reduce(lambda x, y: x + y, numbers)
    print(total_sum)
    ```

11. **Reduce to Concatenate Countries**

    ```python
    sentence = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ', and ' + countries[-1] + ' are north European countries'
    print(sentence)
    ```

12. **Function to Categorize Countries**

    ```python
    def categorize_countries(pattern):
        return [country for country in countries if pattern in country]
    ```

13. **Dictionary of Starting Letters of Countries**

    ```python
    def country_letter_dict(countries):
        letter_dict = {}
        for country in countries:
            letter = country[0]
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
        return letter_dict
    ```

14. **Get First Ten Countries**

    ```python
    def get_first_ten_countries():
        return countries[:10]
    ```

15. **Get Last Ten Countries**

    ```python
    def get_last_ten_countries():
        return countries[-10:]
    ```
