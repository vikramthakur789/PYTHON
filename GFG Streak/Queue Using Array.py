class myQueue:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * n
        self.front = -1
        self.rear = -1

    def enqueue(self, x):
        if self.isFull():
            return
        
        if self.front == -1:
            self.front = 0
        
        self.rear += 1
        self.arr[self.rear] = x

    def dequeue(self):
        if self.isEmpty():
            return
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return self.rear == self.size - 1
        
        
