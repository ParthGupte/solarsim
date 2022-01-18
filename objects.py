import vectors as vec
class Sun():
    def __init__(self,mass,position):
        self.mass = mass
        self.position = position

surya = Sun(1.989*(10**30),vec.vec([0,0,0]))

class Planet():
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position 
        self.velocity = velocity

prithvi = Planet(5.972*(10**24),vec.vec([152095295,0,0]),vec.vec([0,29.29*1000,0]))
