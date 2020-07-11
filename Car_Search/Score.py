class Score():

    def __init__(self, score):
        self.score = score
    
    def display(self):
        fill(0)
        text("Score: {0}".format(self.score),2,11)
        
    def up(self):
        self.score+=1
