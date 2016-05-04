import sys
import csv
#words split text
struct = {}
tapes = []
def main():
	#create struct
	load_struct(sys.argv[1])
	#process tapes
	load_tapes()

def load_struct(fl):
	#3 pass
	#1- loading states
	#2- loading var states (0,1,#,' ')
	#3- loading def (write, step ...)

	with open(fl) as fileInput:

		#first line
		fileInput.readline()
		#assuming always we will have code:
		fileInput.readline()
		lines = fileInput.readlines()
		#delete the last line
		lines = lines[:-1]
		constDef = ['0', '1', '#', ' ']
		lastState= ''
		lastVar=''
		lastDef=''
		boolTapes = 0
		for line in lines:
			try:
				#clean line
				line = line.lstrip()
				line = line.rstrip()
				line = line.replace("'", "")
				#if we split : and we have 2 values this is a def part
				splitLine = line.split(':')


				if splitLine[0] == 'tapes':
					boolTapes = 1
				if splitLine[1] != '':
					if boolTapes == 1:
						tapes.append(splitLine[1].lstrip())
					else:
						struct[lastState][lastVar][splitLine[0]] = splitLine[1].lstrip()
						lastDef = splitLine[0]

				else:
					if splitLine[0] in constDef:
						struct[lastState][splitLine[0]] = {}
						lastVar = splitLine[0]

					else:
						struct[splitLine[0]] = {}
						lastState = splitLine[0]
			except (KeyError, IndexError, TypeError):
				print 'Error construncting the struct'




def load_tapes():
	#process al tapes
	count = 0;
	for tape in tapes:
		count += 1;
		finalTape = run_tapes(tape)
		print 'Tape #'+str(count)+': '+str(finalTape)

def run_tapes(tape):
	cursor = 0
	#by default starting at state start
	state = 'start'
	#control the finish
	boolControl = 0

	while(boolControl == 0):
		#if is final it's blank input
		if cursor >= len(tape):
			var = ' '
		else:
			var = tape[cursor]
		actions = struct[state][var]
		# 3 tasks
		# 1- Write
		# 2- Move
		# 3- State
		# THE ORDER IS IMPORTANT!
		if 'write' in actions:
			tape = write_tape(actions['write'], cursor, tape)
		if 'move' in actions:
			cursor = move_tape(actions['move'], cursor)
		if 'state' in actions:
			state = actions['state']



		#check if final state
		if state == 'end':
			boolControl = 1

	return tape
def move_tape(actionValue, cursor):
	#move cursor position
	if actionValue == 'right':
		cursor += 1
	elif actionValue == 'left':
		cursor -= 1
	return cursor

def write_tape(actionValue, cursor, tape):
	#rewrittte string
	try:
		bTape = list(tape)
		bTape[cursor] = actionValue

	except (KeyError, IndexError, TypeError):
		bTape.append(actionValue)

	return "".join(bTape)

if __name__ == '__main__':
	main()
