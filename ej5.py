import sys
import socket
import time

#words sorted by lenght
words={}

vowels = ['A', 'E', 'I', 'O', 'U']

#freq of the letter
freq_letter={}

#first vocal - we check vowels until we found one
isFirstVocal = 1
#letters used in each level
used_letter = []
#result of the last letter
last_result = []
from random import randint

def main():
	load_words(sys.argv[1])
	load_hang()

def load_words(fl):
	#loads words in memmory
	with open(fl) as fileInput:
		fileInput.readline()
		#segment words by lenght
		lines = fileInput.readlines()
		for line in lines:
			line = line.strip()
			lenght = len(line)

			if lenght in words:

				words[lenght].append(line)
			else:
				words[lenght] = [line]


def load_hang():

	#calc first vocal

	#Oopening tcp connection
	TCP_IP = '52.49.91.111'
	TCP_PORT = 9988
	BUFFER_SIZE = 1024
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	data = s.recv(BUFFER_SIZE)
	#level letters
	level = 3
	#bucle until all levels will be completed o failed
	while True:
		#enter on each lvl
		s.send('10')
		data = s.recv(BUFFER_SIZE)
		level += 1
		#default vars for each level
		letter = first_vocal('')
		isFirstVocal = 1
		del used_letter[:]
		#finish if we don't have more words
		if level not in words:
			break
		#bucle for each level
		while True:
			#send letter
			s.send(str(letter))
			data = s.recv(BUFFER_SIZE)
			result = result_buffer(data, level)
			print data
			#check if is final state
			if letter == "FINAL" or data == "":
				break
			#calc next letter
			letter = process_result(result, letter, level)

	s.close()


#read the buffer to take the result
def result_buffer(data, level):
	data = list(data)
	data = [x for x in data if x != '\n' and x != ' ' and x != '>']
	data = data[-level:]
	return data


#controller method
def process_result(result, letter, level):
	status = 0
	global isFirstVocal
	global last_result
	#check if we found the last word
	if result != last_result:
		status = 1
	#clean the words that doesn't match
	clean_words(status, result, letter, level)

	#is the first vocal?
	if isFirstVocal == 1 and status == 0:
		letter = first_vocal(letter)
	else:
		used_letter.append(letter);
		isFirstVocal = 0
		#freq of the new words
		calc_freq(level)
		#final letter
		letter = get_letter()

	last_result = result
	return letter




def first_vocal(letter):
	vocal = ''
	#rand on first vocal and must be unique
	while True:
		randVocal = randint(0 , 4)
		vocal = vowels[randVocal]
		if(letter != vocal):
			break
	return vocal

def calc_freq(level):
	global freq_letter
	freq_letter = {}
	#freq of the words

	for word in words[level]:
		for char in word:
			if char not in used_letter:
				if char in freq_letter:
					freq_letter[char] = freq_letter[char] + 1
				else:
					freq_letter[char] = 1




def get_letter():

	#order by freq
	freq_letter2 = sorted(freq_letter.iteritems(), key=lambda (k,v): (v,k),reverse=True)
	#if we don't words is last state
	if not freq_letter2:
		letter = 'FINAL'
	else:
		letter = freq_letter2[0][0]
	return letter

def clean_words(status, result, letter, level):

	global words
	words2 = []
	#if we found a letter we should check words with the letter in the same position
	if status == 1:

		for word in words[level]:

			lenghtResult = len(result)
			cursor = 0
			control = 0
			while cursor < lenghtResult:
				if result[cursor] != word[cursor] and (result[cursor] != '_' or word[cursor] == letter):
					control = 1
					cursor = lenghtResult

				cursor += 1
			if control == 0:
				words2.append(word)
	#if we don't found the letter we can delete all words that contain that letter
	else:
		for word in words[level]:
			if letter not in word:
				words2.append(word)

	words[level] = words2

if __name__ == '__main__':
	main()
