from abc import ABC, abstractmethod
import networkx as nx

class Agent(ABC):
    def __init__(self, graph, position: int):
        self.graph = graph
        self.position = position
        self.people_on_board = 0
        # self.people_on_board = self.graph.nodes[self.position]['num_of_people']
        # self.graph.nodes[self.position]['num_of_people'] = 0
        self.timer = 0

    def getScore(self):
        return self.people_on_board * 1000 - self.timer

    @abstractmethod
    def move(self):
        pass

    def isFinished(self):
        return self.graph.graph['total_people'] == self.people_on_board

    def apply_move(self, next_node: int):
        self.timer += self.graph.edges[self.position, next_node]['weight']
        # if the node is breakable remove all the edges including it
        if self.graph.nodes[self.position]['breakable']:
            self.graph.remove_node(self.position)

        self.position = next_node
        self.people_on_board += self.graph.nodes[next_node]['num_of_people']
        self.graph.nodes[next_node]['num_of_people'] -= 0


class HumanAgent(Agent):

    def __init__(self, graph, position: int):
        super().__init__(graph, position)

    def move(self):
        # recieve input from user
        next_position: int = int(input("Enter your move: "))

        if self.graph.has_edge(self.position, next_position):
            self.apply_move(next_position)
            return 1

        print("Invalid move")
        return 0

class GreedyAgent(Agent):

    def __init__(self, graph, position: int):
        super().__init__(graph, position)

    def move(self):
        min_cost = float('inf')
        min_path = None
        next_node = None
        for node in self.graph.nodes:
            if node != self.position and self.graph.nodes[node]['num_of_people'] > 0:
                path = nx.dijkstra_path(self.graph, self.position, node)
                cost = nx.path_weight(self.graph, path, weight='weight')
                if cost < min_cost:
                    min_cost = cost
                    min_path = path

        next_node = min_path[1]
        print("the agent chose to go to node: ", next_node)
        self.apply_move(next_node)

class SaboteurAgent(Agent):

    def __init__(self, graph, position: int):
        super().__init__(graph, position)

    def move(self):
        min_cost = float('inf')
        min_path = None
        next_node = None
        for node in self.graph.nodes:
            if node != self.position and self.graph.nodes[node]['breakable'] == True:
                path = nx.dijkstra_path(self.graph, self.position, node)
                cost = nx.path_weight(self.graph, path, weight='weight')
                if cost < min_cost:
                    min_cost = cost
                    min_path = path
        if min_path is None:
            print("no breakable nodes")
            return 0
            
        next_node = min_path[1]
        print("the agent chose to go to node: ", next_node)
        self.apply_move(next_node)

    def isFinished(self):
        #if there is no breakable node left return true
        return not any(self.graph.nodes[node]['breakable'] for node in self.graph.nodes)


        
    
        
            


       