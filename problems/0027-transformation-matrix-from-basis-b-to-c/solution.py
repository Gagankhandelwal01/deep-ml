import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	B = np.array(B)
	C = np.array(C)
	c_inv = np.linalg.inv(C)
	P = c_inv @ B
	P = P.tolist()
	return P