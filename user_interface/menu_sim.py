"""
Simulation Menu
"""

from PyInquirer import prompt
from user_interface.menu_questions import style, sim_questions1, sim_questions2
from sim_engine.simulation import sim_run


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
                # print(neighbor_stations)
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

    return
