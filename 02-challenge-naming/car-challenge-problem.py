class Entity:
    def __init__(self,x,speed):
        self.x = x
        self.speed = speed
    
    
    def superCar(self):
        return self.speed > 180

def output(car):
    print('Car Name : '+car.x)
    print('Speed Car : '+ str(car.speed))
    print('Super car :' + str(car.superCar()))

x = 'Toyota'

car = Entity(x,120)
output(car)
