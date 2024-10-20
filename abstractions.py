from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    print("i can walk")
class snake(animal):
    print("i can crawl")
class dog(animal):
    print("i can  bark")
h=human()
h.move()
s=snake()
s.move()
d=dog()
d.move()

 
