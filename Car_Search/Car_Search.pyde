from Maze_Generator import Maze_Generator,Cell
from Vehicle import Vehicle
from Food import Food
from Score import Score

#Test

def setup():
    global maze, vehicle, food, score, title
    size(601, 401)
    title = 20
    
    maze = Maze_Generator(width, height, title, title) 
    maze.generateMaze(4,4)
    
    score = Score(0)
    
    velocity = PVector(0, 0)
    vehicle = Vehicle(0, 0, velocity, title)
    
    food = Food(random(maze.rows),random(maze.cols), title)
    path=[]
    path.append(Cell(0,0, title,title))
    path.append(Cell(1,0, title,title))
    path.append(Cell(2,0, title,title))
    path.append(Cell(3,0, title,title))
    path.append(Cell(3,1, title,title))
    path.append(Cell(3,2, title,title))
    path.append(Cell(3,3, title,title))
    
    vehicle.path = path[:]
    
    
    
def draw():
    background(51)
    
    # vehicle.update()
    # food.update()
    
    maze.display()
    score.display()
    vehicle.display()
    food.display()
    
    delay(1000)
    
    vehicle.moveThroughPath()
    
    # vehicle.seek(PVector(food.getX(),food.getY()))
    
    if vehicle.verifyCollision(food):
        maze.mazeRestart()
        score.up()
        food.updatePosition(random(maze.rows),random(maze.cols))
    
