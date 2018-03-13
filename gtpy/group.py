from abc import ABC, abstractmethod

class AbstractElement(ABC):
    """
    This is an sample of element
    from
    """
    def __init__(self,value):
        self.value = value

    @abstractmethod
    def get_invers(self):
        pass

class AbstractGroup(ABC):
    def __init__(self,elements):
        self.elements = elements
        self.__complete()

    def __complete(self):
        for element in self.elements:
            if not element.get_invers() in self.elements:
                self.elements.add(element.get_invers())

    def add_element(self,element):
        self.elements.add(element)
        self.__complete()

class AdditiveElement(AbstractElement):
    def get_invers(self):
        return 0-self.value


class MultiplicativeElement(AbstractElement):
    def get_invers(self):
        return 1/self.value
