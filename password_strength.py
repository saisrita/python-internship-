"""
=================================================
PASSWORD STRENGTH CHECKER
=================================================

Problem Statement:
Write a Python program to check password strength.

-------------------------------------------------
Conditions:
A password is strong if:
1. Length is at least 8
2. Contains at least one digit
3. Contains at least one uppercase letter

-------------------------------------------------
Instructions:
1. Take password input from user.
2. Use loops and conditional statements.
3. Print:
   - "Strong Password"
   - "Weak Password"

-------------------------------------------------
Input Example:
Python123

Output Example:
Strong Password

-------------------------------------------------
Hints:
Use:
isdigit()
isupper()

-------------------------------------------------
Expected Concepts:
- loops
- string functions
- operators
- conditional statements

=================================================
"""

# Write your code below this line
assword = input("Enter password: ")

has_digit = False
has_upper = False 

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

if len(password) >= 8 and has_digit and has_upper:
    print("Strong Password")
else:
    print("Weak Password")
