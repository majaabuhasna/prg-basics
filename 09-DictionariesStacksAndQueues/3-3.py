import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue()
    lookup = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    for char in expression:
        if char in '([{':
            stack.put(char)
        
        elif char in ')]}':
            if stack.empty():
                return False
            
            top_element = stack.get()

            if lookup[char] != top_element:
                return False
    
    return stack.empty() #True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
    print(True)
else:
    print(False)

if brackets_ok(expression2):
    print(True)
else:
    print(False)

if brackets_ok(expression3):
    print(True)
else:
    print(False)
