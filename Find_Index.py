Find the Index

Create a function that takes a list and a string as arguments and return the index of the string.

Examples
['hi', 'edabit', 'fgh', 'abc'], 'fgh' ➞ 2
['Red', 'blue', 'Blue', 'Green'], 'blue' ➞ 1
['a', 'g', 'y', 'd'], 'd' ➞ 3
['Pineapple', 'Orange', 'Grape', 'Apple'], 'Pineapple' ➞ 0

Notes
• Don't forget to return the result.
• All tests contain valid numbers.
• If you are stuck, find help in the Resources tab.
•The variable for list is lst, not 1st.

-----------------------------------CODE------------------------------------------
def find_index(lst, str):
	return lst.index(str)
