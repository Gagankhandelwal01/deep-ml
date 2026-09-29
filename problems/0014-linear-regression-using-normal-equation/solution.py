
import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	x = np.array(X)
	y = np.array(y)

	transpose = x.T
	xTx = transpose @ x

	inverse = np.linalg.inv(xTx)
	coff = inverse @ transpose @ y

	theta = np.round(coff, 4).tolist()
	return theta