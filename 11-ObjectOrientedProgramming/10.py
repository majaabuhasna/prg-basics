class C:
    def __init__(self,arr):
        self.arr = arr

    def m(self,n):
        counter = 0
        for pair in self.arr:
            if pair[0] > 0 and pair[1] > 0:
                counter += 1
        
        if counter >= n:
            return True
        return False
    
def main():
    p1 = C([[2,3],[1,8],[-6,4],[3,-7]])
    print(p1.m(2))
    print(p1.m(3))

if __name__ == '__main__':
    main()