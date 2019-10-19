from operator import floordiv, mod

def div(n, d):
	"""
	Try doctest

	>>> q,r = div(2013, 10)
	>>> q
	201
	>>> r
	3
	"""
	return floordiv(n,d), mod(n, d)
