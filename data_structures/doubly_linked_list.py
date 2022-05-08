class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def traversalDLL(self):
        if not self.head:
            print("Empty linked list")
        else:
            node = self.head
            while node:
                print(f'{node.value}-',end='')
                node= node.next
            print(f'\nhead: {self.head.value} tail: {self.tail.value} len: {self.len}')

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
                node = node.next
                i+=1

            print(f'{nodeValue} not found in the linked List')
            return False

    def insertDLL(self, value, location=-1): ## default location in the end
        if location<-1 or location>self.len:
            raise ValueError(f'location should be -1 or between 0 to len (inclusive)')
        
        newNode = Node(value)
        
        if self.head is None: ## insert first element O(1) S&T
            self.head = newNode
            self.tail = newNode
            self.len += 1

        else:
            if location==0: ## insert in the start O(1) S&T
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
                self.len += 1
            elif location==-1 or location==self.len: ## insert after tail O(1) S&T
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                self.len += 1

            elif location<self.len: ## anywhere in between O(n) time and O(1) space
                tempNode = self.head
                for index in range(1,location):
                    tempNode = tempNode.next

                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.prev = tempNode
                newNode.next = nextNode
                nextNode.prev = newNode

                self.len += 1


    def deleteDLL(self, location=-1): ## default location in the end
        if location<-1 or location>self.len-1:
            raise ValueError(f'location should be -1 or between 0 to len-1 (inclusive)')
        
        if self.head is None: ## insert first element O(1) S&T
            print('Empty linked list')
            return None

        else:
            if location==0: ## delete in the start O(1) S&T
                firstNode = self.head
                self.head = firstNode.next
                del_val = firstNode.value
                firstNode.next,firstNode.prev = None, None
                self.head.prev = None
                self.len -= 1
            elif location==-1 or location==self.len-1: ## delete tail O(1) S&T
                lastNode = self.tail
                self.tail = lastNode.prev
                self.tail.next = None
                del_val = lastNode.value
                lastNode.prev, lastNode.next = None, None
                self.len -= 1

            elif location<self.len: ## anywhere in between O(n) time and space
                tempNode = self.head
                for index in range(1,location):
                    tempNode = tempNode.next

                nextNode = tempNode.next
                tempNode.next = nextNode.next
                tempNode.next.prev = tempNode

                del_val = nextNode.value
                nextNode.next, nextNode.prev = None, None

                self.len -= 1
            
            return del_val


    def delcompleteDLL(self): ## O(n) time and O(1) space complexities
        node = self.head
        while node:
            temp = node.next
            node.next = None
            node.prev = None
            self.head = temp
            node = temp
            self.len -= 1
        self.tail = None



if __name__ == '__main__':
    doublyLinkedList = DLinkedList()
    doublyLinkedList.insertDLL(1)
    doublyLinkedList.insertDLL(2,-1) ## tail insert
    doublyLinkedList.traversalDLL()
    print(doublyLinkedList.tail.value)
    doublyLinkedList.insertDLL(3,1)
    doublyLinkedList.insertDLL(4,1)

    doublyLinkedList.insertDLL(6,doublyLinkedList.len-1) ## before tail insert O(n)
    print(doublyLinkedList.tail.value)
    doublyLinkedList.insertDLL(9,doublyLinkedList.len) ## tail insert


    doublyLinkedList.insertDLL(60,3) ## middle insert O(n)

    doublyLinkedList.insertDLL(80,0) ## head insert O(1)

    doublyLinkedList.insertDLL(10,doublyLinkedList.len - 1) ## head insert O(n)

    print('len: ',doublyLinkedList.len, f' head: {doublyLinkedList.head.value} tail: {doublyLinkedList.tail.value}')

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
    doublyLinkedList.deleteDLL(2)
    doublyLinkedList.traversalDLL()

    print('len: ',doublyLinkedList.len)


    print('Deleting complete linked list/removing all elements')
    doublyLinkedList.delcompleteDLL()
    doublyLinkedList.traversalDLL()
    
    print('len: ',doublyLinkedList.len)



        


