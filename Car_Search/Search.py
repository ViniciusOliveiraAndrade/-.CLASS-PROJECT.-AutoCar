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
        self.depthLimit = 4
        
    def restart(self,maze, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.maze = maze
        self.first = True
        self.frontier = []
        self.hasPath = False
        self.path = []            
        self.depth = 0
        self.depthLimit = 4
        
        
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
        
    def dlsAddFrontier(self,states, path, index = 0):
        temp = []
        for cell in states:
            temp.append(State(cell, path=path, depth=self.depth))
        if index == 0:
            temp.extend(self.frontier)
            self.frontier = temp
        else : 
            aux_1 = self.frontier[:index]
            aux_2 = self.frontier[index:]
            aux_1.extend(temp)
            aux_1.extend(aux_2)
            self.frontier = aux_1
    
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
  
    def dlsGetState(self):
        interections = 0
        for i, state in enumerate(self.frontier):
            if state.depth <= self.depthLimit:
                if state.depth <= self.depth:
                    self.depth = state.depth + 1
                return self.frontier.pop(i), i
        
            interections = interections + 1
        if len(self.frontier) == interections:
            self.depthLimit = self.depthLimit + 3
        return self.dlsGetState()
                                                                    
    def search(self, type = 1): #largura
        index = 0
        if not self.hasPath:
            self.maze.display()
            delay(100)
            if self.first:
                cell = self.maze.grid[self.startPoint.i][self.startPoint.j]
                self.first = False
                state = State(cell)
                if type == 3:
                    self.dlsAddFrontier([state.gridPonit], state.path)
                else:
                    self.frontier.append(state)
                cell.fron()
                # self.printFrontier()
            
            else :
                if type == 3:
                    state, index = self.dlsGetState()
                else:
                    state = self.frontier.pop(0)
                state.gridPonit.ex()
                if not self.verifyEndState(state.gridPonit): # and len(self.frontier) > 0
                    if type == 1: # BFS
                        self.bfsAddFrontier(self.maze.getNeighbors(state.gridPonit), state.path)
                    elif type == 2:# DFS
                        self.dfsAddFrontier(self.maze.getNeighbors(state.gridPonit), state.path)
                    elif type == 3:# DLS
                        self.dlsAddFrontier(self.maze.getNeighbors(state.gridPonit), state.path)
                    elif type == 4:# Greedy
                        self.greedyAddFrontier(self.maze.getNeighbors(state.gridPonit), state.path)
                    elif type == 5:# A Star
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
