class Book:
    def __init__(self, title, pages, author, published_year):
        self.title = title
        self.__pages = pages
        self.author = author
        self.__year = published_year

    def pages(self, page):
        if page > 300:
            raise ValueError("Nomiin huudas baga baina")
        self.__pages = page

    def long_book(self, year)
    # def publish_year(self, year):
    #     if published_year > 10:
    #         raise ValueError("Nomiin jil baga baina")
    #     self.published_year = 
        
        