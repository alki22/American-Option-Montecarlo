import numpy as np
from scipy.optimize import curve_fit


def Z(T,n):
	# Returns Z ~ N(0, sqrt(T/n))
	return np.random.normal(0, np.sqrt(T / n))
	return 0


def functional_relation(St, a, b, c):
	return a + b * St + c * (St ** 2)


def Montecarlo(S0, r, sigma, T, n, N, K):
	# Initialization
	prices_table = np.zeros(shape=(N, n))
	payoffs_table = np.zeros(shape=(N, n))

	for i in range(N):
		prices_table[i][0] = S0

	# Fill with Sj values
	for i in range(N):
		for j in range(1, n):
			# Fill using brownian motion recursive definition
			prices_table[i][j] = prices_table[i][j - 1] * np.e ** ((r - (sigma**2)) * T / n + sigma * Z(T,n))

	# Fill the n-th column with exercise values
	for i in range(N):
		St = prices_table[i][n-1]
		prices_table[i][n - 1] = np.maximum(K - St, 0)

	strike_vector = np.full((1, N), K)

	# Define columns n-1, n-2, ..., 1 
	for i in range(n - 2, 0, -1):
		payoff = strike_vector - prices_table[:, i]
		zeros_vector = np.zeros(shape=(1, N))
		
		payoffs_table[:, i] = np.maximum(zeros_vector, payoff)[0]
		indices = np.where(payoffs_table[:, i] > 0.0)

		if np.size(indices) > 0:
			x_data = prices_table[indices, i][0]
			y_data = payoffs_table[indices, i][0]
			
			# Get optimum values for a, b and c that minimize functional_relation with the given data
			opt_values = curve_fit(functional_relation, x_data, y_data)[0]

			Vt = functional_relation(x_data, opt_values[0], opt_values[1], opt_values[2])
			maximums = np.maximum(Vt, y_data)
			indices = np.where(maximums != y_data)

	# Set the next periods value to zero if option is exercised
	if np.size(indices) > 0:
		payoffs_table[indices, j] = 0

	# Set X to the mean value of the first column elements
	X = np.mean(payoffs_table[:, 1]) * (np.e ** (-r))
	# Get the bonus price
	bonus = np.maximum(K - S0, X)

	print bonus

Montecarlo(36., 0.06, 0.2, 1., 50, 20000, 38)
"""
Montecarlo(36, 0.06, 0.2, 1., 50, 20000, 38.)
Montecarlo(36, 0.06, 0.2, 1., 50, 20000, 40.)
Montecarlo(36, 0.06, 0.2, 1., 50, 20000, 42.)
Montecarlo(36, 0.06, 0.2, 1., 50, 20000, 44.)
"""