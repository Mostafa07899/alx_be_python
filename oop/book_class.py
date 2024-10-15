class Book:
    def __init__(self, title:str, author:str, year:int):
        self.title = title
        self.author = author
        self.year = year


    def __del__(self):
        print(f"deleting {self.title}")

    def __str__(self):
        print(f"{self.title} by {self.author}, published in {self.year}")

    def __repr__(self):
        print(f"Book('{self.title}', '{self.author}', {self.year})")



from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)

    print(repr(my_book))  

    del my_book

if __name__ == "__main__":
    main()