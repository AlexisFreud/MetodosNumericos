"""
Excercise 1: Is the Number Even or Odd?

Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.
Examples

3 ➞ "odd"

146 ➞ "even"

19 ➞ "odd"

Notes

    Dont forget to return the result.
    Input will always be a valid integer.
    Expect negative integers (whole numbers).
    Tests are case sensitive (return "even" or "odd" in lowercase).
    
"""
    
#----------------------------Code------------------------------------
def isEvenOrOdd(num):
	if num%2 == 0: return "even"
	else: return "odd"

"""
Excercise 2: Find the Smallest Number in a List

Create a function that takes a list of numbers and returns the smallest number in the list.
Examples

[34, 15, 88, 2] ➞ 2

[34, -345, -1, 100] ➞ -345

[-76, 1.345, 1, 0] ➞ -76

[0.4356, 0.8795, 0.5435, -0.9999] ➞ -0.9999

[7, 7, 7] ➞ 7

Notes

    Test cases contain decimals.
    If you get stuck on a challenge, find help in the Resources tab.
    If you're really stuck, unlock solutions in the Solutions tab.
    
"""
#----------------------------Code------------------------------------
def findSmallestNum(lst):
	return min(lst)

"""
Excercise 3: Eliminate Odd Numbers within a List

Create a function that takes a list of numbers and returns only the even values.
Examples

[1, 2, 3, 4, 5, 6, 7, 8] ➞ [2, 4, 6, 8]

[43, 65, 23, 89, 53, 9, 6] ➞ [6]

[718, 991, 449, 644, 380, 440] ➞ [718, 644, 380, 440]

Notes

    Return all even numbers in the order they were given.
    All test cases contain valid numbers ranging from 1 to 3000.
"""
#----------------------------Code------------------------------------
def noOdds(lst):
	newList = [i for i in lst if i%2 == 0]
	return newList
