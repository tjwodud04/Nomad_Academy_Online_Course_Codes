def plus(*args):
    result = 0
    for number in args:
        result += number
    return print(result)

plus(1,2,3,1,5,6,3,4,6,3,3,6,5,6,5,4)

'''result
63
'''

class Car():
    def __init__(self, **kwargs):
        print(kwargs)
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car with {self.wheels} wheels"

class Convertible(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
         return f"Car with no roof"

porche = Convertible(color="green", price="$40")
#porche.color = "Red"
#print(porche.color, porche.price)
print(porche.color)
'''
class 안의 function은 method
The First method that is given in python is self
'''

#print(dir(Car))
#mini = Car()
#print(mini.color, mini.price)