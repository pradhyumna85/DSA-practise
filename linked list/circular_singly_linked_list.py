class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def traversalDLL(self): ## O(n) time and O(1) space
        if self.head is None:
            print("Single Linked List doesn't have any elements")
        else:
            node = self.head
            while node is not None:
                print('->',node.value,sep='',end='')
                if node.next==self.head:
                    break
                node = node.next
            print(f'\nhead: {self.head.value} tail: {self.tail.value} len: {self.len} tail.next: {self.tail.next.value}')

    def searchDLL(self,nodeValue): ## O(n) and O(1) time and space compl. resp
        if self.head is None:
            print(f'{nodeValue} not found in the linked List')
            return False
        else:
            node = self.head
            i = 0
            while node:
                if node.value==nodeValue:
                    return True, i
                if node.next == self.head:
                    break
                node = node.next
                i+=1

            print(f'{nodeValue} not found in the linked List')
            return False

    def insertDLL(self, value, location=-1): ## default insert at last -> after orignal tail, space complexity O(1)
        if location<-1 or location>self.len:
            raise ValueError('Location should be -1 or between 0 and len (both inclusive)')
        newNode = Node(value)
        if self.head is None: ## first element insert O(1)
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            self.len += 1
        else:
            if location==0: ## head insert O(1)
                newNode.next = self.head
                self.head = newNode
                self.tail.next = self.head
                self.len += 1
            elif location==-1 or location==self.len: ## After tail insert -> new tail O(1)
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
                self.len += 1
            elif location<self.len: ## between head and tail insert O(n)
                tempNode = self.head ## index=0
                for index in range(1,location):
                    tempNode = tempNode.next
                    
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                # if nextNode == self.tail:
                #     self.tail = newNode
                #     newNode.next = self.head
                self.len += 1


    def deleteDLL(self, location=-1): ## default delete last element, space complexity O(1)
        if location<-1 or location>self.len:
            raise ValueError('Location should be -1 or between 0 and len (both inclusive)')
        if self.head is None: ## nothing to delete
            print('Empty linkedlist')
        else:
            if location==0: ## head delete O(1)
                if self.len<=1:
                    self.head = None
                    self.tail = None
                else:
                    firstNode = self.head
                    self.head = firstNode.next
                    self.tail.next = self.head
                self.len-=1
            elif location<self.len or location==-1: ## between head and tail (inclusive) delete O(n)
                if location==-1:
                    location = self.len-1
                tempNode = self.head ## index=0
                for index in range(1,location):
                    tempNode = tempNode.next
                    
                nextNode = tempNode.next
                tempNode.next = nextNode.next

                if nextNode == self.tail:
                    self.tail = tempNode
                    tempNode.next = self.head
                self.len -= 1

    def delcompleteDLL(self): ## O(1) time and space complexities
        self.head = None
        self.tail = None
        self.len=0



if __name__ == '__main__':
    doublyLinkedList = DLinkedList()
    doublyLinkedList.insertDLL(1)
    doublyLinkedList.insertDLL(2,-1) ## tail insert
    print(doublyLinkedList.tail.value)
    doublyLinkedList.insertDLL(3,1)
    doublyLinkedList.insertDLL(4,1)

    doublyLinkedList.insertDLL(6,doublyLinkedList.len-1) ## before tail insert O(n)
    print(doublyLinkedList.tail.value)
    doublyLinkedList.insertDLL(9,doublyLinkedList.len) ## tail insert


    doublyLinkedList.insertDLL(60,3) ## middle insert O(n)

    doublyLinkedList.insertDLL(80,0) ## head insert O(1)

    print('len: ',doublyLinkedList.len)

    ## traversal
    doublyLinkedList.traversalDLL()

    print([node.value for node in doublyLinkedList])

    print([(i,node.value) for i,node in enumerate(doublyLinkedList)]) ## enumerate using the iterator

    print(doublyLinkedList.tail.value)

    print('################# Searching')
    print(doublyLinkedList.searchDLL(3))
    print(doublyLinkedList.searchDLL(101))

    print('#################### deletion')
    print([(i,node.value) for i,node in enumerate(doublyLinkedList)]) ## enumerate using the iterator
    print('len: ',doublyLinkedList.len)
    doublyLinkedList.deleteDLL(-1)
    doublyLinkedList.traversalDLL()
    doublyLinkedList.deleteDLL(0)
    doublyLinkedList.traversalDLL()
    doublyLinkedList.deleteDLL(3)
    doublyLinkedList.traversalDLL()

    print('len: ',doublyLinkedList.len)

    print(doublyLinkedList.tail.value)

    print('Deleting complete linked list/removing all elements')
    doublyLinkedList.delcompleteDLL()
    doublyLinkedList.traversalDLL()

    print('len: ',doublyLinkedList.len)

