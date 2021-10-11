
import math

'''
    @brief list of node 
'''
class NodeList():

    '''
        @brief create Node
    '''
    def __init__(self):
        self.nodes = []

    '''
        @brief get item
        @param index the index to get
        @return the result
    '''
    def __getitem__(self, index) :
        return self.nodes[index]

    '''
        @brief get list len
        @return the result
    '''
    def __len__(self) :
        return len(self.nodes)

    '''
        @brief append item
        @param node the node to append
    '''
    def append(self, node) :
        if node not in self :
            self.nodes.append(node)

    '''
        @brief insert item
        @param node the node to append
        @param index insertion index
    '''
    def insert(self, node, index) :
        if node not in self :
            self.nodes.insert(index, node)

    '''
        @brief pop item
        @param idx the idx to pop
    '''
    def pop(self, idx=0) :
        return self.nodes.pop(idx)

    '''
        @brief link nodes
        @param a index of first node
        @param b index of second node
    '''
    def link(self, a, b) :
        self.nodes[a].append(self.nodes[b])
    
    '''
        @brief find object regarding its coords
        @param value the value to find
    '''
    def indexof(self, value):
        for n in range(len(self.nodes)):
            if self.nodes[n] == value:
                return n
        return -1
        
    '''
        @brief get string
    '''
    def __str__(self):
        return str(self.nodes)
        
    '''
        @brief get string representation
    '''
    def __repr__(self):
        return "NodeList"+str(self)
    
    