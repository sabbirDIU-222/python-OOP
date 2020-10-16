class Triangle :

    def __init__(self,base,height):
        self.base = base
        self.height = height



    def calculateArea(self):
        return self.base * self.height


amrjomin = Triangle(10,10)
o = amrjomin.calculateArea()
print(o)

