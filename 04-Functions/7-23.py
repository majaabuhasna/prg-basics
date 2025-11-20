def f(password):
    password = str(password)
    if len(password) < 6:
        return False
    
    for char in password:
        if password.count(char) > 1:
            return False
    
    return True
            
print(f("ax15"), f("book123"), f("A2water3"), f("qwerty"), f(""), sep="\n")