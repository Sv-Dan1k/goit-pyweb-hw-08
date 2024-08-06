from mongoengine import Document, StringField, ListField, ReferenceField, connect


connect('project8', host='mongodb+srv://smxkey:wdz953e6@project8.sleu1he.mongodb.net/?retryWrites=true&w=majority&appName=project8')
        

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule='CASCADE')
    quote = StringField(required=True)