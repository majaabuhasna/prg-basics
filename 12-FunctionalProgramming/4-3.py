grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

passing_grades = list(filter(lambda x:x>2,grades))
arithmetic_mean = print(f'Arithmetic mean for grades <> 2.0 is {sum(passing_grades)/len(passing_grades):.2f}')