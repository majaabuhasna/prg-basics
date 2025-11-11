article_number = (input('Enter EAN-13 article number: '))

if len(article_number) == 13 and article_number.isdigit():
    print('Article number is correct')

    if article_number[0:3] == '590':
        print('Article manufactured in Poland')

else:
    print('Article number is incorrect.')