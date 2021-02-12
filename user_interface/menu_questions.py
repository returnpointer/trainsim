"""
Menu Question Definitions
"""

main_questions = [
    {
        'type': 'list',
        'name': 'main',
        'message': '1. What would you like to do ?',
        'choices': ['Build Railway', 'Simulation', 'Quit'],
    }
]

build_questions = [
    {
        'type': 'list',
        'name': 'build',
        'message': '1. Add to the railway network ?',
        'choices': ['Station', 'Junction', 'Track', 'Train', 'Main Menu'],
    },
]

track_questions = [
    {
        'type': 'list',
        'name': 'track_size',
        'message': '1. How long would you like the track to be ?',
        'choices': ['3 units', '5 units', '10 units'],
    },
    {
        'type': 'list',
        'name': 'track_from',
        'message': '2. Where does the track start ?',
        'choices': [],
    },
    {
        'type': 'list',
        'name': 'track_to',
        'message': '3. Where does the track end ?',
        'choices': [],
    }
]


train_questions = [
    {
        'type': 'list',
        'name': 'station',
        'message': '1. Where would you like to station the train ?',
        'choices': [],
    }
]


sim_questions1 = [
    {
        'type': 'list',
        'name': 'trains',
        'message': '1. Which train(s) would you like to ride ?',
        'choices': ['Main Menu', 'All'],
    },
]

sim_questions2 = [
    {
        'type': 'list',
        'name': 'destination',
        'message': '1. Where would you like to go ?',
        'choices': [],
    }
]
