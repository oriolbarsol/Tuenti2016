import sys
#words split text
words = {}
def main():
	#load document and split words in memory
	load_words(sys.argv[1])
	#input file
	load_input(sys.argv[2])

def load_words(fl):
	count = 0
	with open(fl,'r') as f:
	    for line in f:
	        for word in line.split():
	        	count += 1
	        	words[count] = word

def load_input(fl):
	#reading the input file

	fileInput = open(fl)
	case = 0
	#skip firstline the number of cases
	fileInput.readline()
	#read each line
	for key in fileInput.readlines():
		#position of words to count
		start = key.split()[0]
		end = key.split()[1]
		#count words
		wordsCount = count_words(int(start), int(end))
		case += 1
		#order and print the output
		order_print(wordsCount, case)


def count_words(startWord, endWord):
	output = {}
	position = startWord
	#count all words in the range
	while position != endWord:
		position += 1
		word = words[position]
		#if exist sum 1 to the count
		if word in output:
			output[word] += 1
		else:
			output[word] = 1
	return output

def order_print(words, case):
	outuputString = str('Case #'+str(case)+': ')
	count = 0
	#order all words by freq
	for key, value in sorted(words.iteritems(), key=lambda (k,v): (v,k),reverse=True):
   		count+=1
   		#just the 3 firts
		if count == 3:
			outuputString += str(key) + ' ' + str(value)
			break
		else:
			outuputString += str(key) +' '+ str(value) + ','
	#output the result
	print outuputString

if __name__ == '__main__':
	main()
