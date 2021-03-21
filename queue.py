from collections import deque

class Queue:
	def __init__(self):
		self.queue=deque()

	def enqueue(self,item):
		self.queue.append(item)

	def dequeue(self):
		if len(self.queue) >0:
			self.queue.popleft()
		else:
			return None

	def __str__(self):
		return str(self.queue)

my_queue=Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print(my_queue)
my_queue.dequeue()
print(my_queue)

