"""
Menu Functions
"""

from PyInquirer import style_from_dict, prompt, Token
from user_interface.menu_questions import main_questions, build_questions, train_questions, track_questions, sim_questions1, \
    sim_questions2
from graph.graph_railway import GraphRailway
from apis.railway_builder import add_station, add_junction, add_track, add_train
from sim_engine.simulation import sim_run
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
        add_station(railway, graph)

        sim_questions2[0]['choices'].append(railway['stations'][-1])
        train_questions[0]['choices'].append(railway['stations'][-1])
        track_questions[1]['choices'].append(railway['stations'][-1])
        track_questions[2]['choices'].append(railway['stations'][-1])

        print("Station " + railway['stations'][-1] + " successfully added.")
        sleep(1)

    elif answers['build'] == 'Junction':
        if not railway['stations']:
            print("Sorry, cannot build Junctions without any Stations!")
        else:
            add_junction(railway, graph)

            track_questions[1]['choices'].append(railway['junctions'][-1])
            track_questions[2]['choices'].append(railway['junctions'][-1])

            print("Junction " + railway['junctions'][-1] + " successfully added.")
            sleep(1)

    elif answers['build'] == 'Track':
        if len(railway['stations']) < 2 and not railway['junctions'] or \
                len(railway['junctions']) < 2 and not railway['stations']:
            print("Sorry, insufficient Stations/Junctions!")

        else:
            answers = prompt(track_questions, style=style)
            if answers['track_size'] == '3 units':
                track_size = 3
            elif answers['track_size'] == '5 units':
                track_size = 5
            else:  # 10 units
                track_size = 10

            frm = answers['track_from']
            to = answers['track_to']

            if frm == to:
                print("Cannot build track from {} back to {}!".format(frm, to))
            else:
                track_num = add_track(railway, graph, frm, to, track_size)
                track_id = 'track' + str(track_num)
                print("Track " + track_id +
                      " successfully added between {}, {}.".format(railway['tracks'][track_id][0],
                                                                   railway['tracks'][track_id][1]))
                sleep(1)

    elif answers['build'] == 'Train':
        if not railway['stations']:
            print("Sorry, cannot add Trains without any Stations!")

        else:
            answers = prompt(train_questions, style=style)

            train_num = add_train(railway, answers['station'])

            train_id = 'train' + str(train_num)
            sim_questions1[0]['choices'].append(train_id)

            print("Train " + train_id + " at station " +
                  railway['trains'][train_id] + " successfully added.")
            sleep(1)

    else:  # back to Main Menu
        print("Stations:")
        print(railway['stations'])

        print("Junctions:")
        print(railway['junctions'])

        print("Tracks:")
        print(railway['tracks'])

        print("Trains:")
        print(railway['trains'])
        sleep(1)

        ret = True

    return ret


def sim_menu(railway, graph):
    """Simulation Menu"""

    if not railway['stations'] or \
            not railway['tracks'] or \
            not railway['trains']:
        print("Sorry! Cannot run simulation without building "
              "railway network of stations/tracks/trains first.")
        return

    while 1:
        trains = {}
        answers = prompt(sim_questions1, style=style)

        if answers['trains'] == 'Main Menu':
            # Quit Simulation
            break

        elif answers['trains'] == 'All':
            # print("Sorry! Simulation of 'All' trains currently not supported, "
            #       "please select a single train.")
            for key in railway['trains'].keys():
                base_station = railway['trains'][key]

                # arbitrary choice of last
                # neighbor as destination station
                neighbor_stations = list(graph.get_vertex(base_station).get_connections())
                neighbor_stations.sort()
                dest_station = neighbor_stations[-1]

                trains[key] = [base_station, dest_station]

        else:  # User selected train
            train = answers['trains']
            base_station = railway['trains'][train]

            answers = prompt(sim_questions2, style=style)
            while answers['destination'] == base_station:
                print("Sorry! Can't start and end at the same station.")
                answers = prompt(sim_questions2, style=style)

            trains[train] = [base_station, answers['destination']]

        sim_run(graph, trains)


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

        elif answers['main'] == 'Simulation':
            sim_menu(railway, g)
            print(answers)

        else:  # Quit program
            print("Goodbye!")
            break

