class C:
    def __init__(self,name,surname,age,seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        if self.age >= 18:
            return f'{self.surname.capitalize()}{self.name[0].capitalize()}{self.seniority}'
        else:
            return f'{self.surname.lower()}{self.name[0].lower()}{self.seniority}'
        
def main():
    p1 = C("Anna","May",17,7)
    p2 = C("George","Brown",21,4)

    print(p1)
    print(p2)

if __name__ == '__main__':
    main()