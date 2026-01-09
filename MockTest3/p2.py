class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.quadrant = 0
        self.quadrant_2 = 0

    def m1(self):
        if self.x > 0 and self.y > 0:
            self.quadrant = 1
            return self.quadrant
        elif self.x < 0 and self.y > 0:
            self.quadrant = 2
            return self.quadrant
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
            return self.quadrant
        elif self.x > 0 and self.y < 0:
            self.quadrant = 4
            return self.quadrant
        else:
            self.quadrant = 0
            return self.quadrant
        
    def m2(self,a,b):
        self.a = a
        self.b = b

        if self.a > 0 and self.b > 0:
            self.quadrant_2 = 1
        elif self.a < 0 and self.b > 0:
            self.quadrant_2 = 2
        elif self.a < 0 and self.b < 0:
            self.quadrant_2 = 3
        elif self.a > 0 and self.b < 0:
            self.quadrant_2 = 4
        else:
            self.quadrant_2 = 0

        if self.quadrant_2 == self.quadrant:
            return True
        else:
            return False
        
    def m3(self,a,b):
        self.a = a
        self.b = b

        distance = (((self.y - self.b)**2 + (self.x - self.a)**2)**0.5)

        if distance > 5:
            return True
        else:
            return False

def main():
    p = C(2,3)
    r1 = p.m1()
    r2 = p.m2(7,4)
    r3 = p.m2(-3,1)
    r4 = p.m3(8,5)
    r5 = p.m3(4,7)
    p1 = C(0,5)
    r6 = p1.m1()
    r7 = p1.m2(4,7)
    r8 = p1.m2(-7,0)

    return r1,r2,r3,r4,r5,r6,r7,r8

print(main())
