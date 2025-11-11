print('SURVEY')
first_q = input('Are you interested in computer science? (y/n): ') == 'y'
second_q = input('Do you like playing computer games? (y/n): ') == 'y'
third_q = input('Do you have an Instagram account? (y/n): ') == 'y'
print()

answer1 = ''
answer2 = '' 
answer3 = ''

if first_q:
    answer1 = 'yes'
else:
    answer1 = 'no'

if second_q:
    answer2 = 'yes'
else:
    answer2 = 'no'

if third_q:
    answer3 = 'yes'
else:
    answer3 = 'no'

print('SURVEY RESULTS')
print(f'Interested in computer science: {answer1}')
print(f'Playing computer games: {answer2}')
print(f'Has an Instagram account: {answer3}')