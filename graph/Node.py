
import math

'''
    @brief Node entity
    x : x position
    y : y position
    c : cost
    h : heuristic
'''
class Node():

    '''
        @brief create Node
    '''
    def __init__(self, x=0, y=0):
        self.c = 0
        self.h = 0
        self.x = x
        self.y = y
        self.neighbours = []

    '''
        @brief iterate neighbours
    '''
    def __iter__(self) :
        return iter(self.neighbours)

    '''
        @brief append neighbour
        @param node the node to append
    '''
    def append(self, node) :
        if node not in self.neighbours :
            self.neighbours.append(node)
            node.append(self)

    '''
        @brief get distance
        @param value the other value
        @return the result
    '''
    def __sub__(self, value) :
        if isinstance(value, Node):
            dx = self.x - value.x
            dy = self.y - value.y
            return math.sqrt(dx * dx + dy * dy)
        else:
            return None

    '''
        @brief compare if position are equal
        @param value the other value
        @return the result
    '''
    def __eq__(self, value) :
        if isinstance(value, Node):
            return self.x == value.x and self.y == value.y
        else:
            return False

    '''
        @brief check if has greater heuristic
        @param value the other value
        @return the result
    '''
    def __gt__(self, value) :
        if isinstance(value, Node):
            return self.h > value.h
        else:
            return False

    '''
        @brief check if has lower heuristic
        @param value the other value
        @return the result
    '''
    def __lt__(self, value) :
        if isinstance(value, Node):
            return self.h < value.h
        else:
            return False
        
    '''
        @brief get string
    '''
    def __str__(self):
        return f"( ( %s, %s), cost=%d, heuristic=%s )"%(str(self.x), str(self.y), self.c, str(self.h)) 
        
    '''
        @brief get string representation
    '''
    def __repr__(self):
        return "Node"+str(self)
    
    