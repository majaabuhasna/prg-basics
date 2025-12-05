###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r', encoding='utf-8') as email_content:
    email = email_content.read()

# regular expression pattern
# for amounts
pattern = r'€\d+'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0
for amount in amounts:
    amount = int(amount[1:])
    total += amount
    
# print result
print(f'Total: €{total}')