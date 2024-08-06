import json
from models import Author, Quote, connect


connect('project8', host='mongodb+srv://smxkey:wdz953e6@project8.sleu1he.mongodb.net/?retryWrites=true&w=majority&appName=project8')


Author.drop_collection()
Quote.drop_collection()


with open('authors.json', 'r', encoding='utf-8') as f:
    authors_data = json.load(f)
    for author_data in authors_data:
        author = Author(
            fullname=author_data['fullname'],
            born_date=author_data['born_date'],
            born_location=author_data['born_location'],
            description=author_data['description']
        )
        author.save()


with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes_data = json.load(f)
    for quote_data in quotes_data:
        author = Author.objects(fullname=quote_data['author']).first()
        if author:
            quote = Quote(
                tags=quote_data['tags'],
                author=author,
                quote=quote_data['quote']
            )
            quote.save()
