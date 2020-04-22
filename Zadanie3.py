from math import *
import sys

class Kwadrat:

    def __init__(self, x):
        self.x = x
        self.y = x
    def __add__(self,other):
        return self.x + other.x
    def __ge__(self, other):
            return self.x
    def __gt__(self, other):
            return self.x
    def __le__(self, other):
        return other.x
    def __lt__(self, other):
            return other.x


kw1 = Kwadrat(50)
kw2= Kwadrat(5)
kw3= kw1 >= kw2
kw4= kw1 > kw2
kw5= kw1 <= kw2
kw6= kw1 < kw2
print(kw3)
print(kw4)
print(kw5)
print(kw6)