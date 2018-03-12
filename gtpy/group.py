from abc import ABC, abstractmethod

class AbstractElement(ABC):
    def __init__(self,value):
        self.value = value

    @abstractmethod
    def get_invers(self):
        pass

class AdditiveElement(AbstractElement):
    def get_invers(self):
        return 0-self.value

class MultiplicativeElement(AbstractElement):
    def get_invers(self):
        return 1/self.value
