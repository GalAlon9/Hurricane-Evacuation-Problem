# abstract class for agent
from abc import ABC, abstractmethod
from node import Node
from graph import Graph


class Agent(ABC):
    def __init__(self, position:Node, graph : Graph):
        self.graph = graph
        self.position = position
        #picks up people from starting position:
        self.people_on_board = self.position.num_of_people
        position.num_of_people=0
        self.timer =0
    
    def getScore(self):
        return self.people_on_board*1000 - self.timer

    @abstractmethod
    def move(self):
        pass

    def isFinished(self):
        return self.graph.people_to_save == self.people_on_board

    def apply_move(self, next_node:Node):
        self.timer += self.graph.edges[self.position.id][next_node.id]
        #if the node is breakable, make all the edges including it -1
        if self.position.breakable:
            for i in range(len(self.graph.edges)):
                self.graph.edges[i][self.position.id] = -1
                self.graph.edges[self.position.id][i] = -1
        
        self.position = next_node
        self.graph.remove_target(self.position)
        self.people_on_board += self.position.num_of_people
        self.position.num_of_people = 0
        return next_node
    

