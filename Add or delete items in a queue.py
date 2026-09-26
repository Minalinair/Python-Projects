class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.isEmpty():
            self.queue.pop(0)
        else:
            print("Queue is empty!")
    def isEmpty(self):
        if len(self.queue)==0:
            return True
p1 = Queue()
p1.enqueue(3)
p1.enqueue(4)
p1.enqueue(5)
p1.enqueue(6)
p1.enqueue(7)
p1.enqueue(8)
print(p1.queue)
p1.dequeue()
print(p1.queue)
p1.dequeue()
print(p1.queue)
p1.dequeue()
print(p1.queue)
p1.dequeue()
print(p1.queue)
p1.dequeue()
print(p1.queue)
p1.dequeue()
p1.dequeue()
p1.enqueue(9)
print(p1.queue)
p1.dequeue()
print(p1.queue)