class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._head = None
        self._tail = None
        self._size = 0
        self._capacity = k
        
        
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self._head = self._tail = ListNode(value)
        else:
            node = ListNode(value)
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self._head = self._tail = ListNode(value)
        else:
            node = ListNode(value)
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._size += 1
        return True
    
    
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self._size == 1:
            self._head = self._tail = None
        else:
            temp = self._head.next
            self._head.next = None
            temp.prev = None
            self._head = temp
        self._size -= 1
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self._size == 1:
            self._head = self._tail = None
        else:
            temp = self._tail.prev
            self._tail.prev = None
            temp.next = None
            self._tail = temp
        self._size -= 1
        return True
        
        
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self._head.val   
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self._tail.val 
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._size == self._capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()