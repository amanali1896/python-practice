class Animal:
    def __init__(self, habitat, diet):  # it is a special methods. Dundar menthods. This method executes when an
        self.habitat = habitat  # instance of a class is  created #self is the instance of the class
        self.diet = diet

    def speak(self):  # self is very similar to "this" keyword
        print("I live in the " + self.habitat + " and eat " + self.diet)


animal_1 = Animal('jungle', 'meat')  # creating the instance
animal_1.speak()  # no need to pass "self". python does it on its own under the hood


class Lion(Animal):  # lion class extends animal class.
    def __init__(self, title, pride_size):  # very similar to constructor
        super().__init__('savanna', 'meat')  # refering to the super class
        self.title = title
        self.pride_size = pride_size

    def roar(self):
        print("I'm " + self.title + " of " + self.pride_size)


scar = Lion('outcast', '15')
scar.roar()
scar.speak()
