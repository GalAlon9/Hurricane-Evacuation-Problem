# from graph import Graph
# from node import Node
import heapq



class State:
    def __init__(self, depth:int, current_node: int, parent: int, targets, broken):
        self.parent = parent
        self.depth = depth
        self.current_node = current_node
        self.score = 0
        self.cost = 0
        self.targets = targets
        self.broken  = broken
        

    def set_score(self, score):
        self.score = score

    def set_cost(self, cost):
        self.cost = cost

    def is_goal(self):
        if len(self.targets) == 0:
            return True
        return False
    
    def __lt__(self, other):
        #comparator for heap
        return self.score < other.score

class SearchTree:
    def __init__(self, start_state: State, heuristic, graph):
        self.start_state = start_state
        self.fringe = []
        heapq.heapify(self.fringe) #make fringe a heap
        self.current_state = self.start_state
        self.heuristic = heuristic
        self.graph = graph

    def add_to_fringe(self, state: State):
        heapq.heappush(self.fringe, state)
        
    
    def pop_state(self):
        #returns the state with the lowest score
        return heapq.heappop(self.fringe)
    
    def expand(self, state: State):
        #add all the possible states to the fringe
        for node in self.graph.nodes:
            if node != state.current_node:
                if node in self.graph.neighbors(state.current_node):
                    if node not in state.broken:
                        targets = state.targets.copy()
                        if node in targets:
                            targets.remove(node)
                        broken = state.broken.copy()
                        if self.graph.nodes[node]['breakable']:
                            broken.append(node)
                        new_state = State(state.depth+1, node, state.current_node, targets, broken)
                        new_state.set_cost(state.cost + self.graph.edges[state.current_node][node])
                        new_state.set_score(self.heuristic(new_state))
                        self.add_to_fringe(new_state)

    

    def search(self):
        self.add_to_fringe(self.start_state)
        while len(self.fringe) != 0:
            self.current_state = self.pop_state()
            if self.current_state.is_goal():
                return self.current_state
            self.expand(self.current_state)
        return None

    
    def get_path(self, state: State):
        path = []
        while state.parent != None:
            path.append(state.current_node)
            state = state.parent
        path.append(state.current_node)
        return path[::-1]