"""
Menu Functions
"""

from PyInquirer import style_from_dict, prompt, Token
from user_interface.menu_questions import style, main_questions
from user_interface.menu_sim import sim_menu
from user_interface.menu_build import build_menu
from graph.graph_railway import GraphRailway


def main_menu():
    """Main Menu"""
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

        elif answers['main'] == 'Simulation':
            sim_menu(railway, g)
            print(answers)

        else:  # Quit program
            print("Goodbye!")
            break

