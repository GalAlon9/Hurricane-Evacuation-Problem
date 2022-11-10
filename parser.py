from graph import Graph

from .node import Node


#get text from a file and parse it a global variable graph
def parse(file):
    #open file
    f = open(file, 'r')
    #first line after "#N" is the number of nodes
    num_nodes = int(f.readline().split()[1])
    #next num_nodes lines are the nodes
    nodes = []
    for i in range(num_nodes):
        line = f.readline().split()
        if len(line) == 1 :
            nodes.append(Node(i, False,0))
        elif len(line) == 2:
            if line[1] == 'B':
                nodes.append(Node(i, True,0))
            else:
                num_of_people = int(line[1][1])
                nodes.append(Node(i, False,num_of_people))
        elif len(line) == 3:
            num_of_people = int(line[1][1])
            nodes.append(Node(i, True,num_of_people))
        else:
            raise Exception("Invalid input")
    #next line is empty
    f.readline()
    # create matrix size num_nodes*num_nodes and fill it with -1
    edges = [[-1 for i in range(num_nodes)] for j in range(num_nodes)]
    #rest of the file is the edges
    for line in f:
        line = line.split()
        if len(line) != 4:
            raise Exception("Invalid input")
        else:
            w = int(line[3][1])
            edges[int(line[1])][int(line[2])] = w
    
    #create global variable graph
    global graph
    graph = Graph(nodes, edges)
    close(file)

           
    

    
