"""
Excercise 1: Find the Minimum, Maximum, Length and Average Values

Create a function that takes a list of numbers and returns the following statistics:

    Minimum Value
    Maximum Value
    Sequence Length
    Average Value

Examples

[6, 9, 15, -2, 92, 11] ➞ [-2, 92, 6, 21.833333333333332]

[30, 43, 20, 92, 3, 74] ➞ [3, 92, 6, 43.666666666666664]

[4.54, 8.32, 5.20] ➞ [4.54, 8.32, 3, 6.02]

Notes

N/A
"""
#---------------------------Code-----------------------------------------
def minMaxLengthAverage(lst):
	return [min(lst), max(lst), len(lst), (sum(lst) / len(lst))]
  
"""
Excercise 2: Filter out Strings from an Array

Create a function that takes a list of non-negative numbers / strings and returns a new list without the strings.
Example

[1, 2, "a", "b"] ➞ [1, 2]

[1, "a", "b", 0, 15] ➞ [1, 0, 15]

[1, 2, "aasf", "1", "123", 123] ➞ [1, 2, 123]

Notes

Zero is a non-negative number.
"""
#---------------------------Code-----------------------------------------
def filter_list(lst):
	return [i for i in lst if isinstance(i, int)]

"""
Excercise 3: Remove Duplicates from List

Create a function that takes a list of items, removes all duplicate items and returns a new list in the same sequential order as the old list (minus duplicates).
Examples

["John", "Taylor", "John"] ➞ ["John", "Taylor"]

[1, 0, 1, 0] ➞ [1, 0]

['The', 'big', 'cat'] ➞ ['The', 'big', 'cat']

Notes

    Test cases contain lists with both strings and numbers.
    Case sensitive.
"""
#---------------------------Code-----------------------------------------
def removeDups(lst):
	newList = []
	for i in lst:
		if i not in newList:
			newList.append(i)
	return newList
