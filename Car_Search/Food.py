# The "Food" class

class Food():

    def __init__(self, i, j, r):
        self.i = int(i)
        self.j = int(j)
        self.r = r

    # Method to update location
    def updatePosition(self, i, j):
        self.i = int(i)
        self.j = int(j)
        print("i: {} j: {}".format(int(i),int(j)))
    
    def getX(self):
         return self.j * self.r
     
    def getY(self):
        return self.i * self.r
        
    def display(self):
        fill(255,0,0)
        noStroke()
        rect(self.getX()+4, self.getY()+4, self.r-8, self.r-8)
        
