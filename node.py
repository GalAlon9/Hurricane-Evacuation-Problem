# a class for a node in graph
class Node:
    def __init__(self, id, breakable, num_of_people):
        self.id = id
        self.breakable = breakable
        self.num_of_people = num_of_people
        self.visited = False

    def __str__(self):
        return str(self.id)
    
    
