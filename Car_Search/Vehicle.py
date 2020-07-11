class Vehicle():

    def __init__(self, x, y, vel, r):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = r
        self.maxspeed = 5
        self.maxforce = 0.2
        self.reducesSpeed = False

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):
        
        desired = target - self.position
        
        if self.reducesSpeed:
            
            d = desired.mag()
            if (d < 100):
                m = map(d, 0, 101, 0, self.maxspeed)
                desired.setMag(m)
            else:
                desired.setMag(self.maxspeed)
        else:
            desired.setMag(self.maxspeed)
        steer = desired - self.velocity
        steer.limit(self.maxforce)
        self.applyForce(steer)
        
        #=====================Reduces speed===========

    
    def verifyCollision(self,obj1,obj2):
        return (obj1.position.x < (obj2.getX() + obj2.r) and (obj1.position.x + obj1.r) > obj2.getX()) and (obj1.position.y < (obj2.getY() + obj2.r) and (obj1.position.y + obj1.r) > obj2.getY())


    def display(self):
        # Draw a triangle rotated in the direction of velocity
        # text("Reduces Speed: {0}".format("On" if .reducesSpeed else "Off"),2,26)
        theta = self.velocity.heading() + PI / 2
        
        fill(127)
        noStroke()
        strokeWeight(1)
        
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r * 2)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
