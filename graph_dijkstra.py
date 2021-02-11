"""
originally from
https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
"""

from graph import Vertex, Graph, Node
import sys


class VertexD(Vertex):
    def __init__(self, node):
        super().__init__(node)
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def __lt__(self, other_node):
        return self.id < other_node.id

    def __le__(self, other_node):
        return self.id <= other_node.id

    def __gt__(self, other_node):
        return self.id > other_node.id

    def __ge__(self, other_node):
        return self.id >= other_node.id

    def __eq__(self, other_node):
        return self.id == other_node.id

    def __ne__(self, other_node):
        return self.id != other_node.id

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x for x in self.adjacent])


class GraphD(Graph):
    def __init__(self):
        super().__init__()

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = VertexD(node)
        self.vert_dict[node.id] = new_vertex
        return new_vertex

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    """ make shortest path from v.previous"""
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


import heapq


def dijkstra(aGraph, start, target, nodes):
    print('''Running Dijkstra's shortest path''')
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        # for next in v.adjacent:
        for next in current.adjacent:
            next_vertex = aGraph.get_vertex(next)
            # if visited, skip
            if next_vertex.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next_vertex.get_distance():
                next_vertex.set_distance(new_dist)
                next_vertex.set_previous(current)
                print('updated : current = {} '
                      'next = {} new_dist = {}'.format(current.get_id(), next_vertex.get_id(), next_vertex.get_distance()))
            else:
                print('not updated : current = {} '
                      'next = {} new_dist = {}'.format(current.get_id(), next_vertex.get_id(), next_vertex.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


if __name__ == '__main__':

    print("Dijkstra-Graph")
    g = GraphD()

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

    dijkstra(g, g.get_vertex('b'), g.get_vertex('f'), nodes)

    target = g.get_vertex('f')
    path = [target.get_id()]
    shortest(target, path)
    print('The shortest path : {}'.format(path[::-1]))
