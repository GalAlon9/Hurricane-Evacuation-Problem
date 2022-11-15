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
            self.timer += self.graph.edges[self.position.id][next_node.id]
            #if the node is breakable, make all the edges including it -1
            if self.position.breakable:
                for i in range(len(self.graph.edges)):
                    self.graph.edges[i][self.position.id] = -1
                    self.graph.edges[self.position.id][i] = -1
            #    self.graph.edges[:,self.position.id] = -1
            #    self.graph.edges[self.position.id,:] = -1
            self.position = next_node
            self.graph.remove_target(self.position)
            self.people_on_board += self.position.num_of_people
            self.position.num_of_people = 0
            

            return 1


        

    def isFinished(self):
        if self.people_on_board == self.graph.people_to_save:
            return True
        else:
            return False