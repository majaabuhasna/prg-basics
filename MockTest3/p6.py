class C:
    def __init__(self,fn,ln,age):
        self.fn = fn
        self.ln = ln
        self.age = age

    def __str__(self):
        if self.age >= 18:
            return f"{self.fn[0].capitalize()}{self.ln[0].capitalize()}{str(self.age)}"
        else:
            return f"{self.fn[0].lower()}{self.ln[0].lower()}{str(self.age)}"

print(C("John","May",21))
print(C("Anna","Brown",17))