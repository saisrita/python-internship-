"""
=================================================
ELECTRICITY BILL CALCULATOR
=================================================

Problem Statement:
Write a Python program to calculate electricity bill.

-------------------------------------------------
Conditions:
1. First 100 units  -> ₹5 per unit
2. Next 100 units   -> ₹7 per unit
3. Above 200 units  -> ₹10 per unit


-------------------------------------------------
Input Example:
250

Output Example:
Total Bill = ₹1700

-------------------------------------------------
Hints:
Break the problem into multiple conditions.

=================================================
"""

# # Electricity Bill Calculator

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Total Bill = ₹", bill)Write your code below this line
