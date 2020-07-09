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
    food = Food(random(6,width-6),random(6,height-6),PVector(0,0), title/2)
    
    
def draw():
    background(51)
    maze.display()
    
    fill(0)
    text("Score: {0}".format(score.score),2,11)
    text("Reduces Speed: {0}".format("On" if vehicle.reducesSpeed else "Off"),2,26)
    vehicle.update()
    vehicle.display()
    
    food.update()
    food.display()
    
    vehicle.seek(food.position)
    
    if verifyCollision(vehicle,food):
        score.score+=1
        food.position = PVector(random(width-6),random(height-6))
     
def verifyCollision(obj1,obj2):
    return (obj1.position.x < (obj2.position.x + obj2.r) and (obj1.position.x + obj1.r) > obj2.position.x) and (obj1.position.y < (obj2.position.y + obj2.r) and (obj1.position.y + obj1.r) > obj2.position.y)
