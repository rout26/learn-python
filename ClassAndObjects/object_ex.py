class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):

# The self parameter is a way for one function
# in the class to call another function in the
# class (and in the parent class).

    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()

class Giraffes(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots 
    def eat_leaves_from_trees(self):
        print('eating leaves') 



