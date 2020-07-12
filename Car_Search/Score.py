class Score():

    def __init__(self):
        self.score = 0
    
    def display(self):
        fill(0)
        text("Score: {0}".format(self.score),2,11)
        
    def up(self):
        self.score+=1
