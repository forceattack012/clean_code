class Car:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    
    
    def isSuperCar(self):
        return self.speed > 180

    def print_car(self):
        print('Car Name : '+self.name)
        print('Speed Car : '+ str(self.speed))
        print('Super car :' + str(self.isSuperCar()))



car = Car('Toyota',120)
car.print_car()
