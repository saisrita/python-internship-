"""
## 1. Count Vowels in a String

=================================================
VOWEL COUNTER
=================================================

Problem Statement:
Write a Python program that takes a string as
input and counts how many vowels (a, e, i, o, u)
it contains. The check must be case-insensitive.

-------------------------------------------------
Instructions:
1. Take a string as input.
2. Use a for loop to traverse each character.
3. Treat uppercase and lowercase vowels as same.
4. Print:
   - total vowel count

Note: use ASCII  check for letters, and compare. 'e', 'i', 'o', '

-------------------------------------------------
Input Example:
Hello World

Output Example:
Vowel Count: 3

-------------------------------------------------
Explanation:
H e l l o   W o r l d
  ^       ^       ^
'e', 'o', 'o' are vowels -> 3 vowels.
=================================================

"""
text = input("Enter a string: ")
count = 0
for ch in text:
    if 'A' <= ch <= 'Z':
        ch = chr(ord(ch) + 32)
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1
print("Vowel Count:", count)
