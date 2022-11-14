import os
from graph import Graph
from node import Node

#get text from a file and parse it a global variable graph
def parse(file:str):
    #open file
    f = open(file, 'r')
    #first line after "#N" is the number of nodes
    num_nodes = int(f.readline().split()[1])
    #next num_nodes lines are the nodes
    nodes = []
    for i in range(num_nodes):
        line = f.readline().split()
        breakable = True if 'B'in line else False
        number_of_people = 0
        for cell in line:
            if 'P' in cell:
                number_of_people = int(cell[1:])

        nodes.append(Node(i, breakable, number_of_people))
            
    #next line is empty
    f.readline()
    # create matrix size num_nodes*num_nodes and fill it with -1
    edges = [[-1 for i in range(num_nodes)] for j in range(num_nodes)]
    #rest of the file is the edges
    for line in f:
        line = line.split()
        if len(line) < 4:
            raise Exception("Invalid input")
        else:
            w = int(line[3][1])
            edges[int(line[1])-1][int(line[2])-1] = w
            edges[int(line[2])-1][int(line[1])-1] = w
   
    return Graph(nodes, edges)

           

