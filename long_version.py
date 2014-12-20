#We first ask which file do we want to take off coments from
file = open(raw_input("Name of the file: "))

#Then we simply create a list that has all lines
data = file.read()
lines = data.splitlines()

#We choose or create the new file
file2 = open(raw_input("Name of the new file: "), "w")

#If a line starts with '#', it's removed. If not, is written into the new file.
for line in lines:
	if line.startswith('#'):
		del line
	else:
		file.write(line)
		file.write('\n')
