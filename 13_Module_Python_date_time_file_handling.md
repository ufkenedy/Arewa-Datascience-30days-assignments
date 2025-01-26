### Exercises: Level 1

1. **Count Number of Lines and Words in Text Files**

   Here's a function to count lines and words in a text file:

   ```python
   def count_lines_and_words(filename):
       with open(filename, 'r', encoding='utf-8') as file:
           lines = file.readlines()
           num_lines = len(lines)
           num_words = sum(len(line.split()) for line in lines)
       return num_lines, num_words

   # Example usage:
   print(count_lines_and_words('data/obama_speech.txt'))
   print(count_lines_and_words('data/michelle_obama_speech.txt'))
   print(count_lines_and_words('data/donald_speech.txt'))
   print(count_lines_and_words('data/melina_trump_speech.txt'))
   ```

2. **Find Ten Most Spoken Languages**

   ```python
   import json
   from collections import Counter

   def most_spoken_languages(filename, top_n):
       with open(filename, 'r', encoding='utf-8') as file:
           data = json.load(file)
           languages = [language for country in data for language in country['languages']]
           language_counts = Counter(languages)
           return language_counts.most_common(top_n)

   # Example usage:
   print(most_spoken_languages('data/countries_data.json', 10))
   print(most_spoken_languages('data/countries_data.json', 3))
   ```

3. **Find Ten Most Populated Countries**

   ```python
   def most_populated_countries(filename, top_n):
       with open(filename, 'r', encoding='utf-8') as file:
           data = json.load(file)
           sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
           return [{'country': country['name'], 'population': country['population']} for country in sorted_countries[:top_n]]

   # Example usage:
   print(most_populated_countries('data/countries_data.json', 10))
   print(most_populated_countries('data/countries_data.json', 3))
   ```

### Exercises: Level 2

1. **Extract All Incoming Email Addresses**

   ```python
   import re

   def extract_email_addresses(filename):
       with open(filename, 'r', encoding='utf-8') as file:
           text = file.read()
           emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
       return emails

   # Example usage:
   emails = extract_email_addresses('data/email_exchange_big.txt')
   print(emails)
   ```

2. **Find Most Common Words**

   ```python
   def find_most_common_words(filename, top_n):
       with open(filename, 'r', encoding='utf-8') as file:
           text = file.read()
           words = re.findall(r'\w+', text.lower())
           word_counts = Counter(words)
           return word_counts.most_common(top_n)

   # Example usage:
   print(find_most_common_words('data/sample.txt', 10))
   print(find_most_common_words('data/sample.txt', 5))
   ```

3. **Most Frequent Words in Speeches**

   ```python
   def find_most_frequent_words_in_speech(speech_file, top_n=10):
       return find_most_common_words(speech_file, top_n)

   # Example usage:
   print(find_most_frequent_words_in_speech('data/obama_speech.txt'))
   print(find_most_frequent_words_in_speech('data/michelle_obama_speech.txt'))
   print(find_most_frequent_words_in_speech('data/donald_speech.txt'))
   print(find_most_frequent_words_in_speech('data/melina_trump_speech.txt'))
   ```

4. **Check Similarity Between Two Texts**

   implement several functions for this:

   ```python
   def clean_text(text):
       return re.sub(r'[^\w\s]', '', text).lower()

   def remove_support_words(text, stop_words_file):
       with open(stop_words_file, 'r', encoding='utf-8') as file:
           stop_words = set(file.read().split())
           words = text.split()
           return ' '.join(word for word in words if word not in stop_words)

   def check_text_similarity(text1, text2):
       words1 = set(text1.split())
       words2 = set(text2.split())
       intersection = words1.intersection(words2)
       union = words1.union(words2)
       return len(intersection) / len(union)

   # Example usage:
   text1 = clean_text(open('data/michelle_obama_speech.txt').read())
   text2 = clean_text(open('data/melina_trump_speech.txt').read())
   text1 = remove_support_words(text1, 'data/stop_words.txt')
   text2 = remove_support_words(text2, 'data/stop_words.txt')
   similarity = check_text_similarity(text1, text2)
   print(f"Similarity: {similarity:.2f}")
   ```

5. **Find 10 Most Repeated Words in Romeo and Juliet**

   ```python
   print(find_most_common_words('data/romeo_and_juliet.txt', 10))
   ```

6. **Read Hacker News CSV File**

   ```python
   import csv

   def count_lines_containing(filename, *keywords):
       with open(filename, 'r', encoding='utf-8') as file:
           reader = csv.reader(file)
           count = 0
           for line in reader:
               line_text = ' '.join(line).lower()
               if all(keyword.lower() in line_text for keyword in keywords):
                   count += 1
           return count

   # Example usage:
   python_count = count_lines_containing('data/hacker_news.csv', 'python')
   javascript_count = count_lines_containing('data/hacker_news.csv', 'javascript')
   java_count = count_lines_containing('data/hacker_news.csv', 'java')
   java_not_javascript_count = java_count - javascript_count

   print(f"Lines containing Python: {python_count}")
   print(f"Lines containing JavaScript: {javascript_count}")
   print(f"Lines containing Java and not JavaScript: {java_not_javascript_count}")
   ```
