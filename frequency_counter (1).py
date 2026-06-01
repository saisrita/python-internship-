"""
## 1. Count Frequency of Elements in a List  *(Easy)*

=================================================
ELEMENT FREQUENCY COUNTER
=================================================

Problem Statement:
Write a Python program that takes a list of
elements as input and counts how many times
EACH unique element appears in the list.
Store the result in a DICTIONARY where:
   - key   -> the element
   - value -> its frequency

-------------------------------------------------
Input Example 1:
['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

Output Example 1:
{'apple': 3, 'banana': 2, 'orange': 1}

-------------------------------------------------
Input Example 2:
[1, 2, 2, 3, 3, 3]

Output Example 2:
{1: 1, 2: 2, 3: 3}

-------------------------------------------------
Explanation:
For ['apple', 'banana', 'apple', 'orange',
     'banana', 'apple']:
   apple  -> 3 times
   banana -> 2 times
   orange -> 1 time
Result -> {'apple': 3, 'banana': 2, 'orange': 1}
=================================================

"""
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}
for item in elements:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(frequency)
