import sys

def main():
	finalOutput = load_input(sys.argv[1])

def load_input(fl):
	#reading the input file
	output = {}
	fileInput = open(fl)
	case = 0
	#skip firstline the number of cases
	fileInput.readline()
	for key in fileInput.readlines():
		key = int(key)

		#just calc unique values
		if key not in output:
			value = calculate_tables(key)
			#adding values to check if unique
			output[key] = value
			case += 1
			print 'Case #'+str(case)+': '+str(value)



def calculate_tables(value):
	tables = 0
	#0 people 0 tables
	if value == 0:
		tables = 0
	# just 1 table?
	elif value >= 1 and value <= 4:
		tables = 1
	else:
		value = value-3;
		#the first table will seat 3 persons so we can rest that
		tables = value / 2
		#adding the 1 table
		tables += 1
		# if the rest of the division is 1 we can seat the person in the side of the last table


	return tables


if __name__ == '__main__':
	main()
