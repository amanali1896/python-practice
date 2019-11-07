class Animal:
    def __init__(self):  # it is a special methods. Dundar menthods. This method executes when an
        self.habitat = 'jungle'  # instance of a class is  created #self is the instance of the class
        self.diet = 'meat'

    def speak(self):  # self is very similar to "this" keyword
        print("I live in the " + self.habitat + " and eat " + self.diet)


animal_1 = Animal()  # creating the instance
animal_1.speak()  # no need to pass self. python does it on its own under the hood
