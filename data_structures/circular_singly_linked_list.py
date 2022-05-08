# %%
class InvalidLocationError(Exception):
    pass
class EmptyLinkedList(Exception):
    pass


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLinkedList:
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

    def traverseCSLL(self):
        if not self.len:
            raise EmptyLinkedList
        else:
            node = self.head
            print('Head',sep='',end='')
            while node:
                print('->',node.value,sep='',end='')
                node = node.next
                if node == self.head:
                    break
            print('<-Tail->Head')
            print(f'head: {self.head.value} tail: {self.tail.value} tail.next: {self.tail.next.value} len: {self.len}')

    def searchCSLL(self,value):
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

    
    def insertCSLL(self,value,location=-1): ## default location in the end
        if location<-1 or location>self.len:
            raise InvalidLocationError(f'location should be -1 or between 0 to len (inclusive)')
        
        newNode = Node(value)

        if self.head is None: ## empty linked list O(1) S&T
            self.head = newNode
            self.tail = self.head
            newNode.next = self.head
            self.len += 1
        else:

            if location==0: ## at head -> new head O(1) S&T
                newNode.next = self.head
                self.head = newNode
                self.tail.next = self.head

                self.len += 1

            elif location==-1 or location==self.len: ## insert after tail -> new tail O(1) S&T
                self.tail.next = newNode
                newNode.next = self.head
                self.tail = newNode
                self.len += 1
            
            elif location<self.len: ## O(n) Time and O(1) Space
                tempNode = self.head
                for i in range(1,location):
                    tempNode = tempNode.next
                
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

                self.len += 1

    def deleteCSLL(self,location=-1):
        if location<-1 or location>self.len-1:
            raise InvalidLocationError('Location should be -1 or between 0 and len-1 (both inclusive)')

        if self.head is None:
            raise EmptyLinkedList
        
        else:
            if location == 0: ## O(1) S&T
                if self.len<=1:
                    self.head, self.tail = None, None
                else:
                    firstNode = self.head
                    self.head = firstNode.next
                    firstNode.next = None
                    self.tail.next = self.head

                self.len -= 1
            
            elif location==-1 or location<self.len: ## O(n) S&T
                if location==-1:
                    location = self.len - 1

                tempNode = self.head
                for i in range(1,location):
                    tempNode = tempNode.next

                nextNode = tempNode.next
                tempNode.next = nextNode.next

                if nextNode==self.tail:
                    self.tail = tempNode
                    nextNode.next = None

                self.len -= 1

    def deletecompleteCSLL(self):
        if self.head is None:
            raise EmptyLinkedList
        else:
            node = self.head
            while node:
                tempNode = node.next
                node.next = None
                self.head = tempNode
                node = tempNode
                self.len -= 1
                if node == self.tail:
                    self.len -= 1
                    break
            self.head, self.tail = None, None
    
    def createCSLL(self,valuelist):
        try:
            self.deletecompleteCSLL()
        except EmptyLinkedList:
            pass

        self.head = Node(valuelist[0])
        self.len += 1
        node = self.head
        for item in valuelist[1:]:
            node.next = Node(item)
            node = node.next
            self.len += 1
        self.tail = node
        node.next = self.head


# %%
if __name__ == '__main__':
    CSLL = CSLinkedList()
    try:
        print(CSLL)
    except EmptyLinkedList:
        print('empty linked list!')

    CSLL.insertCSLL(value=1,location=-1)
    CSLL.insertCSLL(value=2,location=-1)
    CSLL.insertCSLL(value=3,location=-1)
    CSLL.insertCSLL(value=4,location=-1)
    CSLL.insertCSLL(value=5,location=-1)
    CSLL.insertCSLL(value=6,location=-1)
    print(CSLL)
    CSLL.traverseCSLL()
    
    CSLL.deletecompleteCSLL()

    try:
        print(CSLL)
    except EmptyLinkedList:
        print('empty linked list!')

    CSLL.createCSLL([6,5,4,3,2,1])
    CSLL.traverseCSLL()

    insval = 8
    loc = 0
    print(f"\nAfter inserting {insval} at {loc}:")
    CSLL.insertCSLL(value=insval,location=loc)
    CSLL.traverseCSLL()
    print('\n\n')

    insval = 10
    loc = -1
    print(f"\nAfter inserting {insval} at {loc}:")
    CSLL.insertCSLL(value=insval,location=loc)
    CSLL.traverseCSLL()
    print('\n\n')

    loc = -1
    print(f"\nAfter deleting index {loc}:")
    CSLL.deleteCSLL(location=loc)
    CSLL.traverseCSLL()
    print('\n\n')

    loc = 0
    print(f"\nAfter deleting index {loc}:")
    CSLL.deleteCSLL(location=loc)
    CSLL.traverseCSLL()
    print('\n\n')

    loc = 2
    print(f"\nAfter deleting index {loc}:")
    CSLL.deleteCSLL(location=loc)
    CSLL.traverseCSLL()
    print('\n\n')

    insval = 4
    loc = 2
    print(f"\nAfter inserting {insval} at {loc}:")
    CSLL.insertCSLL(value=insval,location=loc)
    CSLL.traverseCSLL()
    print('\n\n')


    seval = 1
    print(f"\nsearch for value {seval}:")
    print(CSLL.searchCSLL(value=seval))
    print('\n\n')
    

    seval = 3
    print(f"\nsearch for value {seval}:")
    print(CSLL.searchCSLL(value=seval))
    print('\n\n')

    seval = 15
    print(f"\nsearch for value {seval}:")
    print(CSLL.searchCSLL(value=seval))
    print('\n\n')

    print(CSLL)

# %%
