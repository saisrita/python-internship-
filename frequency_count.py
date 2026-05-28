"""
=================================================
CHARACTER FREQUENCY COUNTER
=================================================

Problem Statement:
Write a Python program to count how many times
a character appears in a string.

-------------------------------------------------
Instructions:
1. Take input from the user:
   - a string
   - a character
2. Use loop and conditional statements.
3. Print character count.

-------------------------------------------------
Input Example:
String: programming
Character: g

Output Example:
2
-------------------------------------------------
Expected Concepts:
- loops
- strings
- operators
- logical thinking

=================================================
"""

 s = input("Enter a string: ")
ch = input("Enter a character: ")
count = 0
for i in s:
    if i == ch:
        count += 1

print(count)Write your code below this line
