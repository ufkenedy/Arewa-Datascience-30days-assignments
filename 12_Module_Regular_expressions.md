
### Exercises: Level 1

1. **Most Frequent Word in the Paragraph**

   To find the most frequent word, we can use a dictionary to count occurrences of each word, then sort by frequency.

   ```python
   from collections import Counter

   paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

   # Normalize the paragraph by removing punctuation and converting to lowercase
   words = paragraph.replace('.', '').replace(',', '').lower().split()

   # Use Counter to count word frequencies
   word_count = Counter(words)

   # Sort by frequency
   most_common_words = word_count.most_common()

   print(most_common_words)
   ```

   This will output the list of words sorted by frequency, with "love" being the most frequent.

2. **Distance Between Furthest Particles**

   ```python
   points_text = '-12, -4, -3, -1, 0, 4, 8'
   points = list(map(int, points_text.split(', ')))

   # Sort and find the distance between the smallest and largest
   sorted_points = sorted(points)
   distance = sorted_points[-1] - sorted_points[0]

   print(sorted_points)  # Output: [-12, -4, -3, -1, 0, 4, 8]
   print(distance)       # Output: 20
   ```

### Exercises: Level 2

1. **Pattern for Valid Python Variable**

   A valid Python variable name starts with a letter or underscore, followed by letters, digits, or underscores.

   ```python
   import re

   def is_valid_variable(name):
       pattern = r'^[A-Za-z_]\w*$'
       return bool(re.match(pattern, name))

   print(is_valid_variable('first_name'))  # True
   print(is_valid_variable('first-name'))  # False
   print(is_valid_variable('1first_name'))  # False
   print(is_valid_variable('firstname'))  # True
   ```

### Exercises: Level 3

1. **Clean the Text and Find Most Frequent Words**

   ```python
   import re
   from collections import Counter

   sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

   def clean_text(text):
       # Remove special characters using regex
       cleaned_text = re.sub(r'[^\w\s]', '', text)
       return cleaned_text

   cleaned_sentence = clean_text(sentence)
   print(cleaned_sentence)

   # Count the most frequent words
   def most_frequent_words(text):
       words = text.split()
       word_count = Counter(words)
       return word_count.most_common(3)

   print(most_frequent_words(cleaned_sentence))
   ```

   This code will clean the sentence by removing special characters and count the three most frequent words, providing an output like:

   ```
   I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
   [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
   ```
