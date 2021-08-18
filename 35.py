def search_id(A, left, ):
	if right < left:
		return -1
  
	middle = (left + right) // 2
	if A[middle] == A.index(A[middle]):
		return A.index(A[middle])
	else:
		return search_id(A, left, middle - 1)

A = [0, 1, 2, 3, 4, 5, 6, 8, 10]
print(search_id(A, 0, len(A) - 1))

A = [0, 1, 2, 6, 8, 10]
print(search_id(A, 0, len(A) - 1))

A = [1, 3, 4, 5, 6, 8, 10]
print(search_id(A, 0, len(A) - 1))
