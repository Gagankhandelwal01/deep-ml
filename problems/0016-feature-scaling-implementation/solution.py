import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	m = np.mean(data, axis=0)
	s = np.std(data, axis=0)
	standardized_data = (data - m) / s

	mini = np.min(data, axis=0)
	maxi = np.max(data, axis=0)
	normalized_data = (data - mini) / (maxi - mini)
	return standardized_data, normalized_data