from .singly_linked_list import SLinkedList

class EmptyStackError(Exception):
    pass
class StackFull(Exception):
    pass

class stack(SLinkedList):
    def __init__(self,size=None):
        super().__init__()
        self.size = size

    def __repr__(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            output = [str(item) for item in self]
            return 'Top->'+ '-'.join(output) + '<-Bottom'

    def isEmpty(self):
        return False if self.head else True

    def isFull(self):
        if self.size:
            if self.size == self.len:
                return True
        else:
            return False

    def Push(self,value):
        if self.isFull():
            raise StackFull(f"Current stack of size={self.size} is full!")
        else:
            super().insertSLL(value=value,location=0)
    
    def Pop(self):
        if self.isEmpty():
            raise EmptyStackError
        else:
            del_value = super().deleteSLL(location=0)
            return del_value

    def Peek(self,bottom=False):
        if self.isEmpty():
            raise EmptyStackError
        else:
            if bottom:
                return self.tail.value
            else:
                return self.head.value

    def deleteStack(self):
        super().delcompleteSLL()
