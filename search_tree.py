# import graph as Graph
# import node as Node
# import heapq

# def deepCopyGraph(graph):
#     #returns copy of graph
#     nodes=[]
#     edges=[]
#     for node in graph.nodes:
#         nodes.append(Node.Node(node.id,node.num_of_people,node.breakable))
#     for edge in graph.edges:
#         edges.append(edge.copy())
#     return Graph.Graph(nodes,edges)

# class State:
#     def __init__(self, graph: Graph, parent, depth:int, current_node: Node):
#         self.graph = deepCopyGraph(graph)
#         self.parent = parent
#         self.depth = depth
#         self.current_node = current_node
#         self.score = 0
#         self.cost = 0

#     def set_score(self, score):
#         self.score = score

#     def set_cost(self, cost):
#         self.cost = cost

#     def is_goal(self):
#         #returns true if state is goal
#         return self.graph.people_to_save == 0
    
#     def __lt__(self, other):
#         #comparator for heap
#         return self.score < other.score



# def heuristic(state: State):
#     #returns heuristic value of state
#     return 0

# def A_star_heuristic(state: State):
#     return heuristic(state) + state.cost



# class SearchTree:
#     def __init__(self, start_state: State, heuristic):
#         self.start_state = start_state
#         self.fringe = []
#         heapq.heapify(self.fringe) #make fringe a heap
#         self.current_state = self.start_state
#         self.heuristic = heuristic

#     def add_to_fringe(self, state: State):
#         heapq.heappush(self.fringe, state)
        
    
#     def pop_state(self):
#         #returns the state with the lowest score
#         return heapq.heappop(self.fringe)
    
#     def expand(self, state: State):
#         # adds all the children of the state to the fringe
#         for node in state.graph.nodes:
#             #check if the node is reachable from the current node
#             if state.graph.edges[state.current_node.id][node.id] != -1:
#                 new_graph = deepCopyGraph(state.graph)
#                 new_graph.remove_target(node)
#                 new_graph.visit(node)
#                 new_state = State(new_graph, state, state.depth+1, node)
#                 #score = heuristic(new_state)
#                 score = 0 # remove this later
#                 new_state.set_score(score)
#                 cost = state.cost + state.graph.edges[state.current_node.id][node.id]
#                 new_state.set_cost(cost)
#                 self.add_to_fringe(new_state)
                
    
    

#     def search(self):
#         self.add_to_fringe(self.start_state)
#         while len(self.fringe) != 0:
#             self.current_state = self.pop_state()
#             if self.current_state.is_goal():
#                 return self.current_state
#             self.expand(self.current_state)
#         return None

    
        
#     def getMST(graph):
#         #returns MST of the graph
        
