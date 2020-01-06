class Line:

    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2
        self.x1 = cord1[0]
        self.x2 = cord2[0]
        self.y1 = cord1[1]
        self.y2 = cord2[1]

    def distance(self):
        line_dist = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        print("The length of the line is {0}".format(line_dist))

    def slope(self):
        line_slope = (self.y2 - self.y1) / (self.x2 - self.x1)
        print("The slope of the line is {0}".format(line_slope))


myline = Line((3,2), (8,10))
myline.distance()
myline.slope()


