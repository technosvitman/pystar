
from .graph import *
import time


'''
    @brief graph compute class
'''
class Pystar():
    METHOD_ASTAR=0
    METHOD_PYSTAR=1

    '''
        @brief initialize pystar
        @param start the start point
        @param target the target point
    '''
    def __init__(self, start : Node, target : Node, method=METHOD_ASTAR):
        self.start = start
        self.target = target
        self.__method=method
        
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
        @brief find short path using A* algorithm
    '''
    def __computeAstar(self):
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
                    if not( ne in path or (neidx >= 0 and worklist[neidx].c < n.c ) ) :
                        ne.c = n.c + 1
                        ne.h = ne.c + ( ne - self.target )
                        worklist.append(ne)
            path.append(n)
        return None
        
    '''
        @brief find short path using PyStar algorythm
    '''
    def __computePyStar(self):
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
                        path.insert(ne, i+1)
        return None
    
    ''' 
        @brief find path using selected method
    '''
    def findPath(self):
        if self.__method == Pystar.METHOD_ASTAR:
            return self.__computeAstar()
        elif self.__method == Pystar.METHOD_PYSTAR:
            return self.__computePyStar()
        else:
            return None