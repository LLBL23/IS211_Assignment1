
class Book:
    def __init__(self, author, title):
        """
        Constructor of Book class
        author = Author of the book
        title = Title of the book
        """
        self.author = author
        self.title = title
    
    def display(self):
        """
        Display the book's title and author
        """
        print(f'"{self.title}, written by {self.author}".')


if __name__ == "__main__":
    bk1 = Book('J.K. Rowling', 'Harry Potter and the Goblet of Fire')
    bk2 = Book('Walter Scott', 'Ivanhoe: Romance')

    bk1.display()
    bk2.display()
