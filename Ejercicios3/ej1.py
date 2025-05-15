#Sistema para gestionar una biblioteca virtual:
#
#    Añadir libros (título, autor, páginas)
#    Buscar libros por título
#    Mostrar todos los libros disponibles


def menu_option():
    print ("1. add book")
    print ("2. search book")
    print ("3. show all books")
    print ("4. Exit the program")

def main():
    library = {}
    while True:
        menu_option()
        option = input("select a option: ")

        if option == "1":
            print ("add a book")
            Name = input("add the name of the book: ")
            Author = input ("add the author's name: ")
            Pag = int(input("add the page: "))
            library[Name] = {"Name": Name, "Author": Author, "Pag": Pag}
            print (f"Added book: {Name}, Author: {Author}, Pag: {Pag} ")

        elif option == "2":
            print ("search book")
            Name = input("write the book you want to search for: ")
            if Name in library:
                Book = library[Name]
                print (f"Book found: {Book['Name']}, Author: {Book['Author']}, Pag: {Book['Pag']}")
            else:
                print (f"Book {Name} not found")

        elif option == "3":
            print ("show all books")
            for book in library.values():
                print (f"Book: {book['Name']}, Author: {book['Author']}, Pag: {book['Pag']}")
        elif option == "4":
            print ("Exit the program")
            break
        else:
            print ("Invalid, try again")

if __name__ == "__main__":
     main()
