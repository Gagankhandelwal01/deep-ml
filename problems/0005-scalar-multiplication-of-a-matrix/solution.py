def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	for i in matrix:
		for j in range(len(i)):
			i[j] *= scalar
	return matrix