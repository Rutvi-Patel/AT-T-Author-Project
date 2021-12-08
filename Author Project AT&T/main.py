
from Author import Author
from Book import Book

def createAuthors():
    """this function Creates and initilizes
    Author objects for the given authors"""

    #List of autors and their generes
    authors_dict = {"Steven King":"Horror",
               "Rudyard Kipling" : "Adventure",
               "Isaac Asimov": "Science Fiction",
               "Suzanne Collins": "YA Fiction"}
    authors_list = []
    for key in authors_dict:
        a1 = Author()#creates object instance
        a1.setName(key) #set name value
        a1.setGenre(authors_dict[key]) #set genere value
        authors_list.append(a1)
    return authors_list




if __name__ == '__main__':
    authors = createAuthors()#returns a list of author objects

    print("Enter q to exit input")
    print("Input:\n")
    while (True):
        data = input()#user input
        # break the loop when input is 'q'
        if (str.lower(data) == "q"):
            break
        lst = data.split(",")#split the data with every comma
        if len(lst)==4:#checks if there are four values per data
            b1 = Book(lst[0],lst[1],lst[2],lst[3]) #creates book instance
            for a in authors:
                if a.getName()==lst[2]:
                    a.setBook(b1) #adds the book objects to its author object books list
                    break
    #Gets the author with max number of books
    maxBooks = -1
    author = None
    for a in authors:
        if a.getNumberOfBooks()>maxBooks:
            maxBooks = a.getNumberOfBooks()
            author = a
    #gets the oldest book of that author
    oldbook = author.oldestBook()
    # Output string
    print("\n\nOutput:")
    print(oldbook.getTitle()+",","written by",author.getGenre(),
          "writer", author.getName(), "on", oldbook.getPubDate(),
          "is", oldbook.getPages(), "pages long.")



