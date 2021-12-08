import datetime as dt

class Author:

    def __init__(self):
        self.books = []

    """Author class getters and setters"""
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setBook(self,book):
        self.books.append(book)

    def getGenre(self):
        return self.genre

    def setGenre(self, genre):
        self.genre = genre

    # Returns the total numbers of books of author
    def getNumberOfBooks(self):
        return len(self.books)

    def oldestBook(self):
        """ retrieves the oldest book if this author"""
        str= "01/01/2050"
        str = str.split("/")
        olderDate = dt.datetime(int(str[2]), int(str[0]), int(str[1]))
        mbook = None
        for b in self.books: #looping all the books of author
            var = b.getPubDate().split("/")
            dateb = dt.datetime(int(var[2]), int(var[0]), int(var[1]))
            if (dateb<olderDate): #Comparing publication dates
                olderDate = dateb
                mbook = b
        return mbook
