class Queue():
    def __intit__(self):
        self.queue = []

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return 0
        else:
            return self.queue.pop(0)
        
    def printQueue(self):
        print(self.queue)
        