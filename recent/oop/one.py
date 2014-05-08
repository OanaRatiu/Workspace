class Array_queue(object):
    """docstring for Array_Queue"""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        >>> q = Array_queue()
        >>> q.enqueue(10)
        >>> q.items
        [10]

        >>> q.enqueue(11)
        >>> q.items
        [10, 11]

        >>> q.enqueue('aa')
        >>> q.items
        [10, 11, 'aa']

        """
        self.items.append(item)


    def dequeue(self, default=None):
        """
        >>> q = Array_queue()
        >>> q.enqueue(10)
        >>> q.enqueue(11)
        >>> q.dequeue()
        10
        >>> q.dequeue()
        11
        >>> q.dequeue()
        """
        try:
            return self.items.pop(0)
        except:
            return default


    def isEmpty(self):
        """
        >>> q = Array_queue()
        >>> q.isEmpty()
        True
        >>> q.enqueue(10)
        >>> q.isEmpty()
        False
        """
        return not self.items


    def contains(self, item):
        """
        >>> q = Array_queue()
        >>> q.enqueue(10)
        >>> q.enqueue(11)
        >>> q.contains(10)
        True
        >>> q.contains(7)
        False
        """
        return item in self.items


    def size(self):
        """
        >>> q = Array_queue()
        >>> q.size()
        0
        >>> q.enqueue(10)
        >>> q.size()
        1
        """
        return len(self.items)

    def __eq__(self, other):
        """
        >>> q1 = Array_queue()
        >>> q2 = Array_queue()

        >>> q1 == q2
        True

        >>> q1.enqueue(10)
        >>> q2.enqueue(10)
        >>> q1 == q2
        True

        >>> q1.enqueue(11)
        >>> q1 == q2
        False

        """
        try:
            for item in self.items:
                if not other.contains(item):
                    return False
            return True
        except:
            return False


if __name__ == '__main__':
    a = Array_queue()

    
        