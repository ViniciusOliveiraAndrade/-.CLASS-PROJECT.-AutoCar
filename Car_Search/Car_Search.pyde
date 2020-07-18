from Maze_Generator import Maze_Generator
from Vehicle import Vehicle
from Food import Food
from Score import Score
from Search import Search, GridPoint


def setup():
    global maze, vehicle, food, score, title, search
    size(601, 401)
    title = 40
    
    maze = Maze_Generator(width, height, title, title) 
    maze.generateMaze(4,4)
    
    score = Score()
    
    vehicle = Vehicle(0, 0, title)
    
    food = Food(random(maze.rows),random(maze.cols), title)
    
    search = Search(maze, GridPoint(vehicle.i, vehicle.j), GridPoint(food.i, food.j))

    
def draw():
    background(51)
    # search.bfs()
    search.dfs()
    maze.display()
    score.display()
    vehicle.display()
    food.display()
    
    
    if search.hasPath:
        vehicle.path = search.path
        vehicle.moveThroughPath()
        
    
        if vehicle.verifyCollision(food):
            maze.mazeRestart()
            score.up()
            food.updatePosition(random(maze.rows),random(maze.cols))
            search.restart(maze, GridPoint(vehicle.i, vehicle.j), GridPoint(food.i, food.j))
    
