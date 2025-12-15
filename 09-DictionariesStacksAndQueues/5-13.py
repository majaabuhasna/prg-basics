import queue

stack = queue.LifoQueue()

expression = {}

while True:
    value = input('Enter any number, an operator (+ - * / ) or the equal sign (=): ')

    if value == float(value):
        