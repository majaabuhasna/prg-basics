class Statistics:
    def __init__(self):
        self.numbers = []

    def add_nr(self):
        set_of_numbers = input('Enter a set of numbers separated by a comma: ')
        set_of_numbers = set_of_numbers.split(',')

        for number in set_of_numbers:
            self.numbers.append(int(number.strip()))

    def display_all_nr(self):
        print('Numbers in set:',end=' ')
        for number in self.numbers:
            print(number, end=' ')
        print()

    def maximum_nr(self):
        return max(self.numbers)
    
    def minimum_nr(self):
        return min(self.numbers)
    
    def arithmetic_mean(self):
        sum_of_nr = sum(self.numbers)
        return (sum_of_nr/int(len(self.numbers)))
    
    def median(self):
        sorted_numbers = sorted(self.numbers)
        n = len(self.numbers)
        if len(self.numbers)%2==0:
            median = ((n//2) + (n//2 - 1))/2
            return sorted_numbers[median]
        else:
            median = n//2
            return sorted_numbers[median]
        
    def print_all(self):
        print(f'Minimum: {self.minimum_nr()}')
        print(f'Maximum: {self.maximum_nr()}')
        print(f'Arithmetic mean: {self.arithmetic_mean()}')
        print(f'Median: {self.median()}')

def main():
    s1 = Statistics()
    s1.add_nr()
    s1.display_all_nr()
    s1.maximum_nr()
    s1.minimum_nr()
    s1.arithmetic_mean()
    s1.median()
    s1.print_all()

if __name__ == '__main__':
    main()