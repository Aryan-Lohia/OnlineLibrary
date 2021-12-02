import urllib.request
from pathlib import Path
import webbrowser
import platform
class LibraryClass:
    def __init__(self, library_name) -> None:
        self.booklist = {}
        self.update=False
        self.username=input("Please Enter Your Name\n")
        print(f"Welcome {self.username}")
        self.path=str(Path(__file__).absolute())
        if(platform.platform()[:platform.platform().index("-")]=="Windows"):
            self.path=self.path[:self.path.rindex("\\Library.py")+1]+"\\books.txt"
        elif(platform.platform()=="Linux"):
            self.path=self.path[:self.path.rindex("/Library.py")+1]+"/books.txt"
        data = urllib.request.urlopen(urllib.request.Request("https://raw.githubusercontent.com/Aryan-Lohia/OnlineLibrary/main/root/books.txt"))
        with open(self.path,"w") as books:
            books.write("")
            for line in data:
                if len(line)==0 :
                    break
                line=str(line)[2:-3]
                books.write(line+"\n")
                book=line[0 :line.rindex(" ")]
                link = line.split()[-1]
                self.booklist[book.upper()] = link
        self.library_name = library_name

    def Display_book(self) -> None:
        print(f"Books in {self.library_name[0:14]}:")
        i=1
        for books in self.booklist:
            print(f"{i}.{books}")
            i+=1

    def Get_book(self, book_serial) -> None:
        books=list(self.booklist.keys())
        try:
            book_name = books[book_serial-1]
        except:
            print(f"Invalid serial no. Please choose a book from the list.\n")
            return
        print("Enjoy your book!!")
        webbrowser.open(self.booklist[book_name])
        
    def Add_book(self, book_name,link) -> None:
        if book_name not in self.booklist:
            self.update=True
            self.booklist[book_name]=link
            with open(self.path,'a') as books:
                books.write(f"{book_name} {link}\n")
            print("Thank You for contributing to this library\nYour book will be checked and added soon.")
        else:
            print("This book already exists in library\n")

    def Search_book(self, book_name) -> None:
        if book_name in self.booklist:
            print(f"{book_name} is present in library at serial number {list(self.booklist.keys()).index(book_name)+1}\n")
        elif True in map(lambda x:book_name in x,list(self.booklist.keys())):
            print("Closest Results:")
            for book in self.booklist:
                if book_name in book:
                    print(f"{book} : present in library at serial number : {list(self.booklist.keys()).index(book)+1}")
        else:
            print("Sorry the book you need is not present in the library\n")

    def User_choice(self, choice) -> None:
        if choice == '1':
            self.Display_book()
        elif choice == '2':
            book = (input("Enter Name of book you want to search:\n")).upper()
            self.Search_book(book)
        elif choice == '3':
            book = int(input("Enter serial number of the book you want from the list:\n"))
            self.Get_book(book)
        elif choice == '4':
            book = (input("Enter Name of book you want to add:\n")).upper()
            link = input("Enter link to the book you want to add:\n")
            self.Add_book(book, link)
        else:
            print("Invalid Entry. Please try again")
