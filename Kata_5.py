"""
Ejercicio 1: 
Return the Sum of the Two Smallest Numbers

Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.
Examples

[19, 5, 42, 2, 77] ➞ 7

[10, 343445353, 3453445, 3453545353453] ➞ 3453455

[2, 9, 6, -1] ➞ 8

[879, 953, 694, -847, 342, 221, -91, -723, 791, -587] ➞ 563

[3683, 2902, 3951, -475, 1617, -2385] ➞ 4519

Notes

    Don't count negative numbers.
    Floats and empty lists will not be used in any of the test cases.
"""
#---------------------------Code-----------------------------------------
def sum_two_smallest_nums(lst):
	num1 = lst[0]
	num2 = lst[1]
	for i in range(2, len(lst)):
		if lst[i] < 0: continue
		elif num1 < 0:
			num1 = lst[i]
		elif num2 < 0:
			num2 = lst[i]
		elif lst[i] >= num1 and lst[i] >= num2: continue
		elif lst[i] <= num1:
			if num1 < num2:
				num2 = lst[i]
			else:
				num1 = lst[i]
		else:
			if num2 < num1:
				num1 = lst[i]
			else:
				num2 = lst[i]
	return num1+num2
