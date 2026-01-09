def f(uid):
    for i in range(len(uid)):
        for j in range(i+1,len(uid)):
            if uid[i] == uid[j]:
                return False
            
    return True

print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))