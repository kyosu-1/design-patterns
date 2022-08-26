class Book(object):
    def __init__(self, name: str) -> None:
        self.__name = name
    
    def get_name(self) -> str:
        return self.__name


# iterator pattern
class BookShelf(object):
    def __init__(self) -> None:
        self.__books = []
    
    def append(self, book: Book) -> None:
        self.__books.append(book)
    
    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index >= len(self.__books):
            raise StopIteration()
        
        book = self.__books[self.__index]
        self.__index += 1
        return book
