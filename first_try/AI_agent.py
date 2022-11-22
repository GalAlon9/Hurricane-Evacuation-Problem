# abstract class for AI agent
from abc import ABC, abstractmethod
from first_try.graph_try.graph import Graph


class AI_agent(ABC):
    def __init__(self, position :int , graph : Graph):
        self.graph = graph
        self.position = position
        self.people_on_board = 0
        self.timer =0
        
    

    def heuristic(self, state):
        #return the heuristic value of the state : sum of minimum distances from current position to all targets
        return 0
        

    