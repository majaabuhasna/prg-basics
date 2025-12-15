import queue

stack = queue.LifoQueue()

string = str(input('String: '))

for char in string:
    stack.put(char)

reversed_string = ''

while not stack.empty():
    reversed_string += str(stack.get(char))

print(f'Reversed string: {reversed_string}')