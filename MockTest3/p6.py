class C:
    def __init__(self,fn,ln,age):
        self.fn = fn
        self.ln = ln
        self.age = age
        self.text = ''

    def __str__(self):
        if self.age >= 18:
            self.text += str(self.fn[0]).capitalize()
            self.text += str(self.ln[0]).capitalize()
            self.text += str(self.age)

        else:
            self.text += str(self.fn[0]).lower()
            self.text += str(self.ln[0]).lower()
            self.text += str(self.age)

        return self.text

print(C("John","May",21))
print(C("Anna","Brown",17))