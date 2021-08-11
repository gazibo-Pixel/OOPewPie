import json

class Writeable:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def write(self, data):
        with open(self.filepath, 'w') as f:
            f.write(data)

class Readable:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def read(self):
        with open(self.filepath, 'r') as f:
            print(f.read())
class JSONS:
    def to_json(self, obj):
        print (json.dumps(obj))
class Book:
    def __init__(self, title, author, filepath):
        self.title = title 
        self.author = author
        self.filepath = filepath
        self.reader = Readable(filepath)
        self.writer = Writeable(filepath)
        self.JSONs = JSONS()
    
    def read(self):
        self.reader.read()
    
    def write2(self, data):
        self.writer.write(data)
    
    def to_json(self, obj):
        self.JSONs.to_json(obj)

book = Book(title='Not a Book', author='Ibn Batotah' , filepath='./book3.txt')
book.write2('Today TxT: Andew Cummou is out 2')