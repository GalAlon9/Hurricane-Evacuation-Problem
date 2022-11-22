from abc import ABC, abstractmethod
from first_try.node import Node
from first_try.graph_try.graph import Graph
import sys


# abstract class for agent
class Agent(ABC):
    def __init__(self, position:Node, graph : Graph):
        self.graph = graph
        self.position = position
        #picks up people from starting position:
        self.people_on_board = self.position.num_of_people
        position.num_of_people=0
        self.timer =0
    
    def getScore(self):
        return self.people_on_board*1000 - self.timer

    @abstractmethod
    def move(self):
        pass

    def isFinished(self):
        return self.graph.people_to_save == self.people_on_board

    def apply_move(self, next_node:Node):
        self.timer += self.graph.edges[self.position.id][next_node.id]
        #if the node is breakable, make all the edges including it -1
        if self.position.breakable:
            for i in range(len(self.graph.edges)):
                self.graph.edges[i][self.position.id] = -1
                self.graph.edges[self.position.id][i] = -1
        
        self.position = next_node
        self.graph.remove_target(self.position)
        self.people_on_board += self.position.num_of_people
        self.position.num_of_people = 0
        return next_node
    

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


def dijkstra_greedy(start:Node, graph:Graph):
    #returns shortest path to node with people
    #if no node with people, returns empty list
    shortestDists=[sys.maxsize]*len(graph.nodes)
    added=[False]*len(graph.nodes)
    shortestDists[start.id]=0
    parents=[None]*len(graph.nodes)
    #parents is array where each index contains the index of its parent in the shortest path
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
    if nearestIndex!= -1 and graph.get_node(nearestIndex).num_of_people>0:
        return getPath(start.id,parents,nearestIndex)
    return []
        

class StupidGreedyAgent(Agent):
    def __init__(self,graph:Graph, position:Node):
        super().__init__(position= position, graph=graph)

    def move(self):
        shortestPathToPeople = dijkstra_greedy(self.position, self.graph)
        print(shortestPathToPeople)
        if len(shortestPathToPeople)==0:
            self.isFinished()
        else:
            self.apply_move(self.graph.get_node(shortestPathToPeople[0]))

    def isFinished(self):
        shortestPathToPeople = dijkstra_greedy(self.position, self.graph)
        return len(shortestPathToPeople)==0