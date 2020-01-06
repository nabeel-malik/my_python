class Cylinder:

    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height

    def volume(self):
        cylinder_vol = 3.142 * self.radius**2 * self.height
        print("The volume of the cylinder is {0}".format(cylinder_vol))

    def surface_area(self):
        cylinder_surf_area = (2 * 3.142 * self.radius**2) + (2 * 3.142 * self.radius * self.height)
        print("The surface area of the cylinder is {0}".format(cylinder_surf_area))


mycylinder = Cylinder(3,2)
mycylinder.volume()
mycylinder.surface_area()


