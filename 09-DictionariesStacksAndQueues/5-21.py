import json

movie = {
    'title' : 'Bodies Bodies Bodies',
    'year' : 2022,
    'director' : 'Halina Reijn',
    'genre' : 'horror',
    'cast' : {
        'Emma' : 'Chase Sui Wonders',
        'Alice' : 'Rachel Sennott',
        'Sophie' : 'Amandla Stenberg',
        'Bee' : 'Marija Bakałowa',
        'David' : 'Pete Davidson'
    }
}

with open('favourite.json','w',encoding='utf-8') as file:
    json.dump(movie, file, indent=4)

print('Data has been printed to favourite.json!')