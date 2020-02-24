

class Point:
    def __init__(self,index,X,Y,pix):
        self.index=index
        self.x=X
        self.y=Y
        self.pix=pix

    def displayPiont(self):
        print("The point is:({},{},{},{})".format(self.index,self.x,self.y,self.pix))
