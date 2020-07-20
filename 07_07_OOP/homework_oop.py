class Human:
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        print("{}: I usually eat lots of {}!".format(self.name, food))

    def sleep(self, time):
        print("{}: And I want to sleep for {} hours!".format(self.name, time))

class Baby(Human):
    def eat(self, food):
        print("{}: I don't want to eat {}!".format(self.name, food))
    
    def say_something(self):
        print("{}: Bééé!".format(self.name))
    
    def sleep(self, time):
        print("{}: {} hours of sleep is not enough for me!".format(self.name, time))

class Adult(Human):
    def say_something(self):
        print("{}: I have to go to work, I am late!".format(self.name))

class Senior(Human):
    def eat(self, food):
        print("({} looks hungry at {}.)".format(self.name, food))
        super().eat(food)
   
    def say_something(self):
        print("{}: I need to find the biggest discounts!".format(self.name))

    def sleep(self, time):
        print("({} sees the number {} on the alarm clock.)".format(self.name, time))
        super().sleep(time)


lidi = [Baby('Honzík'), Adult('Jana'), Senior('Pepa')]

for human in lidi:
    human.say_something()
    human.eat('chocolate') 
    human.sleep('8')