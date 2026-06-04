"""
## 2. Filter Long Words and Convert to Uppercase  *(Easy)*

=================================================
LONG WORDS TO UPPERCASE
=================================================

Problem Statement:
Write a Python program that takes a list of
strings and returns a TUPLE of two values:
   1. a list of words whose length is greater
      than 4, all converted to UPPERCASE
   2. a set of unique FIRST letters of those
      long words (also uppercase)

You MUST use lambda, filter(), and map().


-------------------------------------------------
Input Example:
["apple", "kiwi", "banana", "fig", "orange", "pear"]

Output Example:
Long Words: ['APPLE', 'BANANA', 'ORANGE']
First Letters: {'A', 'B', 'O'}

-------------------------------------------------
Explanation:
filter (len > 4)  -> ['apple', 'banana', 'orange']
map    (upper)    -> ['APPLE', 'BANANA', 'ORANGE']
First letters set -> {'A', 'B', 'O'}
=================================================

"""
words = ["apple", "kiwi", "banana", "fig", "orange", "pear"]

long_words = list(filter(lambda x: len(x) > 4, words))

uppercase_words = list(map(lambda x: x.upper(), long_words))
first_letters = set(map(lambda x: x[0], uppercase_words))

print("Long Words:", uppercase_words)
print("First Letters:", first_letters)
