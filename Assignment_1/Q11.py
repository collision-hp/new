'''Duck typing in Python is a concept where the type or class of an object is less important than the methods it defines. If an object implements the methods expected by a piece of code, it can be used regardless of its actual type.'''

class Dog:
    def speak(self):
        return "Woof!"
class Robot:
    def speak(self):
        return "Beep!"
def describe(entity):
    print(entity.speak())

if __name__=="__main__":
    dog=Dog()
    robot=Robot()
    describe(dog)
    describe(robot)

