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


def setup():
    global vehicle, food, food_count
    size(640, 360)
    food_count = Food_count(0)
    velocity = PVector(0, 0)
    velocity2 = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    food = Food(random(width), random(height), velocity2)
    
def draw():
    background(255)
    fill(0)
    text("Food: {0}".format(food_count.food_count),20,25)
    
    vehicle.update()
    vehicle.display()
    food.update()
    food.display()
    vehicle.seek(food.position)

    
    if verifyCollision(vehicle,food):
        #food_count= food_count+1
        food_count.food_count+=1
        food.position = PVector(random(width),random(height))

   
    
def keyTyped():
    if key == ' ':
        vehicle.statusRS = not vehicle.statusRS

def verifyCollision(obj1,obj2):
    return (obj1.position.x < (obj2.position.x + obj2.r) and (obj1.position.x + obj1.r) > obj2.position.x) and (obj1.position.y < (obj2.position.y + obj2.r) and (obj1.position.y + obj1.r) > obj2.position.y)

class Food_count():

    def __init__(self,food_count):
        self.food_count = food_count

# def keyTyped():   
#      if key == 'a':       
#          vehicle.applyForce(PVector(-0.1,0))
#     elif key == 'd':
#         vehicle.applyForce(PVector(0.1,0))
#     elif key == 'w':
#         vehicle.applyForce(PVector(0,-0.1))
#     elif key == 's':
#         vehicle.applyForce(PVector(0,0.1))

# def keyReleased():
#     vehicle.velocity = PVector(0,0)
        
