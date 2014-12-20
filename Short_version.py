lines = open(raw_input("Name of the file: ")).read().splitlines()
file = open(raw_input("Name of the new file: "), "w")
for line in lines:
	if line.startswith('#'):
		del line
	else:
		file.write(line)
		file.write('\n')
