# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle
from Food import Food
from Score import Score

def setup():
    global vehicle,food,score
    size(640, 360)
    score = Score(0)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    food = Food(random(6,width-6),random(6,height-6),PVector(0,0))
    

def draw():
    background(255)
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
    
def keyTyped():
    if key == ' ':
        vehicle.reducesSpeed = not vehicle.reducesSpeed

def verifyCollision(obj1,obj2):
    return (obj1.position.x < (obj2.position.x + obj2.r) and (obj1.position.x + obj1.r) > obj2.position.x) and (obj1.position.y < (obj2.position.y + obj2.r) and (obj1.position.y + obj1.r) > obj2.position.y)
