'''
A list of three numbers in any order is given as input and
returns True if the list satisfies: h**2 = b**2 + p**2 for h, p and b 
in the list else returns False.
'''

def pythagorian_pair(pair):
	is_pair = False
	sorted_pair = sorted(pair)
	if sorted_pair[2]**2 == sorted_pair[1]**2 + sorted_pair[0]**2:
		is_pair = True
	return is_pair

