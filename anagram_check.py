"""
## 5. Check if Two Strings are Anagrams (*Hard*)

=================================================
ANAGRAM CHECK
=================================================

Problem Statement:
Write a Python program that takes TWO strings
as input and checks whether they are ANAGRAMS
of each other.

Two strings are anagrams if they contain the
exact same characters with the same frequency,
just in a different order. The check must be
case-insensitive and should ignore spaces.

-------------------------------------------------
Instructions:
1. Take two strings as input.
2. Convert both strings to lowercase and
   remove all spaces using a for loop
   (do NOT use str.replace()).
3. If their lengths are different, they cannot
   be anagrams.
4. Do NOT use:
   - sorted() or .sort()
   - dictionaries
   - sets
   - collections.Counter
   - str.count()
5. Print:
   - "Anagram" or "Not Anagram"

-------------------------------------------------
Input Example 1:
String 1: Listen
String 2: Silent

Output Example 1:
Anagram

-------------------------------------------------
Input Example 2:
String 1: Hello
String 2: World

Output Example 2:
Not Anagram

-------------------------------------------------
Explanation:
"Listen" -> "listen"
"Silent" -> "silent"
Both have the same characters with the same
frequency (l, i, s, t, e, n) -> Anagram.

"Hello" and "World" do not contain the same
characters, so they are Not Anagram.
=================================================

"""
s1 = input("String 1: ")
s2 = input("String 2: ")
str1 = ""
for ch in s1:
    if ch != " ":
        str1 += ch.lower()

str2 = ""
for ch in s2:
    if ch != " ":
        str2 += ch.lower()

if len(str1) != len(str2):
    print("Not Anagram")
else:
    anagram = True

    for ch in str1:
        c1 = 0
        c2 = 0

        for x in str1:
            if x == ch:
                c1 += 1

        for x in str2:
            if x == ch:
                c2 += 1

        if c1 != c2:
            anagram = False
            break

    if anagram:
        print("Anagram")
    else:
        print("Not Anagram")
