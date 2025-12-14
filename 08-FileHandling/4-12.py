import csv

def save_book_to_file(genre,book_info):
    file_name = f'books_{str(genre).lower().replace(' ','_')}.txt'

    with open(file_name,'a',encoding='utf-8') as file:
        file.write(book_info + '\n')

with open('books.csv','r',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        genre = row['Genre']

        line_to_save = f'{row['Title']},{row['Author']},{row['Year']}'

        save_book_to_file(genre,line_to_save)