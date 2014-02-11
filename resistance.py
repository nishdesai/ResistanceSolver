import solver
import time

class Game:
	def __init__(self):
		self.file_name = time.strftime('%H-%M-%d-%m-%Y.txt')
		self.solver = None

	def set_file_name(self, file_name):
		"""Setter method for game file"""
		self.file_name = file_name
		self.solver = solver.Solver(solver.Parser(open(file_name)).args)

	def new_game(self, resistance_count, spy_count, players):
		"""Sets up new game"""
		f = open(self.file_name, 'a+')
		setup_string = "Spies %(spy)d\nResistance %(res)d\n%(player)s" %{'spy':spy_count, 'res':resistance_count, 'player':', '.join(players)}

		f.write(setup_string)
		f.close
		self.set_file_name(self.file_name)




game = Game()

def start_game():
	print '\nWelcome to the game of Resistance!\n\n'
	print '(L)oad game from file.\n'
	print '(N)ew game.\n'

	start_option = raw_input('Choose starting option: ')
	start_option = start_option.upper()

	if start_option == 'N':
		start_new_game()

	elif start_option == "L":
		file_name = raw_input('\nEnter filename: ') 
		game.set_file_name(file_name)

	else:
		print 'Sorry. I didn\'t recognize that. Please try again.\n'
		start_game()

def play_game(solver):
	pass

def start_new_game():
	pass


start_game()