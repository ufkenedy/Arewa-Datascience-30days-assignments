
### Exercises: Level 1

1. **Generate a Six Digit/Character `random_user_id`**

   ```python
   import random
   import string

   def random_user_id():
       return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

   print(random_user_id())  # Example output: '1ee33d'
   ```

2. **Function `user_id_gen_by_user`**

   ```python
   def user_id_gen_by_user():
       num_chars = int(input("Enter number of characters: "))
       num_ids = int(input("Enter number of IDs: "))
       ids = [''.join(random.choices(string.ascii_letters + string.digits, k=num_chars)) for _ in range(num_ids)]
       return ids

   # Example usage:
   print(user_id_gen_by_user())  # Try inputting: 5 5 or 16 5
   ```

3. **Function `rgb_color_gen`**

   ```python
   def rgb_color_gen():
       return f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"

   print(rgb_color_gen())  # Example output: 'rgb(125,244,255)'
   ```

### Exercises: Level 2

1. **Function `list_of_hexa_colors`**

   ```python
   def list_of_hexa_colors(n):
       return ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(n)]

   print(list_of_hexa_colors(3))  # Example output: ['#a3e12f', '#03ed55', '#eb3d2b']
   ```

2. **Function `list_of_rgb_colors`**

   ```python
   def list_of_rgb_colors(n):
       return [rgb_color_gen() for _ in range(n)]

   print(list_of_rgb_colors(3))  # Example output: ['rgb(5,55,175)', 'rgb(50,105,100)', 'rgb(15,26,80)']
   ```

3. **Function `generate_colors`**

   ```python
   def generate_colors(color_type, n):
       if color_type == 'hexa':
           return list_of_hexa_colors(n)
       elif color_type == 'rgb':
           return list_of_rgb_colors(n)
       else:
           raise ValueError("Color type must be 'hexa' or 'rgb'.")

   print(generate_colors('hexa', 3))  # Example output: ['#a3e12f', '#03ed55', '#eb3d2b']
   print(generate_colors('rgb', 1))   # Example output: ['rgb(33,79,176)']
   ```

### Exercises: Level 3

1. **Function `shuffle_list`**

   ```python
   def shuffle_list(lst):
       random.shuffle(lst)
       return lst

   # Example usage:
   print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Example: [3, 9, 1, 7, 5, 2, 6, 8, 4]
   ```

2. **Function to Generate Seven Unique Random Numbers**

   ```python
   def unique_random_numbers():
       return random.sample(range(10), 7)

   print(unique_random_numbers())  # Example output: [2, 8, 9, 1, 3, 7, 5]
   ```
