class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.arr = []
        self.size = n
        
    
    def isEmpty(self):
        # Check if queue is empty
        return len(self.arr) == 0

    
    def isFull(self):
        # Check if queue is full
        return len(self.arr) == self.size

    
    def enqueue(self, x):
        # Enqueue
        if not self.isFull():
            self.arr.append(x)

    
    def dequeue(self):
        # Dequeue
        if not self.isEmpty():
            self.arr.pop(0)
          
        
    def getFront(self):
        # Get front element
        if self.isEmpty():
            return - 1
        return self.arr[0]    
       
    
    def getRear(self):
        # Get rear element 
        if self.isEmpty():
            return - 1
        return self.arr[-1]    
            
    
        
