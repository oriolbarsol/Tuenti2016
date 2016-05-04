import sys

combos = []
def main():

	load_combos()
	load_trainings(sys.argv[1])

def load_combos():
	#load combos
	combos.append(['L','LD','D','RD','R','P'])
	combos.append(['D','RD','R','P'])
	combos.append(['R','D','RD','P'])
	combos.append(['D','LD','L','K'])
	combos.append(['R','RD','D','LD','L','K'])

	#order combos by lenght
	combos.sort(lambda x,y: cmp(len(x), len(y)),reverse=True)

def load_trainings(fl):
	#proces each training

	with open(fl) as fileInput:
		fileInput.readline()
		lines = fileInput.readlines()
		count = 0
		for line in lines:
			count += 1
			result = train_combos(line)
			print 'Case #'+str(count)+': '+str(result)

def train_combos(line):
	lastFails = 0
	#
	cursor = 0
	#clean line
	line = line.lstrip()
	line = line.rstrip()
	#split each value
	values = line.split('-')
	#total lenght of the trainng
	lenghtValues = len(values)
	#control when miss a combo
	booleanControl = 0
	#the last char of last error, the next error must be greater than this
	lastCursor = 0
	while cursor < lenghtValues:
		#check all posible combos (ordered before)
		for combo in combos:
			lenght = len(combo)
			count = 0
			#loop al values of the combo and check if is the last value of the line
			while count < lenght and (cursor+count)<=lenghtValues:
				cursosTmp = cursor+count;
				#if is the last value or the values are diferent
				if ((cursosTmp) == lenghtValues) or values[cursosTmp] != combo[count]:
					#check if fail on the last move of the combo
					if count == (lenght-1) and (cursosTmp) > lastCursor:
						lastFails += 1
						#control vars
						booleanControl = 1
						lastCursor = cursosTmp
					break
				count += 1
			#the combos are ordered so if we find a fail we should break the loop
			if booleanControl == 1:
				booleanControl = 0
				break
		#next value
		cursor += 1
	return lastFails


if __name__ == '__main__':
	main()
