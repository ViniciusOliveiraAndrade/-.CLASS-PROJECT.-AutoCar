class Vehicle():

    def __init__(self, i, j, r):
        self.i = i
        self.j = j
        self.r = r
        self.path = []

    def moveThroughPath(self):
        delay(100)
        if len(self.path) > 0:
            next = self.path[0]
            if self.i == next.i and self.j == next.j:
                self.path.pop(0)
                if len(self.path) > 0:
                    next = self.path[0]
                else:
                    return
            self.i = next.i
            self.j = next.j
    

    # def verifyCollision(self,obj1,obj2):
    #     return (obj1.position.x < (obj2.getX() + obj2.r) and (obj1.position.x + obj1.r) > obj2.getX()) and (obj1.position.y < (obj2.getY() + obj2.r) and (obj1.position.y + obj1.r) > obj2.getY())
    
    def verifyCollision(self,obj):
        return self.i == obj.i and self.j == obj.j
    
    def getX(self):
         return self.j * self.r
     
    def getY(self):
        return self.i * self.r
        
    def display(self):
        fill(250)
        noStroke()
        rect(self.getX()+4, self.getY()+4, self.r-8, self.r-8)
