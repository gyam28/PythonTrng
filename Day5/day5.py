# # class METHODS


class Car:

    number_of_wheels = 4
    datetime = True

    def __init__(self, brandname, year): #there can only be one init constructor
        self.brandname = brandname
        self.year = year

#CLASS METHODS
    @classmethod
    def setting(cls, number):
        cls.number_of_wheels = number

    @classmethod #instead of writing a long string and splitting it,longcoding
    def alternative_init(cls, string):
        brand,year,  = string.split("-")
        return cls(brand,year)
#STATIC METHOD - not so much used, because it cannot be interacted with it
    @staticmethod
    def today():
        return datetime.now()
class FlyingCar(Car):
    def __init__(self, brand, year, speed, number_of_wings):
        super().__init__(brand,year)
        self.speed = speed
        self.wings = number_of_wings

help(FlyingCar)

car_3 = Car.alternative_init("BMW-2000")
# print(car_3.__dict__)


car_1 = Car("BMW", 2000)
car_2 = Car("Audi",2005)

print(car_1.number_of_wheels)
print(car_2.number_of_wheels)
print(Car.number_of_wheels)

car_1.setting(6)

print(car_1.number_of_wheels)
# print(car_1.__dict__)
# print(car_2.__dict__)
# print(Car.__dict__)

#STATIC METHODS decorator @staticmethod
