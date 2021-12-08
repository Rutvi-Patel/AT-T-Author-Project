
class Book:
    def __init__(self, title, pubDate, author, pages): #Initializing books values
        self.title = title
        self.pubDate = pubDate
        self.author = author
        self.pages = pages

    """Book class getters"""
    def getTitle(self):
        return self.title
    def getPubDate(self):
        return self.pubDate
    def getAuthor(self):
        return self.author
    def getPages(self):
        return self.pages
