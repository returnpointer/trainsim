"""
Railway Network Graph Class
inherits from Dijkstra Graph Class
"""

from graph.graph_dijkstra import VertexD, GraphD
from graph import graph_dijkstra

SIGNAL_STATE = {'RED': 0, 'GREEN': 1}
SIGNAL_STATE_DCODE = {0: 'RED', 1: 'GREEN'}


class Connector(VertexD):
    weight_idx = 0
    signal_state_idx = 1

    def __init__(self, node):
        super().__init__(node)
        # self.type = node.type

    def add_neighbor(self, neighbor, weight=0, signal_state=SIGNAL_STATE['RED']):
        self.adjacent[neighbor.id] = [weight, signal_state]

    def get_signal_state(self, neighbor_id):
        if neighbor_id not in self.adjacent:
            print("ERROR [get_signal_state]: {} not a valid neighbor to {}!".format(neighbor_id, self.id))
            return
        return self.adjacent[neighbor_id][self.signal_state_idx]

    def set_signal_state(self, neighbor_id, state):
        if state != SIGNAL_STATE['GREEN'] and state != SIGNAL_STATE['RED']:
            print("Error: Invalid Signal State!\n"
                  "Signal state unchanged "
                  "from {}".format(SIGNAL_STATE_DCODE[self.adjacent[neighbor_id][self.signal_state_idx]]))
        else:
            if neighbor_id not in self.adjacent:
                print("ERROR [set_signal_state]: {} not a valid neighbor to {}!".format(neighbor_id, self.id))
                return
            self.adjacent[neighbor_id][self.signal_state_idx] = state

    def get_weight(self, neighbor_id):
        if neighbor_id not in self.adjacent:
            print("ERROR [get_weight]: {} not a valid neighbor to {}!".format(neighbor_id, self.id))
            return
        return self.adjacent[neighbor_id][self.weight_idx]


class GraphRailway(GraphD):
    def __init__(self):
        super().__init__()

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Connector(node)
        self.vert_dict[node.id] = new_vertex
        return new_vertex


class Node:
    def __init__(self, id):
        self.id = id


def print_graph(g):
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w
            # wid = w.get_id()
            print('( {} , {}, {})'.format(vid, wid, v.get_weight(w)))


if __name__ == '__main__':
    print("Railway-Graph")
    g = GraphRailway()

    nodes = {'a': Node('a'),
             'b': Node('b'),
             'c': Node('c'),
             'd': Node('d'),
             'e': Node('e'),
             'f': Node('f')}

    g.add_vertex(nodes['a'])
    g.add_vertex(nodes['b'])
    g.add_vertex(nodes['c'])
    g.add_vertex(nodes['d'])

    # g.add_edge('a', 'b', 1)
    g.add_edge('a', 'c', 1)
    # g.add_edge('b', 'c', 3)
    # g.add_edge('b', 'd', 2)
    # g.add_edge('c', 'd', 10)

    print('Dijkstra Graph data:')
    print_graph(g)

    # graph_dijkstra.dijkstra(g, g.get_vertex('d'))
    #
    # target = g.get_vertex('c')
    # path = [target.get_id()]
    # graph_dijkstra.shortest(target, path)
    # # print('The shortest path : {}'.format(list(reversed(path))))
    # print('The shortest path : {}'.format(path[::-1]))
    # path_str = ""
    # for station in reversed(path):
    #     path_str += station + " -> "
    #
    # path_str = path_str[:-4]
    # print(path_str)
    #
    # g.reset_vertices()
    graph_dijkstra.dijkstra(g, g.get_vertex('a'))

    target = g.get_vertex('c')
    path = [target.get_id()]
    graph_dijkstra.shortest(target, path)
    # print('The shortest path : {}'.format(list(reversed(path))))
    print('The shortest path : {}'.format(path[::-1]))
    path_str = ""
    for station in reversed(path):
        path_str += station + " -> "

    path_str = path_str[:-4]
    print(path_str)

