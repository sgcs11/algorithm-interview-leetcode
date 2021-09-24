# self.cnt를 사용해서 enQUue 시 +1 deQueue시 -1하면서 카운트하면 더 쉽게 풀이되나 책의 풀이를 따라 작성함
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * (k)
        self.front = 0
        self.rear = 0
        self.maxlen = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.maxlen
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.front] = None
        self.front = (self.front + 1) % self.maxlen
        return True

    def Front(self) -> int:
        return self.q[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.q[self.rear - 1] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.rear] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.rear] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()