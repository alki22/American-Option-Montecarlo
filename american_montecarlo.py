import numpy as np
from scipy.optimize import curve_fit

def Z(T,n):
	# Returns Z ~ N(0, sqrt(T/n))
	return np.random.normal(0, np.sqrt(T / n))
	return 0

def Montecarlo(s0, r, sigma, T, n, N, K):
	# Initialization
	table = np.zeros(shape=(N,n))
	for i in range(table.shape[0]):
		table[i][0] = s0

	# Fill with Sj values
	for i in range(N):
		for j in range(1, n): 
			table[i][j] = table[i][j - 1] * np.e ** ((r - (sigma**2)) * T / n + sigma * Z(T,n))