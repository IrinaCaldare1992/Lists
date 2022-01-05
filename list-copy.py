queue = [
    "Jane",
    "Mark",
    "Dan"
]

couple = [
    "Ann",
    "Max",
    "Pete"
]

for i in range(len(couple)):
    queue.append(couple[i])
    
for i in range(len(queue)):
    print(i, queue[i])