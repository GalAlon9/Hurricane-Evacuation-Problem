# abstract class for AI agent
from abc import ABC, abstractmethod
from graph import Graph


class AI_agent(ABC):
    def __init__(self, position :int , graph : Graph):
        self.graph = graph
        self.position = position
        self.people_on_board = 0
        self.timer =0
    
    