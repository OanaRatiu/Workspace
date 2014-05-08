from abc import ABCMeta, abstractmethod

class My_queue():
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def contains(self, item):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def compare_with_queue(self, queue)


class Array_queue(My_queue):
    """docstring for Array_Queue"""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        if not self.items:
            return True
        return False

    def contains(self, item):
        if item in self.items:
            return True
        return False

    def size(self):
        return len(self.items)

    def compare_with_queue:
        pass



if __name__ == '__main__':
    a = Array_queue()

    
        