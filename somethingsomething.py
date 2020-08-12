
import time

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

print(greeting(382))

from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

my_car = Car('red', 3812.4)

time.sleep(5)
