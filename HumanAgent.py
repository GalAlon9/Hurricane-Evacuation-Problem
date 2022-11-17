from agent import Agent
from graph import Graph

class HumanAgent(Agent):

    def __init__(self,graph:Graph, position:int):
        super().__init__(position= graph.get_node(position), graph=graph)

    def move(self):
        #recieve input from user
        next_position:int = int(input("Enter your move: ")) -1
        next_node = self.graph.get_node(next_position)
        if next_node is None:
            print("Invalid move")
            return 0
        elif self.graph.edges[self.position.id][next_node.id] == -1:
            print("Invalid move")
            return 0
        else :
            self.apply_move(next_node)
            return 1


        

    def isFinished(self):
        if self.people_on_board == self.graph.people_to_save:
            return True
        else:
            return False