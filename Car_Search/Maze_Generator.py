class Maze_Generator(object):
    def __init__(self, screen_width, screen_height, rows_size, cols_size):
        self.rows = int(screen_height / rows_size)
        self.cols = int(screen_width / cols_size)
        print("Rows:{} Cols:{}".format(self.rows,self.cols))
        self.rows_size = rows_size
        self.cols_size = cols_size
        self.stack = []
        self.generateGrid()
    
    def generateGrid(self):
        self.grid = []
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.cols):
                cell = Cell(i, j, self.cols_size, self.rows_size )
                self.grid[i].append(cell)
    
    def generateMaze(self, i , j):
        self.current_cell = self.grid[i][j] 
        self.current_cell.visited = True
        self.stack.append(self.current_cell)
        while len(self.stack) > 0:
            next_cell = self.checkNeighbors(self.current_cell)
            if next_cell is not None:
                next_cell.visited = True
                self.removeWalls(self.current_cell, next_cell)
                self.current_cell = next_cell
                self.stack.append(self.current_cell)
            else:
                self.current_cell = self.stack.pop(len(self.stack)-1)
        print("Maze Generator Has Finished!")
                
    
    def mazeRestart(self):
        self.generateGrid()
        self.generateMaze(0,0)
                                            
    def checkNeighbors(self, current_cell):
        neighbors = []
        
        if current_cell.i > 0 and not self.grid[current_cell.i - 1][current_cell.j].visited: #Verify top
            neighbors.append(self.grid[current_cell.i - 1][current_cell.j])
        
        if current_cell.j < self.cols -1 and not self.grid[current_cell.i][current_cell.j + 1].visited:  #Verify right
            neighbors.append(self.grid[current_cell.i][current_cell.j + 1])
        
        if current_cell.i < self.rows - 1 and not self.grid[current_cell.i + 1][current_cell.j].visited: #Verify botton
            neighbors.append(self.grid[current_cell.i + 1][current_cell.j])
        
        if current_cell.j > 0 and not self.grid[current_cell.i][current_cell.j -1].visited:              #Verify left
            neighbors.append(self.grid[current_cell.i][current_cell.j -1])
        
        if len(neighbors) > 0:
            return neighbors[int(random(len(neighbors)))]
        return None
                
    def getNeighbors(self, gridPoint):
        neighbors = []
        cell = self.grid[gridPoint.i][gridPoint.j]
        if cell.i > 0 and not self.grid[cell.i - 1][cell.j].walls[2] and not self.grid[cell.i - 1][cell.j].used(): #Verify top
            c = self.grid[cell.i - 1][cell.j]
            c.fron()
            neighbors.append(c)
        
        if cell.j < self.cols -1 and not self.grid[cell.i][cell.j + 1].walls[3] and not self.grid[cell.i][cell.j + 1].used():  #Verify right
            c = self.grid[cell.i][cell.j + 1]
            c.fron()
            neighbors.append(c)
        
        if cell.i < self.rows - 1 and not self.grid[cell.i + 1][cell.j].walls[0] and not self.grid[cell.i + 1][cell.j].used(): #Verify botton
            c = self.grid[cell.i + 1][cell.j]
            c.fron()
            neighbors.append(c)
        
        if cell.j > 0 and not self.grid[cell.i][cell.j -1].walls[1] and not self.grid[cell.i][cell.j -1].used(): #Verify left
            c = self.grid[cell.i][cell.j -1]
            c.fron()
            neighbors.append(c)
        
        if len(neighbors) > 0:
            return neighbors
        else:
            return []
                            
    def removeWalls(self, cell_a, cell_b):
        x = cell_a.j - cell_b.j
        if x == 1:
            cell_a.walls[3] = False
            cell_b.walls[1] = False
        elif x == -1:
            cell_a.walls[1] = False
            cell_b.walls[3] = False
        
        y = cell_a.i - cell_b.i
        if y == 1:
            cell_a.walls[0] = False
            cell_b.walls[2] = False
        elif y == -1:
            cell_a.walls[2] = False
            cell_b.walls[0] = False
    
    def displayCurrentCell(self):
        x = self.current_cell.j * self.current_cell.w_size
        y = self.current_cell.i * self.current_cell.h_size
        fill(0,0,255,100)
        rect(x, y, self.current_cell.w_size, self.current_cell.h_size)
    
    def display(self):
        for rows in self.grid:
            for cell in rows:
                cell.display()
                if len(self.stack) > 0:
                    self.displayCurrentCell()
    
class Cell(object):
    def __init__(self, i, j, w_size, h_size):
        self.i = i
        self.j = j
        self.w_size = w_size
        self.h_size = h_size
        self.walls = [True, True, True, True]
        self.visited = False
        self.expanded = False
        self.inFront = False
        self.isPath = False
        
    def fron(self):
        self.expanded = False
        self.inFront = True
    
    def ex(self):
        self.expanded = True
        self.inFront = False
    
    def pa(self):
        self.expanded = False
        self.inFront = False
        self.isPath = True
        
    def used(self):
        return self.expanded or self.inFront
    
    def getX(self):
         return self.j * self.w_size
    def getY(self):
        return self.i * self.h_size
    
    def display(self):
        x = self.j * self.w_size
        y = self.i * self.h_size
        
        if self.visited:
            noStroke()
            
            fill(255,255,255,100)
            
            rect(x, y, self.w_size, self.h_size)
            
            if self.inFront:
                fill (255,255,0)
                rect(x+1, y+1, self.w_size-2, self.h_size-2)
            if self.expanded:
                fill (0,255,0)
                rect(x+1, y+1, self.w_size-2, self.h_size-2)
            if self.isPath:
                fill (0,0,255)
                rect(x+1, y+1, self.w_size-2, self.h_size-2)
            
        stroke(255)
        strokeWeight(4)
        # fill(255,255,255)
        # text("i={} j={}".format(self.i, self.j), x +2, y+15)
        if self.walls[0]:
            line(x, y, x + self.w_size, y )
        if self.walls[1]:
            line(x + self.w_size, y, x + self.w_size, y + self.h_size )
        if self.walls[2]:
            line(x + self.w_size, y + self.h_size, x, y + self.h_size )
        if self.walls[3]:
            line(x, y + self.h_size, x, y)
