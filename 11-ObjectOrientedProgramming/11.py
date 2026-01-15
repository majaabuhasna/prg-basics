class C:
    def __init__(self,dictionary):
        self.dictionary = dictionary

    def m1(self,s,n):
        self.dictionary[s] = n

    def m2(self,s):
        sum_of_fans = 0
        for sector in s:
            for key,value in self.dictionary.items():
                if key == sector:
                    sum_of_fans += value

        return sum_of_fans
    
def main():
    stadium = C({"A":120,"D":150,"G":90,"K":110})
    stadium.m1("G",130)
    print(stadium.m2("GD"))
    print(stadium.m2("KEJ"))

if __name__ == '__main__':
    main()