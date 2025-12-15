import queue

stack = queue.LifoQueue()

natural_number = int(input('Natural number: '))

remainder = natural_number % 2
stack.put(remainder)
result = natural_number // 2

while result != 0:
    remainder = result % 2
    stack.put(remainder)
    result = result // 2

binary = ''
while not stack.empty():
    binary += str(stack.get())

print(f'Binary number: {binary}')