class Vehicle:
    def start_engine(self):
        print("Vehicle engine started")

class Car(Vehicle):
    def play_music(self):
        print("Playing music in the car")

class ElectricCar(Car):
    def charge_battery(self):
        print("Battery is charging")

vehicle = Vehicle()
vehicle.start_engine()


car=Car()
car.start_engine()
car.play_music()

electric_car=ElectricCar()
electric_car.start_engine()
electric_car.play_music()
electric_car.charge_battery()
