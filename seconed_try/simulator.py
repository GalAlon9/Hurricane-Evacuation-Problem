import networkx as nx
from Agents import GreedyAgent
from Agents import SaboteurAgent
# from agents import SaboteurAgent
from matplotlib import pyplot as plt



def parse(file:str):

    graph = nx.Graph()

    #open file
    f = open(file, 'r')
    #first line after "#N" is the number of nodes
    num_nodes = int(f.readline().split()[1])
    #next num_nodes lines are the nodes
    for i in range(num_nodes):
        line = f.readline().split()
        breakable = True if 'B'in line else False
        number_of_people = 0
        for cell in line:
            if 'P' in cell:
                number_of_people = int(cell[1:])

        graph.add_node(i+1, breakable=breakable, num_of_people=number_of_people)

    #add to the graph field for total number of people
    graph.graph['total_people'] = sum([graph.nodes[node]['num_of_people'] for node in graph.nodes])
    #read and throw away the next line
    f.readline()

    #rest of the file is the edges
    for line in f:
        line = line.split()
        if len(line) < 4:
            raise Exception("Invalid input")
        else:
            w = int(line[3][1])
            graph.add_edge(int(line[1]), int(line[2]), weight=w)

    return graph


def simulate(graph, agent):
    #receive start node
    start_position = int(input("Enter start position: "))
    agent = agent(graph, start_position)
    agent.people_on_board += graph.nodes[start_position]['num_of_people']
    graph.nodes[start_position]['num_of_people'] = 0
    
    while not agent.isFinished():
        #press enter to move
        input()
        agent.move()
        show_graph(graph)
        print("Score: \n", agent.getScore())
        print("People on board: \n", agent.people_on_board)


def show_graph(graph, pos=None):
    #plot the graph and show breakable nodes in red and non breakable in blue,
    #the number of people in each node is shown in the node like this: (id, num_of_people)
    # and the weight of each edge is shown next to the edge
    #and also show the position of the agent
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, nodelist=[node for node in graph.nodes if graph.nodes[node]['breakable']], node_color='r')
    nx.draw_networkx_nodes(graph, pos, nodelist=[node for node in graph.nodes if not graph.nodes[node]['breakable']], node_color='b')
    nx.draw_networkx_labels(graph, pos, labels={node: f"{node} ({graph.nodes[node]['num_of_people']})" for node in graph.nodes})
    nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, 'weight'))
    plt.show()
    



def main():
    graph = parse("seconed_try\input.txt")
    # show_graph(graph)
    simulate(graph,SaboteurAgent)

if __name__ == "__main__":
    main()