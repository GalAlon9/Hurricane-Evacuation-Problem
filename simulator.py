from .graph import graph
from .agent import agent

class Simulator:
    def __init__(self, num_of_agents: int):
        self.num_of_agents = num_of_agents
        
    def run(self):
        
