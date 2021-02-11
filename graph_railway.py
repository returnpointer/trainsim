from graph_dijkstra import VertexD, GraphD
import graph_dijkstra


SIGNAL_STATE = ['GREEN', 'RED']


class Connector(VertexD):
    weight_idx = 0
    signal_state_idx = 1

    def __init__(self, node):
        super().__init__(node)
        # self.type = node.type

    def add_neighbor(self, neighbor, weight=0, signal_state='RED'):
        self.adjacent[neighbor.id] = weight, signal_state

    def get_signal_state(self, neighbor):
        return self.adjacent[neighbor.id][self.signal_state_idx]

    def set_signal_state(self, neighbor, state):
        if state not in SIGNAL_STATE:
            print("Error: Invalid Signal State!\n"
                  "Signal state unchanged from {}".format(self.adjacent[neighbor.id][self.signal_state_idx]) )
        else:
            self.adjacent[neighbor.id][self.signal_state_idx] = state

    def get_weight(self, neighbor_id):
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
    g.add_vertex(nodes['e'])
    g.add_vertex(nodes['f'])

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    # g.add_edge('a', 'd', 5)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    print('Dijkstra Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w
            # wid = w.get_id()
            print('( {} , {}, {})'.format(vid, wid, v.get_weight(w)))

    graph_dijkstra.dijkstra(g, g.get_vertex('a'), g.get_vertex('e'), nodes)

    target = g.get_vertex('e')
    path = [target.get_id()]
    graph_dijkstra.shortest(target, path)
    print('The shortest path : {}'.format(path[::-1]))
