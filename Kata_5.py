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


"""
Ejercicio 2: 
Cumulative List Sum

Create a function that takes a list of numbers and returns a list where each number is the sum of itself + all previous numbers in the list.
Examples

[1, 2, 3] ➞ [1, 3, 6]

[1, -2, 3] ➞ [1, -1, 2]

[3, 3, -2, 408, 3, 3] ➞ [3, 6, 4, 412, 415, 418]

Notes

Return an empty list if the input is an empty list.
"""
#---------------------------Code-----------------------------------------
def cumulative_sum(lst):
	lista = [x for x in lst]
	for i in range(len(lst)):
		for j in range(0, i):
			lista[i]+=lst[j]
	return lista

"""
Ejercicio 3: 
Find the Minimum, Maximum, Length and Average Values

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
	return [min(lst), max(lst), len(lst), (sum(lst)/len(lst))]
