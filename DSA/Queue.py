queue = []

# Enqueue.....
queue.append(100)
queue.append(200)
queue.append(300)

# Dequeue....
print("Dequeted:",queue.pop(0))
print("queue after dequeue:",queue)

# peek....
print("front ele",queue[0])

# emplty check...
print("Is empty?",len(queue)==0)


