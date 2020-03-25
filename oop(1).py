# a = 10
# b = 20
# everything in python is objects unlike java or c ++
# click ctrl one __add__ and + to know more
# print(a + b)
# print(a.__add__(b))


class Kettle(object):
    # class attribute that all instances share // this is similar to static field in java but not exactly same
    power_source = "electricity"

    # difference between functions and methods inside a class is the self keyword that is present as an argument
    # self is just a name we can use any other name but convention is so well established to use self as variable name
    # self is a reference to the instance of the class
    # __init__ is used to initialise a class method along with variables
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


# creating instance of the class Kettle
kenwood = Kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.99
print(kenwood.price)

# creating instance of the class Kettle
hamilton = Kettle("hamilton", 14.99)
print(hamilton.price)
print(hamilton.make)

hamilton.price = 15.99
print(hamilton.price)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

# the variable on is intialized as False in init
print(hamilton.on)
# the variable on is changed to True as declared in hamilton method
hamilton.switch_on()
print(hamilton.on)
Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

# class attributes

print("*" * 80)
# kenwood instance has power attributed because we dynamically assign it now.
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print(Kettle.power_source)

print(kenwood.power_source)

print(hamilton.power_source)

# we can access name space by __dict__ attribute
print("switch to atomic power")
# the below line doesn't change the static class attribute
Kettle.power_source = "atomic"
# the below line changes kenwood variable power_source to gas
print("change kenwood to gas")

kenwood.power_source = "gas"
print(kenwood.power_source)

print(Kettle.__dict__)

print(kenwood.__dict__)

print(hamilton.__dict__)