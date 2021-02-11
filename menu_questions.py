main_questions = [
    {
        'type': 'list',
        'name': 'main',
        'message': '1. What would you like to do ?',
        'choices': ['Build Railway', 'Run Simulation', 'Quit'],
    }
]

build_questions = [
    {
        'type': 'list',
        'name': 'build',
        'message': '1. Add to the railway network ?',
        'choices': ['Station', 'Junction', 'Track', 'Train', 'Main Menu'],
    },
    # {
    #     'type': 'list',
    #     'name': 'connect',
    #     'message': '2. Place track between connections ?',
    #     'choices': [],
    # }
]

track_questions = [
    {
        'type': 'list',
        'name': 'track',
        'message': '1. How long would you like the track to be ?',
        'choices': ['3 units', '5 units', '10 units'],
    }
]


train_questions = [
    {
        'type': 'list',
        'name': 'railway',
        'message': '1. Where would you like to station the train ?',
        'choices': [],
    }
]
