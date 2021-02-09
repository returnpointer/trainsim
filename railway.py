from graph import Vertex, Graph

SIGNAL_STATE = [ 'GREEN', 'RED']


class Connection(Vertex):
    weight_idx = 0
    signal_state_idx = 1

    def __init__(self, node):
        super().__init__(node)
        self.type = node.type

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

class Node:
    def __init__(self, id):
        self.id = id


# class Station(Node):
#     def __init__(self, node):
#         super().__init__(self, node)
#
#
# class Junction(Node):
#     def __init__(self, node):
#         super().__init__(self, node)


class Railway(Graph):
    def __init__(self):
        super().__init__()

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Connection(node)
        self.vert_dict[node.id] = new_vertex
        return new_vertex

