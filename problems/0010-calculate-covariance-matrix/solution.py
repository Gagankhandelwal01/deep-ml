import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	vectors = np.array(vectors)

	vectors = np.cov(vectors)
	vectors = vectors.tolist()
	return vectors