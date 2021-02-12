"""
Simulation Engine
"""

from graph.graph_railway import SIGNAL_STATE
from graph.graph_dijkstra import dijkstra, shortest
from time import sleep


def sim_init(graph, station_from, station_to):
    """Init sim:
    Run Dijkstra's SPA and
    initialize railway signals"""

    graph.reset_vertices()
    dijkstra(graph, station_from)
    path_backwards = [station_to.get_id()]
    shortest(station_to, path_backwards)
    path = list(reversed(path_backwards))

    for i in range(1, len(path)):
        source = path[i - 1]
        destination = path[i]
        source_vertex = graph.get_vertex(source)
        source_vertex.set_signal_state(destination, SIGNAL_STATE['GREEN'])

    return path


def sim_update(graph, trains, current_paths, current_source, current_destination, final_destination):
    curr_dest_idx = 0
    dest_idx = 0
    distance_idx = 1

    if current_destination != final_destination:
        # Ensure no train crashes by
        # creating potential conflicts map
        conflict_map = {}
        for train, destination in current_destination.items():
            if destination not in conflict_map:
                conflict_map[destination] = []
            conflict_map[destination].append(train)

        # Coordinate railway signals queue
        for dest, trains_var in conflict_map.items():
            if len(trains) > 1:
                train = trains_var.pop(0)
                source_vertex = graph.get_vertex(current_source[train])
                source_vertex.set_signal_state(destination, SIGNAL_STATE['GREEN'])
                for train in trains_var:
                    source_vertex = graph.get_vertex(current_source[train])
                    source_vertex.set_signal_state(destination, SIGNAL_STATE['RED'])

    # Update and display current status
    for train in trains:
        destination = current_destination[train]
        signal_state = graph.get_vertex(current_source[train]).get_signal_state(destination)

        if signal_state == SIGNAL_STATE['GREEN']:
            distance = current_paths[train][curr_dest_idx][distance_idx]
            if distance > 0:
                current_paths[train][curr_dest_idx][distance_idx] -= 1
                distance = current_paths[train][curr_dest_idx][distance_idx]

                print(">>> {} on it's way to {}, "
                      "distance remaining {}.".format(train,
                                                      destination,
                                                      distance))
            else:
                print("****** {} has arrived at {}.".format(train, destination))
                if current_paths[train]:
                    source_path = current_paths[train].pop(curr_dest_idx)
                    current_source[train] = source_path[dest_idx]
                    if current_paths[train]:
                        current_destination[train] = current_paths[train][curr_dest_idx][dest_idx]

        else:
            print(">>>> {} to {} stopped with signal RED. ".format(train, destination))

    return


def sim_start(graph, trains, paths):
    """Run Simulation"""
    print("Starting simulation..")
    sleep(1)

    current_source = {}
    current_destination = {}
    final_destination = {}
    current_paths = {}

    # Initialize simulation states
    for train, stations in trains.items():
        # print(paths[train])
        current_source[train] = paths[train][0]
        current_destination[train] = paths[train][1]
        final_destination[train] = paths[train][-1]

    # Store relevant path weights (distances)
    for train, path in paths.items():
        current_paths[train] = []
        for i in range(1, len(path)):
            source = path[i - 1]
            destination = path[i]
            source_vertex = graph.get_vertex(source)
            distance = source_vertex.get_weight(destination)
            current_paths[train].append([destination, distance])

    total_time_elapsed = 1

    sim_update(graph, trains, current_paths, current_source, current_destination, final_destination)
    sleep(2)

    all_journeys_complete = False
    while not all_journeys_complete:
        total_time_elapsed += 1
        sim_update(graph, trains, current_paths, current_source, current_destination, final_destination)
        sleep(2)
        print("Total sim time: {}".format(total_time_elapsed))

        all_journeys_complete = True
        for train, path in current_paths.items():
            # Check if any remaining paths left
            if path:
                all_journeys_complete = False
                break

    print("Simulation complete!")


def sim_run(graph, trains):
    """Main sim handler"""
    paths = {}
    from_idx = 0
    to_idx = 1

    for train in trains:
        # Initialize graph for simulation
        paths[train] = sim_init(graph,
                                graph.get_vertex(trains[train][from_idx]),
                                graph.get_vertex(trains[train][to_idx]))

        # Describe shortest path
        path_str = ""
        for station in paths[train]:
            path_str += station + " -> "
        path_str = path_str[:-4]
        print('The shortest path for {} is: {}'.format(train, path_str))

    # Run simulation
    sim_start(graph, trains, paths)

