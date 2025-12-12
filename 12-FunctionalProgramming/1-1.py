###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   m = (int(x)+int(y))/2
   return m

# takes two numbers from keyboard
n1 = input('Number 1: ')
n2 = input('Number 2: ')

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result: .2f}')