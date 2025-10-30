class Library:
    def __init__ (self, listOfBooks):
        self.books = listOfBooks
        
    def displayAvailavleBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("\t" + book)
            
    def borrowBook(self, bookName):
        if bookName in self.books:
           print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
           self.books.remove(bookName)   
        else:
           print("Sorry, This book has already been issued to someone else. Please wait until the book is returned")        
            
class Student:
    pass

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    centralLibrary.displayAvailavleBooks()