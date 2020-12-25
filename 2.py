from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def textile_spend(self):
        pass

class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    def textile_spend(self):
        return self.size/6.5 + 0.5

class Costume(Clothes):

    def __init__(self, growth):
        self.growth = growth

    @property
    def textile_spend(self):
        return 2*self.growth + 0.3

example = Coat(10)
print(example.textile_spend())

example_2 = Costume(170)
print(example_2.textile_spend)