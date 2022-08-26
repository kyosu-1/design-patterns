from book import Book, BookShelf


def main():
    book_self = BookShelf()
    book_self.append(Book("Around the World in 80 Days"))
    book_self.append(Book("Bible"))
    book_self.append(Book("Cinderella"))
    book_self.append(Book("Daddy-Long-Legs"))
    for book in book_self:
        print(book.get_name())


if __name__ == '__main__':
    main()
