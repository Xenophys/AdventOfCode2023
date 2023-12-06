def readfile(filename, strip_lines=True):
	with open(filename, 'r') as prov_file:
		if strip_lines:
			return [line.strip() for line in prov_file.readlines()]
		else:
			return prov_file.readlines()