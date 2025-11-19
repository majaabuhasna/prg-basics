def f(n):
    counter = 0
    candidate = 2

    while counter < n:
        is_prime = True
        sqrt = candidate ** 0.5

        for i in range(2, int(sqrt)+1):
            if candidate % i == 0:
                is_prime = False
                break

        if is_prime:
            counter += 1
            if counter == n:
                return candidate
            
        candidate += 1

print(f(1))
print(f(5))
        
