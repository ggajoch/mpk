import fileinput


for line in fileinput.input():
	inp = line.split()
	for x in inp:
		print(int(x))
	
