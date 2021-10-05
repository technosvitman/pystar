
from graph import *
import time


'''
    @brief graph compute class
'''
class Pystar():
    '''
        @brief initialize pystar
        @param start the start point
        @param target the target point
    '''
    def __init__(self, start : Node, target : Node):
        self.start = start
        self.target = target
        
    '''
        @brief buildPath
    '''
    def __buildPath(self, path):
        idx = path.indexof(self.target)
        path = path[:idx+1]
        while path[idx] != self.start and idx > 0 :
            while path[idx - 1] not in path[idx] and idx > 0:
                path.pop(idx-1)
                idx = idx - 1
            idx = idx - 1
        return path
        
    '''
        @brief find short path
    '''
    def originalfindPath(self):
        self.start.h = 0
        self.start.c = 0
        path = NodeList()
        worklist = NodePriorList()
        worklist.append(self.start)
        while len(worklist):
            n = worklist.pop()
            if n == self.target : 
                path.append(self.target)
                return self.__buildPath(path)
            else:
                for ne in n :
                    neidx = worklist.indexof(ne)
                    if not( ne in path or (neidx >= 0 and worklist[idx].c < n.c ) ) :
                        ne.c = n.c + 1
                        ne.h = ne.c + ( ne - self.target ) 
                        worklist.append(ne)
            path.append(n)
        return None
        
    '''
        @brief find short path
    '''
    def findPath(self):
        self.start.h = 0
        self.start.c = 0
        path = NodeList()
        path.append(self.start)
        i = 0
        while i < len(path):
            n = path[i]
            if n == self.target : 
                return self.__buildPath(path)
            else:
                i+=1
                for ne in n :
                    neidx = path.indexof(ne)
                    if not(neidx >= 0 and path[neidx].c < n.c ) :
                        ne.c = n.c + 1
                        ne.h = ne.c + ( ne - self.target ) 
                        if neidx >=0:
                            i = neidx
                        path.append(ne)
        return None

nl = NodeList()

# 0 5
nl.append(Node(2,0))
nl.append(Node(3,0))
nl.append(Node(4,0))
nl.append(Node(5,0))
nl.append(Node(6,0))
nl.append(Node(7,0))

# 6 14
nl.append(Node(0,1))
nl.append(Node(1,1))
nl.append(Node(2,1))
nl.append(Node(3,1))
nl.append(Node(4,1))
nl.append(Node(5,1))
nl.append(Node(6,1))
nl.append(Node(7,1))
nl.append(Node(8,1))

# 15 20
nl.append(Node(2,2))
nl.append(Node(3,2))
nl.append(Node(4,2))
nl.append(Node(5,2))
nl.append(Node(6,2))
nl.append(Node(7,2))

# 21 26
nl.append(Node(2,3))
nl.append(Node(3,3))
nl.append(Node(4,3))
nl.append(Node(5,3))
nl.append(Node(6,3))
nl.append(Node(7,3))

# 27 28
nl.append(Node(0,4))
nl.append(Node(8,4))

nl.link(0, 1)
nl.link(0, 8)
nl.link(1, 2)
nl.link(2, 3)
nl.link(3, 4)
nl.link(4, 5)

nl.link(6, 27)
nl.link(6, 7)
nl.link(7, 8)
nl.link(8, 15)
nl.link(9, 16)
nl.link(10, 17)
nl.link(11, 18)
nl.link(12, 19)
nl.link(13, 20)
nl.link(14, 28)

nl.link(15, 21)
nl.link(16, 22)
nl.link(17, 23)
nl.link(18, 24)
nl.link(19, 25)
nl.link(20, 26)

nl.link(21, 22)
nl.link(22, 23)
nl.link(23, 24)
nl.link(24, 25)
nl.link(25, 26)

nl.link(27, 28)


star = Pystar(nl[7], nl[14])
print("====>")
now = time.time()
print(star.originalfindPath())
print(time.time()-now)
print("====>")
now = time.time()
print(star.findPath())
print(time.time()-now)