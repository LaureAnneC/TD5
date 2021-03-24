!/usr/bin/env python3
from book import Book
def main():
    book = Book("TEST")
    book.insert_order(10, 10.0) #by default we insert a buy order
    book.insert_order(120, 12.0, False) #here we insert a sell order
    book.insert_order(5, 10.0)
    book.insert_order(2, 11.0)
    book.insert_order(1, 10.0, False)
    book.insert_order(10, 10.0, False)
if __name__ == "__main__":
    main()

