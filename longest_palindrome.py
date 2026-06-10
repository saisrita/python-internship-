"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""

with open("sowpods.txt", "r") as file:
    words = [line.strip().lower() for line in file]

palindromes = [word for word in words if word == word[::-1]]

if palindromes:
   
    max_length = max(len(word) for word in palindromes)


    longest_palindromes = [
        word for word in palindromes if len(word) == max_length
    ]

    print(f"Longest palindrome length: {max_length}")
    for word in sorted(longest_palindromes):
        print(word)
else:
    print("No palindrome words found.")
