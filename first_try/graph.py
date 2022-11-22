from first_try.node import Node
from typing import List
class Graph:
    def __init__(self, nodes: List[Node], edges: List[List[int]]):
        self.nodes = nodes
        self.edges = edges
        self.people_to_save = sum(node.num_of_people for node in nodes)
        self.targets = [node for node in nodes if node.num_of_people > 0]
        # self.to_be_visited = []

    def print_graph(self):
        for i in range(len(self.nodes)):
            print(self.nodes[i].id, end=" ")
            for j in range(len(self.edges[i])):
                print(self.edges[i][j], end=" ")
            print()

    def get_node(self, id: int):
        for node in self.nodes:
            if node.id == id:
                return node
        return None

    def remove_target(self, node: Node):
        if node in self.targets:
            self.targets.remove(node)
        
    def  visit(self, node: Node):
        node.visited = True
        for i in range(len(self.edges[node.id])):
            if self.edges[node.id][i] != -1:
                self.edges[node.id][i] = -1
                self.edges[i][node.id] = -1
        self.targets.remove(node)
        self.people_to_save -= node.num_of_people
        node.num_of_people = 0

    