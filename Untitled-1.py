#!/usr/bin/env python

import threading
import time

'''
class MyThread(threading.Thread):
    def run(self):                                         # Default called function with mythread.start()
        print("{} started!".format(self.getName()))        # "Thread-x started!"
        time.sleep(1)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))       # "Thread-x finished!"

def main():
    for x in range(4):                                     # Four times...
        mythread = MyThread(name = "Thread-{}".format(x))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread, run method will be invoked
        time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another

if __name__ == '__main__':
    main()
'''


class  MyClass:
    x = 5

print(MyClass())

p1 = MyClass()

print(p1.x)
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
'''




class User:
  def __init__(self, first_name, inventory):
    self.first_name = first_name
    self.inventory = inventory

peter = User("peter", 36)
nick = User("nick")

print(user.first_name)
print(user.inventory)


