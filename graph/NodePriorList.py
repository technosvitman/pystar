
import math
from .NodeList import NodeList

'''
    @brief Priority list of node reagarding 
'''
class NodePriorList(NodeList):

    '''
        @brief compare two nodes priority
        @param a the index of the first node to compare
        @param b the index of the second one
    '''
    def __compare(self, a, b):
        if self.nodes[a] > self.nodes[b]:
            return 1
        elif self.nodes[a] < self.nodes[b]:
            return -1
        else:
            return 0
    
    '''
        @brief pop the highest priority in list
    '''
    def pop(self):
        idx = 0
        for n in range(1, len(self)):
            if self[n] < self[idx] : 
                idx = n
        return self.nodes.pop(idx)
        
    '''
        @brief get string representation
    '''
    def __repr__(self):
        return "NodePriorList"+str(self)
        
    
    