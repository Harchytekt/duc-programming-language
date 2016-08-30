
def isFloat(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

print isFloat("2.0")