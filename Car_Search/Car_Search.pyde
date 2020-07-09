from Maze_Generator import Maze_Generator

def setup():
    global maze
    size(600, 400)
    maze = Maze_Generator(width, height, 20, 20) 
    maze.generateMaze(4,4)
    
def draw():
    background(51)
    maze.display()
     
