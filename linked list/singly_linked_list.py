class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def traversalSLL(self): ## O(n) time and O(1) space
        if self.head is None:
            print("Single Linked List doesn't have any elements")
        else:
            node = self.head
            print('Head',sep='',end='')
            while node is not None:
                print('->',node.value,sep='',end='')
                node = node.next
            print('<-Tail')
            print(f'head: {self.head.value} tail: {self.tail.value} len: {self.len}')

    def searchSLL(self,nodeValue): ## O(n) and O(1) time and space compl. resp
        if self.head is None:
            print(f'{nodeValue} not found in the linked List')
            return False
        else:
            node = self.head
            i = 0
            while node:
                if node.value==nodeValue:
                    return True, i
                node = node.next
                i+=1

            print(f'{nodeValue} not found in the linked List')
            return False

    def insertSLL(self, value, location=-1): ## default insert at last -> after orignal tail, space complexity O(1)
        if location<-1 or location>self.len:
            raise ValueError('Location should be -1 or between 0 and len (both inclusive)')
        newNode = Node(value)
        if self.head is None: ## first element insert O(1)
            self.head = newNode
            self.tail = newNode
            self.len += 1
        else:
            if location==0: ## head insert O(1)
                newNode.next = self.head
                self.head = newNode
                self.len += 1
            elif location==-1 or location==self.len: ## After tail insert -> new tail O(1)
                newNode.next = None
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

                self.len += 1


    def deleteSLL(self, location=-1): ## default delete last element, space complexity O(1)
        if location<-1 or location>self.len-1:
            raise ValueError('Location should be -1 or between 0 and len-1 (both inclusive)')
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
                    del_val = firstNode.value
                    firstNode.next = None
                self.len-=1
            elif location<self.len or location==-1: ## between head and tail (inclusive) delete O(n)
                if location==-1:
                    location = self.len-1
                tempNode = self.head ## index=0
                for index in range(1,location):
                    tempNode = tempNode.next
                    
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                del_val = nextNode.value

                if nextNode == self.tail:
                    self.tail = tempNode
                    tempNode.next = None
                    nextNode.next = None
                    
                self.len -= 1

            return del_val

    def delcompleteSLL(self): ## O(n) time and O(1) space complexities
        ## In Java, Python and JavaScript automatic garbage collection happens, 
        # so deleting a linked list is easy. Just need to change head & tail to null, but this is not applicable for doubly linked lists
        ## However, complete general implementation is shown below with explicitly deleting each node
        node = self.head
        while node:
            temp = node.next
            node.next = None
            self.head = temp
            node = temp
            self.len -= 1
        self.tail = None

if __name__ == '__main__':
    singlyLinkedList = SLinkedList()
    singlyLinkedList.insertSLL(1)
    singlyLinkedList.insertSLL(2,-1) ## tail insert
    print(singlyLinkedList.tail.value)
    singlyLinkedList.insertSLL(3,1)
    singlyLinkedList.insertSLL(4,1)

    singlyLinkedList.insertSLL(6,singlyLinkedList.len-1) ## before tail insert O(n)
    print(singlyLinkedList.tail.value)
    singlyLinkedList.insertSLL(9,singlyLinkedList.len) ## tail insert


    singlyLinkedList.insertSLL(60,3) ## middle insert O(n)

    singlyLinkedList.insertSLL(80,0) ## head insert O(1)

    singlyLinkedList.insertSLL(10,singlyLinkedList.len - 1) ## head insert O(n)

    print('len: ',singlyLinkedList.len, f' head: {singlyLinkedList.head.value} tail: {singlyLinkedList.tail.value}')

    ## traversal
    singlyLinkedList.traversalSLL()

    print([node.value for node in singlyLinkedList])

    print([(i,node.value) for i,node in enumerate(singlyLinkedList)]) ## enumerate using the iterator

    print(singlyLinkedList.tail.value)

    print('################# Searching')
    print(singlyLinkedList.searchSLL(3))
    print(singlyLinkedList.searchSLL(101))

    print('#################### deletion')
    print([(i,node.value) for i,node in enumerate(singlyLinkedList)]) ## enumerate using the iterator
    print('len: ',singlyLinkedList.len)
    singlyLinkedList.deleteSLL(-1)
    singlyLinkedList.traversalSLL()
    singlyLinkedList.deleteSLL(0)
    singlyLinkedList.traversalSLL()
    singlyLinkedList.deleteSLL(3)
    singlyLinkedList.traversalSLL()

    print('len: ',singlyLinkedList.len)

    print(singlyLinkedList.tail.value)

    print('Deleting complete linked list/removing all elements')
    singlyLinkedList.delcompleteSLL()
    singlyLinkedList.traversalSLL()

    print('len: ',singlyLinkedList.len)

