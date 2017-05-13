
"""
Suppose we have very large sparse vectors, which contains a lot of zeros and double .
find a data structure to store them
get the dot product of them
In this case, we first have to store the sparse vector using hash map.
for example [3,0,0,5,6] -> (0,3) (3,5) (4,6) The key is each element's position and the value is the number.
Then we have two hash tables, and we have to iterate through them to calculate the dot product
"""

import random
import numpy as np

def sparse_dot_vector(sparse_vec1, sparse_vec2):
	hash_table1 = [(key, value) for key, value in zip(list(range(len(sparse_vec1))), sparse_vec1) if value != 0]
	hash_table2 = [(key, value) for key, value in zip(list(range(len(sparse_vec2))), sparse_vec2) if value != 0]
	print("Lengths of hash tables 1 and 2 are: ", len(hash_table1), "and", len(hash_table2))

	for i in range(len(hash_table1)):
		for j in range(len(hash_table2)):
			if hash_table1[i][0] == hash_table2[j][0]:
				dot_sum += hash_table1[i][1]*hash_table2[j][1]
	return dot_sum	
	
	# TODO: double for loops during the summation - to calculate the dot product
	# out of two hash tables is inefficient.		
