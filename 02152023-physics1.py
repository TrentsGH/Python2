from vector import vect
class obj:
    def __init__(self,mass=0,position=vect(),velocity=vect(),acceleration=vect(),space=None):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.space = space
        self.name = 'Object '
        self.space.bind(self)

    def __write__(self,x=None):
        out ="""Object Name : {0}
Mass        : {1} (kg)
Position    : {2} (m)
Velocity    : {3} (m/s)
Acceleration: {4} (m/s^2)
""".format(self.name, self.mass, self.position,
           self.velocity, self.acceleration)
        return out
    def __repr__(self):
        return self.__write__()
        
        
        

class space:
    def __init__(self):
        self.objects = []

    def bind(self,obj):
        self.objects.append(obj)
        obj.name+= '{}'.format(self.objects.index(obj)+1)
        

univ = space()
ball = obj(1,velocity = vect([1,0,0]),space = univ)
        
    

    
        
