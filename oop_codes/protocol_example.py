
from typing import Protocol


class READABLE(Protocol):
    def read(self) : ...


class BOOK:
    
    def __init__(self,title,author, publish_date,pages):
        self.author = author
        self.title = title
        self.publish_date = publish_date
        self.pages = pages

    def read(self):
        return f'THE book is {self.title} written by {self.author} with {self.pages} pages and published on {self.publish_date}'
    
class Newspaper:
    def __init__(self,title, date):
        self.title = title
        self.date = date

    def read (self):
        return f'THE NEWSPAPER IS {self.title} and date is {self.date}'
    
def read(item: READABLE):
    print(item.read())

book = BOOK('THE UPRISING','PRABIN NEUPANE', '2001-05-20',500)
paper = Newspaper('the himalayan times', '2025-02-25')

read(book)
read(paper)