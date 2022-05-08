# %%
class InvalidLocationError(Exception):
    pass
class EmptyLinkedList(Exception):
    pass


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class CDLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            if node == self.head:
                break
    
    def __repr__(self):
        if not self.len:
            raise EmptyLinkedList

        output = [str(item) for item in self]
        return '->'.join(output)

    def traverseCDLL(self):
        if not self.len:
            raise EmptyLinkedList
        else:
            node = self.head
            print('Head',sep='',end='')
            while node:
                print('<->',node.value,sep='',end='')
                node = node.next
                if node == self.head:
                    break
            print('<->Tail<->Head')
            print(f'head: {self.head.value} tail: {self.tail.value} tail.next: {self.tail.next.value} head.prev: {self.head.prev.value} len: {self.len}')

    def searchCDLL(self,value):
        if self.head is None:
            raise EmptyLinkedList
        else:
            node = self.head
            i=0
            while node:
                if node.value == value:
                    return True, i
                node = node.next
                if node == self.head:
                    break
                i+=1
            
            print(f'{value} not found in the linked List')
            return False

    
    def insertCDLL(self,value,location=-1): ## default location in the end
        if location<-1 or location>self.len:
            raise InvalidLocationError(f'location should be -1 or between 0 to len (inclusive)')
        
        newNode = Node(value)

        if self.head is None: ## empty linked list O(1) S&T
            self.head = newNode
            self.tail = self.head
            newNode.next = self.head
            newNode.prev = self.head
            self.len += 1

        else:

            if location==0: ## at head -> new head O(1) S&T
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = self.head
                self.head.prev = self.tail

                self.len += 1

            elif location==-1 or location==self.len: ## insert after tail -> new tail O(1) S&T
                self.tail.next = newNode
                newNode.prev = self.tail
                newNode.next = self.head
                self.tail = newNode
                self.head.prev = self.tail
                self.len += 1
            
            elif location<self.len: ## O(n) Time and O(1) Space
                tempNode = self.head
                for i in range(1,location):
                    tempNode = tempNode.next
                
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.prev = tempNode
                newNode.next = nextNode
                nextNode.prev = newNode

                self.len += 1

    def deleteCDLL(self,location=-1):
        if location<-1 or location>self.len-1:
            raise InvalidLocationError('Location should be -1 or between 0 and len-1 (both inclusive)')

        if self.head is None:
            raise EmptyLinkedList
        
        else:
            if location == 0: ## O(1) S&T
                if self.len<=1:
                    self.head.next, self,head,prev = None, None
                    self.head, self.tail = None, None
                else:
                    firstNode = self.head
                    self.head = firstNode.next
                    firstNode.next, firstNode.prev = None, None
                    self.tail.next = self.head
                    self.head.prev = self.tail

                self.len -= 1

            elif location==-1 or location==self.len-1: ## O(1) S&T
                prevNode = self.tail.prev
                self.tail.next,self.tail.prev =None, None
                self.tail = prevNode
                self.tail.next = self.head
                self.head.prev = self.tail
                
                self.len -= 1
            
            elif location<self.len: ## O(n) S&T
                tempNode = self.head
                for i in range(1,location):
                    tempNode = tempNode.next

                nextNode = tempNode.next
                tempNode.next = nextNode.next
                tempNode.next.prev = tempNode
                
                nextNode.prev, nextNode.next = None, None

                self.len -= 1

    def deletecompleteCDLL(self):
        if self.head is None:
            raise EmptyLinkedList
        else:
            node = self.head
            while node:
                tempNode = node.next
                node.next, node.prev = None, None
                self.head = tempNode
                node = tempNode
                self.len -= 1
                if node == self.tail:
                    self.len -= 1
                    break
            self.head, self.tail = None, None
    
    def createCDLL(self,valuelist):
        try:
            self.deletecompleteCDLL()
        except EmptyLinkedList:
            pass

        self.head = Node(valuelist[0])
        self.len += 1
        node = self.head
        for item in valuelist[1:]:
            node.next = Node(item)
            node.next.prev = node
            node = node.next
            self.len += 1
        self.tail = node
        node.next = self.head
        self.head.prev = self.tail


# %%
if __name__ == '__main__':
    CDLL = CDLinkedList()
    try:
        print(CDLL)
    except EmptyLinkedList:
        print('empty linked list!')

    CDLL.insertCDLL(value=1,location=-1)
    CDLL.insertCDLL(value=2,location=-1)
    CDLL.insertCDLL(value=3,location=-1)
    CDLL.insertCDLL(value=4,location=-1)
    CDLL.insertCDLL(value=5,location=-1)
    CDLL.insertCDLL(value=6,location=-1)
    print(CDLL)
    CDLL.traverseCDLL()
    
    CDLL.deletecompleteCDLL()

    try:
        print(CDLL)
    except EmptyLinkedList:
        print('empty linked list!')

    CDLL.createCDLL([6,5,4,3,2,1])
    CDLL.traverseCDLL()

    insval = 8
    loc = 0
    print(f"\nAfter inserting {insval} at {loc}:")
    CDLL.insertCDLL(value=insval,location=loc)
    CDLL.traverseCDLL()
    print('\n\n')

    insval = 10
    loc = -1
    print(f"\nAfter inserting {insval} at {loc}:")
    CDLL.insertCDLL(value=insval,location=loc)
    CDLL.traverseCDLL()
    print('\n\n')

    loc = -1
    print(f"\nAfter deleting index {loc}:")
    CDLL.deleteCDLL(location=loc)
    CDLL.traverseCDLL()
    print('\n\n')

    loc = 0
    print(f"\nAfter deleting index {loc}:")
    CDLL.deleteCDLL(location=loc)
    CDLL.traverseCDLL()
    print('\n\n')

    loc = 2
    print(f"\nAfter deleting index {loc}:")
    CDLL.deleteCDLL(location=loc)
    CDLL.traverseCDLL()
    print('\n\n')

    insval = 4
    loc = 2
    print(f"\nAfter inserting {insval} at {loc}:")
    CDLL.insertCDLL(value=insval,location=loc)
    CDLL.traverseCDLL()
    print('\n\n')


    seval = 1
    print(f"\nsearch for value {seval}:")
    print(CDLL.searchCDLL(value=seval))
    print('\n\n')
    

    seval = 3
    print(f"\nsearch for value {seval}:")
    print(CDLL.searchCDLL(value=seval))
    print('\n\n')

    seval = 15
    print(f"\nsearch for value {seval}:")
    print(CDLL.searchCDLL(value=seval))
    print('\n\n')

    print(CDLL)

# %%
