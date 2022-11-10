from .agent import Agent
from .graph import graph

class StupidGreedyAgent(Agent):

    def __init__(self):
        super().__init__()
        self.shortestPathToPeople = dijkstra(self.position, graph)

    def move(self):
        if shortestPathToPeople.isEmpty():
            finished()
        else:
            nextMove = shortestPathToPeople.pop(0)
            self.timer += graph.edges[self.position.id][next_node.id]
            self.position = next_node
            self.people_on_board += self.position.num_of_people
            self.position.num_of_people = 0
            #if the node is breakable, make all the edges including it -1
            if self.position.breakable:
               graph.edges[:,self.position.id] = -1
               graph.edges[self.position.id,:] = -1

    def finished(self):
        super().finished()

    def dijkstra(self, start, graph):
        #returns shortest path to node with people
        #if no node with people, returns empty list
        shortestDist=[]
        added=[]
        for i in range(len(graph.nodes)):
            shortestDist[i]=
            added.append(False)
        