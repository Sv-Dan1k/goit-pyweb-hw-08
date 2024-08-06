from models import Author, Quote
import sys

def search_by_author(name):
    author = Author.objects(fullname=name).first()
    if not author:
        print(f"No author found with name {name}")
        return
    quotes = Quote.objects(author=author)
    for quote in quotes:
        print(f"{quote.author.fullname}: {quote.quote}")

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        try:
            print(f"{quote.author.fullname}: {quote.quote}")
        except Author.DoesNotExist:
            print("Author not found for this quote.")

def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    for quote in quotes:
        try:
            print(f"{quote.author.fullname}: {quote.quote}")
        except Author.DoesNotExist:
            print("Author not found for this quote.")

def main():
    while True:
        command = input("Enter command: ")
        if command.startswith('name:'):
            name = command.split(':', 1)[1].strip()
            search_by_author(name)
        elif command.startswith('tag:'):
            tag = command.split(':', 1)[1].strip()
            search_by_tag(tag)
        elif command.startswith('tags:'):
            tags = command.split(':', 1)[1].strip()
            search_by_tags(tags)
        elif command == 'exit':
            sys.exit()
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
