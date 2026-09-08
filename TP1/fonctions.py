def puissance(a,b):
	if not type(a) is int or not type(b) is int:
		raise TypeError("Nombres entiers seulement")
	try:
		return a**b
	except ZeroDivisionError:
		return ("0^"+str(b)+" est indéfini.")
