from pathlib import Path
class LibraryClass:
    def __init__(self, library_name) -> None:
        self.booklist = {}
        self.update=False
        self.username=input("Please Enter Your Name\n")
        print(f"Welcome {self.username}")
        path=str(Path(__file__).absolute())
        self.path=path[:path.rindex("\\")+1]+"\\books.txt"
        with open(self.path) as books:
            while True:
                booklink=books.readline().strip(("\n"))
                if len(booklink)==0 :
                    break
                book=booklink[0 : booklink.rindex(" ")]
                link = booklink.split()[-1]
                self.booklist[book.upper()] = link
        self.library_name = library_name

    def Display_book(self) -> None:
        print(f"Books in {self.library_name}:")
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
        print(f"You may find {book_name} at this link: {self.booklist[book_name]}")

    def Add_book(self, book_name,link) -> None:
        if book_name not in self.booklist:
            self.update=True
            self.booklist[book_name]=link
            with open(self.path,'a') as books:
                books.write(f"{book_name} {link}\n")
            print("Your Book has been added. \nThank You for contributing to this library\n")
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
