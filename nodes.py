
class Web:
    connections = {}
    weights = []
    def add(self, first, second, weight = 1):

        first = Node(first)
        second = Node(second)

        connection = frozenset(first, second)
        if connection not in self.connections:
            self.connections.[connection] = weight
        else:
            self.connections[connection] +=weight
class Node:
    all_connections = {}
    def __init__(self, name):
        self.connections = {}
        self.name = name
    def add(self, first, second, weight = 1):
        connection = frozenset(first, second)
        if connection not in self.connections:
            self.connections.[connection] = weight
        else:
            self.connections[connection] +=weight
def group(data):
    startnode = data.keys[0]
