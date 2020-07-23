import math
class Search (object):
    def __init__(self,maze, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.maze = maze
        self.first = True
        self.frontier = []
        self.hasPath = False
        self.path = []
        self.depth = 0
        
    def restart(self,maze, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.maze = maze
        self.first = True
        self.frontier = []
        self.hasPath = False
        self.path = []            
        self.depth = 0
        
        
    def verifyEndState(self,p):
        return p.i == self.endPoint.i and p.j == self.endPoint.j 
    
    def bfsAddFrontier(self,states, path):
        for cell in states:
            self.frontier.append(State(cell, path=path))
        # self.printFrontier()
    
    def dfsAddFrontier(self,states, path):
        temp = []
        for cell in states:
            temp.append(State(cell, path=path))
        temp.extend(self.frontier)
        self.frontier = temp
    
    def greedyAddFrontier(self,states, path):
        for cell in states:
            self.frontier.append(State(cell, fh = self.eucliDist(cell.i,cell.j, self.endPoint.i, self.endPoint.j), path=path))
        self.frontier.sort(key=lambda x: x.fh)
    
    def aStarAddFrontier(self,states, path, cost):
        for cell in states:
            self.frontier.append(State(cell, fg = cost, fh = self.eucliDist(cell.i,cell.j, self.endPoint.i, self.endPoint.j),  path=path))
        self.frontier.sort(key=lambda x: x.fn)
    
    def eucliDist(self, x0, x1, y0, y1):
        return math.sqrt(((x0 - y0) ** 2) + ((x1 - y1) ** 2))                
                                    
    def search(self, type = 1): #largura
        if not self.hasPath:
            self.maze.display()
            # delay(100)
            if self.first:
                cell = self.maze.grid[self.startPoint.i][self.startPoint.j]
                self.first = False
                state = State(cell)
                self.frontier.append(state)
                cell.fron()
                # self.printFrontier()
            
            else :
                state = self.frontier.pop(0)
                state.gridPonit.ex()
                if not self.verifyEndState(state.gridPonit): # and len(self.frontier) > 0
                    if type == 1: # BFS
                        self.bfsAddFrontier(self.maze.getNeighbors(state.gridPonit), state.path)
                    elif type == 2:# DFS
                        self.dfsAddFrontier(self.maze.getNeighbors(state.gridPonit), state.path)
                    elif type == 3:# Greedy
                        self.greedyAddFrontier(self.maze.getNeighbors(state.gridPonit), state.path)
                    elif type == 4:# A Star
                        self.aStarAddFrontier(self.maze.getNeighbors(state.gridPonit), state.path, state.fg)
                    else:
                        self.bfsAddFrontier(self.maze.getNeighbors(state.gridPonit), state.path)
                else:
                    self.path = state.path
                    self.hasPath = True
                    for c in self.path:
                        c.pa()
                                        
    
    def printFrontier(self):
        s = ""
        for i, state in enumerate(self.frontier):
            s+=" | i:{} j:{}".format( state.gridPonit.i, state.gridPonit.j)
        
        print(s)
    def printPath(self):
        s = ""
        for i, state in enumerate(self.path):
            s+=" | i:{} j:{}".format( state.i, state.j)
        
        print(s)

class State(object):
    def __init__(self, gridPonit, fg = 0, fh = 0, path = [], depth = 0):
        self.gridPonit = gridPonit
        self.fg = fg
        self.fh = fh
        self.fn = self.fg + self.fh
        self.path = path[:]
        self.path.append(gridPonit)
        self.depth = depth

class GridPoint(object):
    def __init__(self, i, j):
        self.i = i
        self.j = j
