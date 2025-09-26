# implementation_using_queue
from queue import LifoQueue

stack = LifoQueue(maxsize=4)

stack.put(2)
stack.put(3)
stack.put(4)
# stack.put(5)

print(stack) # Problem ye hai ki LifoQueue ka direct print(stack) karoge to aisa output aayega:
# Problem ye hai ki LifoQueue ka direct print(stack) karoge to aisa output aayega:
# ⚠️ Matlab object ka memory address print hoga, andar ka stack content nahi


print(stack.full())
print(stack.qsize())
print("Stack elements:", list(stack.queue))
