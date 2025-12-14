# takes two numbers from keyboard
n1 = input('Number 1: ')
n2 = input('Number 2: ')

# define an anonymous function
mean = lambda x,y: (int(x)+int(y))/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result: .2f}')