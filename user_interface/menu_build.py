"""
Railway Builder Menu
"""

from PyInquirer import prompt
from user_interface.menu_questions import style, build_questions, train_questions, track_questions, sim_questions1, \
    sim_questions2
from apis.railway_builder import add_station, add_junction, add_track, add_train
from time import sleep


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
