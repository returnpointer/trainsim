"""Railway Building APIs"""
from graph_railway import Node

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


def add_track(railway, graph, frm, to, size):
    global num_tracks
    num_tracks += 1

    graph.add_edge(frm, to, size)

    track_id = 'track' + str(num_tracks)
    railway['tracks'][track_id] = [frm, to]

    return num_tracks


def add_train(railway, station):
    global num_trains
    num_trains += 1

    train_id = 'train' + str(num_trains)
    railway['trains'][train_id] = station

    return num_trains
