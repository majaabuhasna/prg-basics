class C:
    def __init__(self,value):
        self.value = value

    def m1(self):
        return self.value
    
    def m2(self):
        self.value += 1

    def m3(self):
        self.value -= 1

    def m4(self,n):
        self.value += n

    def __str__(self):
        return str(self.value)
    
def main():
    c=C(5)
    r1 = c.m1()
    c.m2()
    r2 = c.m1()
    c.m4(-8)
    r3 = c.m1()
    c.m3()
    r4 = c.m1()
    c.m4(10)
    r5 = c.m1()
    r6 = c.__str__()

    return r1,r2,r3,r4,r5,r6

print(main())