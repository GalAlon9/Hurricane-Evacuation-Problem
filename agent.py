# abstract class for agent
from abc import ABC, abstractmethod
from node import Node
from graph import Graph


class Agent(ABC):
    def __init__(self, position:Node, graph : Graph):
        self.graph = graph
        self.position = position
        self.people_on_board = 0
        self.timer =0
    
    def getScore(self):
        return self.people_on_board*1000 - self.timer

    @abstractmethod
    def move(self):
        pass

    def isFinished(self):
        return self.graph.people_to_save == self.people_on_board
    

