from PyInquirer import style_from_dict, prompt, Token, Separator
from menu_questions import main_questions, build_questions, train_questions
from graph_railway import GraphRailway
from railway_builder import add_station
from time import sleep

style = style_from_dict({
	Token.Separator: '#fff',  # white
	Token.QuestionMark: '#000',  # black
	Token.Selected: '#00BFFF',  # sky blue
	Token.Pointer: '#fff',  # white
	Token.Instruction: '#fff',  # white
	Token.Answer: '#008000 bold',  # green
	Token.Question: '#FF7F50',  # shade of orange
})


def build_menu(railway, graph):
	ret = False
	answers = prompt(build_questions, style=style)
	if answers['build'] == 'Station':
		print(add_station(railway, graph))
		sleep(2)
		print(answers)
	elif answers['build'] == 'Junction':
		# add_junction(railway, graph)
		print(answers)
	elif answers['build'] == 'Train':
		# add_train(railway, graph)
		print(answers)
	else:  # back to Main Menu
		ret = True

	return ret


def main_menu():

	g = GraphRailway()
	railway = {
		'stations': [],
		'junctions': [],
		'tracks': {},
		'trains': {}
	}

	while 1:
		answers = prompt(main_questions, style=style)

		if answers['main'] == 'Build Railway':
			back_to_main_menu = False
			while not back_to_main_menu:
				back_to_main_menu = build_menu(railway, g)
		elif answers['main'] == 'Run Simulation':
			# sim_run()
			print(answers)
		else:  # Quit program
			print("Goodbye!")
			break


main_menu()
