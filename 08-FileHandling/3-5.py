###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Enter username: ')
password = input('Enter password: ')

# pattern (criteria) for username and password
username_pattern = '[a-z]{6,}'
password_pattern = '^\w{8,}$'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if username_match and password_match:
   print('Both username and password meet the requirements!')
else:
   print('Either username, password or both do not meet the requirements.')