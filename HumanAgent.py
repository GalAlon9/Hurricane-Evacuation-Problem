from .agent import Agent
from .graph import graph

class HumanAgent(Agent):

    def __init__(self):
        super().__init__()

    def move(self):
        #recieve input from user
        next_position:int = input("Enter your move: ")
        next_node = graph.get_node(next_position)
        if next_node is None:
            print("Invalid move")
            return 0
        elif graph.edges[self.position.id][next_node.id] == -1:
            print("Invalid move")
            return 0
        else :
            self.timer += graph.edges[self.position.id][next_node.id]
            self.position = next_node
            graph.remove_target(self.position)
            self.people_on_board += self.position.num_of_people
            self.position.num_of_people = 0
            #if the node is breakable, make all the edges including it -1
            if self.position.breakable:
               graph.edges[:,self.position.id] = -1
               graph.edges[self.position.id,:] = -1

            return 1


        

    def finished(self):
        super().finished()