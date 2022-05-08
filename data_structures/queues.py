from .singly_linked_list import SLinkedList

class EmptyQueueError(Exception):
    pass
class QueueFull(Exception):
    pass

class queue(SLinkedList):
    def __init__(self,size=None):
        super().__init__()
        self.size = size

    def __repr__(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            output = [str(item) for item in self]
            return 'First->'+ '<-'.join(output) + '<-Last'

    def isEmpty(self):
        return False if self.head else True

    def isFull(self):
        if self.size:
            if self.size == self.len:
                return True
        else:
            return False

    def Enqueue(self,value):
        if self.isFull():
            raise QueueFull(f"Current queue of size={self.size} is full!")
        else:
            super().insertSLL(value=value,location=-1)
    
    def Dequeue(self):
        if self.isEmpty():
            raise EmptyQueueError
        else:
            del_value = super().deleteSLL(location=0)
            return del_value

    def Peek(self,last=False):
        if self.isEmpty():
            raise EmptyQueueError
        else:
            if last:
                return self.tail.value
            else:
                return self.head.value

    def deleteQueue(self):
        super().delcompleteSLL()
