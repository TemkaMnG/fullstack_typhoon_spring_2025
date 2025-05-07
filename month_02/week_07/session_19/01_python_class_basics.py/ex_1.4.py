
import datetime
class Book():
    def __init__(self, title, pages, author, published_year):
        self.title = title
        self.pages = pages
        self.author = author
        self.published_year = published_year

    def nas(self):
        real_year = datetime.datetime.now().year
        return real_year - self.published_year

    def urt_eseh(self):
        return self.pages > 300
            # def pages(self, page):
    #     if page > 300:
    #         raise ValueError("Nomiin huudas baga baina")
    #     self.__pages = page

    # def long_book(self, year)
    # def publish_year(self, year):
    #     if published_year > 10:
    #         raise ValueError("Nomiin jil baga baina")
    #     self.published_year =

book1 = Book("The Hobbit", "J.R.R. Tolkien", 295, 1937)
book2 = Book("War and Peace", "Leo Tolstoy", 1225, 1869)
book3 = Book("Python Crash Course", "Eric Matthes", 544, 2019)
books = [book1, book2, book3]
for book in books:
    print(book)
    print(f"Age: {book.get_age()} years")
    print(f"Long book: {'Yes' if book.is_long() else 'No'}")
    print("-" * 30)
