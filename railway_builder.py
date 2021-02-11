from graph_railway import Node
"""Railway Building APIs"""

num_stations = 0
num_junctions = 0
num_tracks = 0
num_trains = 0


def add_station(railway, graph):
    global num_stations
    num_stations += 1
    station_id = 's' + str(num_stations)

    graph.add_vertex(Node(station_id))

    railway['stations'].append(station_id)

    return num_stations


def add_junction(railway, graph):
    global num_junctions
    num_junctions += 1
    junction_id = 'j' + str(num_junctions)

    graph.add_vertex(Node(junction_id))

    railway['junctions'].append(junction_id)

    return num_junctions


def add_tracks(railway, graph, frm, to, size):
    global num_tracks
    num_tracks += 1

    graph.add_edge(frm, to, size)

    railway['tracks'].append(frm+'-'+to)

    return num_tracks


def add_trains(railway, graph, station):
    global num_trains
    return
