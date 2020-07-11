from Maze_Generator import Maze_Generator
from Vehicle import Vehicle
from Food import Food
from Score import Score

#Test

def setup():
    global maze, vehicle, food, score, title
    size(600, 400)
    title = 40
    maze = Maze_Generator(width, height, title, title) 
    
    maze.generateMaze(4,4)
    score = Score(0)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity, title/2)
    food = Food(random(maze.rows),random(maze.cols), title)
    print("Rows:{} Cols:{}".format(maze.rows,maze.cols))
    
def draw():
    background(51)
    
    vehicle.update()
    # food.update()
    
    maze.display()
    score.display()
    vehicle.display()
    food.display()
    
    # delay(1000)
    
    vehicle.seek(PVector(food.getX(),food.getY()))
    
    if vehicle.verifyCollision(vehicle,food):
        maze.mazeRestart()
        score.up()
        food.updatePosition(random(maze.rows),random(maze.cols))
        
     
