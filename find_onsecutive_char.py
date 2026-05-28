"""
=================================================
CONSECUTIVE CHARACTER COUNTER
=================================================

Problem Statement:
Write a Python program to count the maximum number
of consecutive occurrences of the same character
in a string.

-------------------------------------------------
Instructions:
1. Take a string as input.
2. Use a for loop.
3. Find the longest consecutive repeating character.
4. Print:
   - character
   - count

-------------------------------------------------
Input Example:
aaabbccccdde

Output Example:
Character: c
Count: 4

-------------------------------------------------
Explanation:
a -> 3 times
b -> 2 times
c -> 4 times
d -> 2 times
e -> 1 time

Highest consecutive count:
c -> 4

-------------------------------------------------
Hints:
1. Compare current character with previous character.
2. Keep track of:
   - current count
   - maximum count
3. Update maximum when needed.

-------------------------------------------------
Expected Concepts:
- Don't use dictionary.
- for loops
- string indexing
- operators
- conditional statements
- logical thinking

=================================================
"""

s = input("Enter a string: ")
max_char = s[0]
max_count = 1

current_char = s[0]
current_count = 1
for i in range(1, len(s)):
    if s[i] == current_char:
        current_count += 1
    else:
        current_char = s[i]
        current_count = 1
    if current_count > max_count:
        max_count = current_count
        max_char = current_char
print("Character:", max_char)
print("Count:", max_count)
