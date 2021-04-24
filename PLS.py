"""
Public Library System! 
Analyse 3 summative assignment. Gemaakt door Mike, Luuk en Bruno uit INF1D

"""
import PLSbackend as BE
from PLSbackend import data


currentUser = "anonymous user"

BE.clear()
print(

"▒█▀▄▀█ ▒█░░░ ▒█▀▀█ 　 ▒█░░░ ░▀░ █▀▀▄ █▀▀█ █▀▀█ █▀▀█ █░░█ 　 █▀▀ █░░█ █▀▀ ▀▀█▀▀ █▀▀ █▀▄▀█ \n"+
"▒█▒█▒█ ▒█░░░ ▒█▀▀▄ 　 ▒█░░░ ▀█▀ █▀▀▄ █▄▄▀ █▄▄█ █▄▄▀ █▄▄█ 　 ▀▀█ █▄▄█ ▀▀█ ░░█░░ █▀▀ █░▀░█ \n"+
"▒█░░▒█ ▒█▄▄█ ▒█▄▄█ 　 ▒█▄▄█ ▀▀▀ ▀▀▀░ ▀░▀▀ ▀░░▀ ▀░▀▀ ▄▄▄█ 　 ▀▀▀ ▄▄▄█ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░░▀\n"
)


print("Welcome to MLB Public Library System \nThis interface was made by Mike, Luuk and Bruno from class INF1D")


######
# hieronder zijn allemaal functies die bepalen welk menu er getoond wordt aan de hand van 
# wie er preces ingelogd is. of als er niemand is ingelogd krijg je het meest algemene scherm te zien 
######

def MenuNoLogin(): 
    global currentUser
    possibleanswers = ["1", "2", "3", "4", "5", "9"]
    answer = ""
    while answer not in possibleanswers:
        print(f"Hi, {currentUser}. \nWhat would you like to do? (type the number) \n 1. Login \n 2. Browse books \n 3. Exit Program \n 4. (test boekje) \n 5. (test user object) \n")

        answer = input()


        if answer == "1" :
            username = input("Enter username: ")
            password = input("Enter password: ")
            loggedIn, currentUser = BE.PublicLibrary.loginUser(username,password)
            if loggedIn:
                MenuLibrarian()
            else:
                print("Login failed. Please try again")


        elif answer == "2": 
            BE.Catalog.BookBrowser()

        elif answer == "4":
            boekje = BE.Book("jezus", "israel", "heb ik niet", "hebreeuws", "internet hadden ze toen nog niet", 800, "de bijbel", 0)

            boekje.GetInfo()
        
        elif answer == "5":
            hans = BE.Subscriber(5,"male", "Dutch", "Hans", "de Boer", "Lange Lindelaan 14", "3011BB", "Rotterdam", "hansjepansje@gmail.com", "masterhans123", "0619283755")

            print(hans)

        elif answer == "9":
            print("OK, cya")
            break
        else:
            print("Command not recognized, please try again.")

        answer = input("Press any key to continue ...")

def MenuLibrarian():
    global currentUser
    answer = ""
    possibleanswers = ["1", "2","3","4", "5","9"]

    print(f"\nWelcome, Librarian. What would you like to do?")
    while answer not in possibleanswers:
        print("\n 1. Add book to database. \n 2. Create new subscriber. \n 3. View loaned items. \n 4. Load / make system backup. \n 5. Browse Books \n 9. Logout. \n")

        answer = input(" >> ")

        if answer == "1":
            registerBook()
        elif answer == "2":
            registerCustomer()
        elif answer == "3":
            print("loaned item ook nog niks")
            a = input()
            MenuLibrarian()
        elif answer == "4":
            print("You have selected: 4. Load / make system backup")
            possibleanswers = ["1", "2","9"]
            answer = ""

            while answer not in possibleanswers:
                print(f"\n 1. Load system backup \n 2. Make system backup \n 9. Return to previous menu")
                answer = input()
                if answer == "1":
                    #loadsystembackup()
                    BE.PublicLibrary.loadSystemBackup()
                    print("Backup loaded.")
                    a = input()
                    MenuLibrarian()
                elif answer == "2":
                    #makebackup
                    
                    BE.PublicLibrary.backupSystem()
                    print("Backup created. ")
                    a = input()
                    MenuLibrarian()
                elif answer == "9":
                    print("Returning to previous menu...")
                    MenuLibrarian()
        elif answer == "5":
            BE.Catalog.BookBrowser()
        elif answer == "9":
            currentUser = "anonymous user"
            print("Logging out...")
            a = input()
            RunProgram()

        else: 
            print("Command not recognized, please try again.")

        # answer = input("Press any key to continue ...")

def registerCustomer():
    print("To register a new customer we need some information about the customer.")
    language = input("Language -> ")
    gender = input("Gender -> ")
    firstName = input("First name -> ")
    lastName = input("Last name -> ")
    adress = input("Adress -> ")
    zipCode = input("ZipCode -> ")
    city = input("City -> ")
    email = input("Email -> ")
    username = input("Username -> ")
    phoneNumber = input("Phone number -> ")
    try:
        BE.Librarian.registerCustomer(language, gender, firstName, lastName, adress, zipCode, city, email, username, phoneNumber)
        print("\nCustomer succesfully registered.")
    except:
        print("\nRegistering went wrong. Please try again.")
        registerCustomer()
    addAnotherCustomer = ""
    possibleAnswers = ["1","2"]
    while addAnotherCustomer not in possibleAnswers:
        addAnotherCustomer = input("\nWould you like to register another customer?\n 1. Yes, please.\n 2. No, thank you.\n")
        if addAnotherCustomer == "1":
            registerCustomer()
        elif addAnotherCustomer == "2":
            print("\n")
            MenuLibrarian()
        else:
            print("Command not recognized, please try again.")

def registerBook():
    print("To register a new book we need some information.")
    title = input("Book title -> ")
    author = input("Book Author -> ")
    pages = input("Total pages -> ")
    year = input("Publishing year -> ")
    country = input("Country -> ")
    language = input("Book Language -> ")
    imageLink = input("Image link -> ")
    link = input("Website link -> ")
    try:
        BE.Librarian.registerBook(author, country, imageLink, language, link, pages, title, year)
        print("\nBook was succesfully added to the database.")
    except:
        print("\nSomething went wrong. Please try again.")
        registerBook()
    addAnotherBook = ""
    possibleAnswers = ["1","2"]
    while addAnotherBook not in possibleAnswers:
        addAnotherBook = input("\nWould you like to add another book?\n 1. Yes, please.\n 2. No, thank you.\n")
        if addAnotherBook == "1":
            registerBook()
        elif addAnotherBook == "2":
            print("\n")
            MenuLibrarian()
        else:
            print("Command not recognized, please try again.")



def RunProgram():
    if currentUser == "anonymous user":
        MenuNoLogin()
    elif currentUser == "Librarian":
        MenuLibrarian()


###########################################################
# dit wordt de te runnen code, het begin van de interface #
###########################################################


RunProgram()

