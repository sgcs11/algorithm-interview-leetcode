from collections import deque


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.dq = [None] * k
        self.front = 0
        self.last = k - 1
        self.cnt = 0
        self.maxlen = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.front = (self.front - 1) % self.maxlen
        self.dq[self.front] = value
        self.cnt += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.last = (self.last + 1) % self.maxlen
        self.dq[self.last] = value
        self.cnt += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.dq[self.front] = None
        self.front = (self.front + 1) % self.maxlen
        self.cnt -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.dq[self.last] = None
        self.last = (self.last - 1) % self.maxlen
        self.cnt -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.dq[self.front] if not self.isEmpty() else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.dq[self.last] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.cnt == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cnt == self.maxlen
