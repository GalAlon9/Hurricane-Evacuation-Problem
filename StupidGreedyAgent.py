import sys
from agent import Agent
from graph import Graph
from node import Node

def getPath(start:int,parents,nearestIndex):
    #returns path from start to nearestIndex
    path=[]
    while nearestIndex!=start:
        path.append(nearestIndex)
        nearestIndex=parents[nearestIndex]
    path.append(start)
    path.reverse()
    return path
    

def dijkstra(start:Node, graph:Graph):
    #returns shortest path to node with people
    #if no node with people, returns empty list
    shortestDists=[sys.maxsize]*len(graph.nodes)
    added=[False]*len(graph.nodes)
    shortestDists[start.id]=0
    parents=[None]*len(graph.nodes)
    for i in range(1,len(graph.nodes)):
        nearestIndex=-1
        shortestDist=sys.maxsize
        for index in range (len(graph.nodes)):
            if shortestDists[index]<shortestDist and not added[index]:
                nearestIndex=index
                shortestDist=shortestDists[index]
        if graph.get_node(nearestIndex).num_of_people>0:
            #found node with people
            return getPath(start.id,parents,nearestIndex)
        added[nearestIndex]=True
        #updates shortestDists for all nodes adjacent to nearestIndex
        for index in range (len(graph.nodes)):
            if graph.edges[nearestIndex][index]!=-1 and shortestDists[nearestIndex]+graph.edges[nearestIndex][index]<shortestDists[index]:
                shortestDists[index]=shortestDists[nearestIndex]+graph.edges[nearestIndex][index]
                parents[index]=nearestIndex
    #incase furthest node has people
    nearestIndex=-1
    shortestDist=sys.maxsize
    for index in range (len(graph.nodes)):
        if shortestDists[index]<shortestDist and not added[index]:
            nearestIndex=index
            shortestDist=shortestDists[index]
    if graph.get_node(nearestIndex).num_of_people>0:
        return getPath(start.id,parents,nearestIndex)
    return []
        

class StupidGreedyAgent(Agent):
    def __init__(self,graph:Graph, position:int):
        super().__init__(position= graph.get_node(position), graph=graph)

    def move(self):
        self.shortestPathToPeople = dijkstra(self.position, self.graph)
        if len(self.shortestPathToPeople)>0:
            self.shortestPathToPeople.pop(0)
        print(self.shortestPathToPeople)
        if len(self.shortestPathToPeople)==0:
            self.isFinished()
        else:
            nextMove = self.shortestPathToPeople.pop(0)
            self.timer += self.graph.edges[self.position.id][nextMove]
            self.position = self.graph.get_node(nextMove)
            self.people_on_board =self.people_on_board + self.position.num_of_people
            self.position.num_of_people = 0
            #TO DO add break

    def isFinished(self):
        super().isFinished()