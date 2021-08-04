from ..assets.stacks_and_queues import Queue


class Vertix:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertix, weight):
        self.vertix = vertix
        self.weight = weight


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        v = Vertix(value)
        self.adjacency_list[v] = []
        return v

    def add_edge(self, start_node, end_node, weight=0):
        if start_node not in self.adjacency_list:
            raise KeyError('Start node is not exist in Graph')

        if end_node not in self.adjacency_list:
            raise KeyError('End node is not exist in Graph')

        edge = Edge(end_node, weight)
        self.adjacency_list[start_node].append(edge)

    def get_nodes(self):

        return self.adjacency_list.keys()

    def get_neighbors(self, node):

        return self.adjacency_list[node]

    def size(self):

        return len(self.adjacency_list)

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():
            # Concatenate the value of vertix
            output += vertix.value
            # Iterate over all edges of this vertix
            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value
            # Add a new line
            output += '\n'
        return output

    def breadth_first(self, node):
        node_lst = []
        queue = Queue()
        visit_node = set()

        if node not in self.adjacency_list or self.adjacency_list[node] == []:
            return None

        queue.enqueue(node)
        visit_node.add(node.value)

        while not queue.isEmpty():
            vertix = queue.dequeue()
            node_lst.append(vertix.value)

            for edge in self.adjacency_list[vertix]:
                if edge.node.value not in visit_node:
                    visit_node.add(edge.node.value)
                    queue.enqueue(edge.node)

        return node_lst
