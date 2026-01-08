from abc import ABC, abstractmethod

class LibraryItem(ABC):

    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_book(self):
        pass



class Book(LibraryItem):
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__is_available = True

    @property
    def is_available(self):
        return self.__is_available

    @is_available.setter
    def is_available(self,is_available):
        self.__is_available = is_available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        
        else:
            print("Book is unavailable!")
            return False
        
    def return_book(self):
        if not self.is_available:
            self.is_available = True
        
        else:
            print('Book isn\'t lent to anybody')


class Ebook(LibraryItem):
    def __init__(self,title,author,isbn, file_size):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.file_size = file_size

    def borrow(self):
        print(f"You can download the ebook '{self.title}' (Size - {self.file_size} MB)")
        return True
    
    def return_book(self):
        print(f"Digital copies needn't be returned!")
        return True

        
class Reference_Book(LibraryItem):
    
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__is_available = False
    
    def borrow(self):
        print("Reference Books cannot be borrowed")
        return False
    
    def return_book(self):
        print("Reference books are not borrowed or returned!!")
        
class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self,book):
        if len(self.borrowed_books) >=3:
            print('A maximum of 3 books can be borrowed!')
            return False
        else:
            if book.borrow():
                self.borrowed_books.append(book)
                return True

    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        
        else:
            print("Book isn't borrowed!")

def borrow_any(book,member):

    if len(member.borrowed_books) >=3:
        print(f"A maximum of 3 books can be borrowed!" )
    elif book.borrow():
        member.borrowed_books.append(book)
        print(f"{member.name} borrowed {book.title}")

    else:
        print("Book couldn't be borrowed!")
    
