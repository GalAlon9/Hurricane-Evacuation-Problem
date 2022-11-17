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
    path.reverse()
    return path
    

def dijkstra(start:Node, graph:Graph):
    #returns shortest path to node with people
    #if no node with people, returns empty list
    shortestDists=[sys.maxsize]*len(graph.nodes)
    added=[False]*len(graph.nodes)
    shortestDists[start.id]=0
    parents=[None]*len(graph.nodes)
    #parents is array where each 
    for i in range(1,len(graph.nodes)):
        nearestIndex=-1
        shortestDist=sys.maxsize
        for index in range (len(graph.nodes)):
            if shortestDists[index]<shortestDist and not added[index]:
                nearestIndex=index
                shortestDist=shortestDists[index]
        if(nearestIndex==-1):
            #no path to breakable node
            return []
        if graph.get_node(nearestIndex).breakable and nearestIndex!=start.id:
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
    if nearestIndex != -1 and graph.get_node(nearestIndex).breakable and nearestIndex!=start.id:
        return getPath(start.id,parents,nearestIndex)
    return []
        

class SaboteurAgent(Agent):
    def __init__(self,graph:Graph, position:Node):
        super().__init__(position= position, graph=graph)

    def move(self):
        shortestPathToBreakable = dijkstra(self.position, self.graph)
        if len(shortestPathToBreakable)==0:
            self.isFinished()
        else:
           self.apply_move(self.graph.get_node(shortestPathToBreakable[0]))


    def isFinished(self):
        shortestPathToBreakable = dijkstra(self.position, self.graph)
        print ("path is:", shortestPathToBreakable)
        return len(shortestPathToBreakable)==0