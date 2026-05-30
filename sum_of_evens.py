"""
## 1. Sum of Even Numbers in a List  *(Easy)*

=================================================
SUM OF EVEN NUMBERS
=================================================

Problem Statement:
Write a Python program that takes a list of
integers as input and calculates the sum of
all EVEN numbers in the list.

-------------------------------------------------
Instructions:
1. Take a list of integers as input.
2. Use a for loop to traverse the list.
3. Use the modulo operator (%) to check
   whether a number is even (n % 2 == 0).
4. Maintain a running total of even numbers.
5. Do NOT use:
   - sum()
   - filter()
   - list comprehensions
6. Print:
   - the total sum

-------------------------------------------------
Input Example 1:
[1, 2, 3, 4, 5, 6]

Output Example 1:
Sum of Even Numbers: 12

-------------------------------------------------
Input Example 2:
[7, 11, 13]

Output Example 2:
Sum of Even Numbers: 0

-------------------------------------------------
Explanation:
For [1, 2, 3, 4, 5, 6]:
   even numbers -> 2, 4, 6
   sum          -> 2 + 4 + 6 = 12

For [7, 11, 13]:
   no even numbers, so the sum is 0.
=================================================

"""
numbers = eval(input())

even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum = even_sum + num

print("Sum of Even Numbers:", even_sum)
