"""
Public Library System! 
Analyse 3 summative assignment. Gemaakt door Mike, Luuk en Bruno uit INF1D

"""
import PLSbackend as BE
from PLSbackend import data, abs_path
import json
import csv
import sys


currentUser = "guest"
currentUserName = ""

# BE.clear()

def StartScreen():
    BE.clear()
    print(

    "\n▒█▀▄▀█ ▒█░░░ ▒█▀▀█ 　 ▒█░░░ ░▀░ █▀▀▄ █▀▀█ █▀▀█ █▀▀█ █░░█ 　 █▀▀ █░░█ █▀▀ ▀▀█▀▀ █▀▀ █▀▄▀█ \n"+
    "▒█▒█▒█ ▒█░░░ ▒█▀▀▄ 　 ▒█░░░ ▀█▀ █▀▀▄ █▄▄▀ █▄▄█ █▄▄▀ █▄▄█ 　 ▀▀█ █▄▄█ ▀▀█ ░░█░░ █▀▀ █░▀░█ \n"+
    "▒█░░▒█ ▒█▄▄█ ▒█▄▄█ 　 ▒█▄▄█ ▀▀▀ ▀▀▀░ ▀░▀▀ ▀░░▀ ▀░▀▀ ▄▄▄█ 　 ▀▀▀ ▄▄▄█ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░░▀\n"
    )


def MadeBy ():
    print("Welcome to MLB Public Library System \nThis interface was made by Mike, Luuk and Bruno from class INF1D\n")


######
# hieronder zijn allemaal functies die bepalen welk menu er getoond wordt aan de hand van 
# wie er preces ingelogd is. of als er niemand is ingelogd krijg je het meest algemene scherm te zien 
######

def MenuNoLogin(errorMessage = ""): 
    global currentUser, currentUserName
    possibleanswers = ["1", "2", "9"]
    answer = ""
    while answer not in possibleanswers:
        StartScreen()
        MadeBy()
        print(f"{errorMessage}Hi, {currentUser}.\n\nWhat would you like to do? (type the number)\n\n 1. Log in\n 2. Browse books\n 9. Exit Program\n")
        answer = input(">> ")
        if answer == "1" :
            loginMenu()
        elif answer == "2": 
            BookBrowser()
        elif answer == "9":
            CloseProgram()
        else:
            MenuNoLogin("Command not recognized, please try again.\n\n")

def loginMenu(errorMessage = ""):
    global currentUser, currentUserName
    answer = ""
    possibleAnswers = ["1", "2", "3"]
    while answer not in possibleAnswers:
        StartScreen()
        print(f"{errorMessage}\nLogin Menu\n\n 1. Log in as subscriber.\n 2. Log in as librarian.\n 3. Log in as publishing company.\n 9. Return to the main menu.\n")
        answer = input(">> ")
        if answer == "1":
            StartScreen()
            print("\nEnter login information for subscriber:\n")
            username = input("Enter username (email adress): ")
            password = input("Enter password (zipcode): ")
            loggedIn, currentUser, currentUserName = BE.PublicLibrary.loginUser(username, password, "customers", "EmailAddress", "ZipCode")
            if loggedIn:
                RunProgram()
            else:
                loginMenu("\nLogin failed. Please try again\n")
        elif answer == "2":
            StartScreen()
            print("\nEnter login information for librarian:\n")
            username = input("Enter username: ")
            password = input("Enter password: ")
            loggedIn, currentUser, currentUserName = BE.PublicLibrary.loginUser(username, password, "librarians")
            if loggedIn:
                RunProgram()
            else:
                loginMenu("\nLogin failed. Please try again\n")
        elif answer == "3":
            print("\nEnter login information for publishing company:\n")
            username = input("Enter username: ")
            password = input("Enter password: ")
            loggedIn, currentUser, currentUserName = BE.PublicLibrary.loginUser(username, password, "publishingcompany")
            if loggedIn:
                RunProgram()
            else:
                loginMenu("\nLogin failed. Please try again\n")
        elif answer == "9":
            RunProgram()
        else:
            loginMenu("\nCommand not recognized, please try again.\n")

def MenuLoggedIn(errorMessage = ""):
    global currentUser, currentUserName
    answer = ""
    possibleAnswers = ["1", "2", "9"]

    while answer not in possibleAnswers:
        StartScreen()
        print(f"{errorMessage}Hi, {currentUserName}.\n\nWhat would you like to do? (type the number)\n\n 1. Browse books\n 2. Loan/Return a book\n 9. Logout\n")
        answer = input(">> ")
        if answer == "1":
            BookBrowser()
        elif answer == "2":
            LoanMenu()
        elif answer == "9":
            currentUser = "guest"
            RunProgram()
        else:
            MenuLoggedIn("\nCommand not recognized, please try again.\n\n")

def MenuLibrarian(errorMessage = ""):
    global currentUser, currentUserName
    answer = ""
    possibleanswers = ["1", "2","3","4", "5", "6", "7","9"]

    while answer not in possibleanswers:
        StartScreen()
        print(f"{errorMessage}\nWelcome, {currentUserName}. What would you like to do?")
        print("\n 1. Add single book to database. \n 2. Add multiple books to database using JSON \n 3. Create new subscriber/librarian/publishing company. \n 4. Loan books + loan administration \n 5. Load / make system backup. \n 6. Browse Books \n 7. Add customers via CSV file \n 9. Logout. \n")
        answer = input(">> ")

        if answer == "1":
            registerBook()
        elif answer == "2":
            jsonbookfile = input("Type the name of the file here to load the books from JSON : ")
        
            try:
                with open(abs_path + f'//{jsonbookfile}.json') as f:
                    jsonbookfile2 = json.load(f)
                with open(abs_path + '/json/books.json', 'w') as json_file:
                    json.dump(jsonbookfile2, json_file, indent = 4)
                with open(abs_path + '/json/books.json') as f:
                    data['books'] = json.load(f)

                with open(abs_path + '/json/customers.json') as f:
                    data['customers'] = json.load(f)

                with open(abs_path + '/json/librarians.json') as f:
                    data['librarians'] = json.load(f)

                with open(abs_path + '/json/loanItems.json') as f:
                    data['loanItems'] = json.load(f)

                
                for item in data['books']:
                    AddToLoanItemsNew(item['title'], item['author'])
                print("Load succesfull. Press any key to continue...")
                a = input()
                RunProgram()

            except: 
                print("Load failed! Did you enter the correct filename?")
                a = input("Press any key to continue ...")
                RunProgram()

        elif answer == "3":
            registerMenu()
        elif answer == "4":
            print("You have selected: Loan books + loan administration")
            possibleanswers = ["1", "2", "3","9"]
            answer = ""

            while answer not in possibleanswers:
                print(f"\n 1. Loan a book to a customer \n 2. Return a loaned book \n 3. View loan administration \n 9. Return")
                answer = input()
                if answer == "1":

                    LoanItemOut()
                    # print("You have selected 1. Loan a book to a customer")


                    # whichbook = input("Name of book: ")
                    # dateloaned = input("Date of loan (DD-MM-YYYY): ")
                    # datereturn = input("Expected return date(DD-MM-YYYY): ")
                    # loanuser = input("Username to which the book will be loaned: ")
                    # newLoanItem = BE.LoanItem(whichbook, dateloaned, datereturn, loanuser)

                    # BE.LoanAdministration.loanItems.append(newLoanItem)
                    # # BE.PublicLibrary.writeJson('json/loanItems.json',  newLoanItem.__dict__ , 'a+')
                elif answer == "2":
                    ReturnLoanItem()
                    
                elif answer == "3":
                    print("You have selected 3. View loan administration")
                    print("Viewing all loaned books. Press any key to continue... ")
                    a = input()
                    BE.LoanAdministration.GetInfo()
                elif answer == "9":
                    print("Returning to previous menu...")
                    RunProgram()
            RunProgram()
        elif answer == "5":
            print("You have selected: 6. Load / make system backup")
            possibleanswers = ["1", "2","9"]
            answer = ""

            while answer not in possibleanswers:
                print(f"\n 1. Load system backup \n 2. Make system backup \n 9. Return to the main menu.\n")
                answer = input()
                if answer == "1":
                    BE.PublicLibrary.loadSystemBackup()
                    print("Backup loaded. Press any key to continue... ")
                    a = input()
                    RunProgram()
                elif answer == "2":
                    try:
                        BE.PublicLibrary.backupSystem()
                        print("Backup succesful. \nFile created as: backup.json.  ")
                        a = input()
                        RunProgram()
                    except: 
                        print("Backup failed. Did you enter the filename correctly?")
                elif answer == "9":
                    print("Returning to previous menu...")
                    RunProgram()
        elif answer == "6":
            BookBrowser()
        elif answer == "7":
            ImportCSV()
            RunProgram()
        elif answer == "9":
            currentUser = "guest"
            RunProgram()
        else: 
            MenuLibrarian("\nCommand not recognized, please try again.\n")

def registerMenu():
    answer = ""
    possibleAnswers = ["1", "2", "3"]

    while answer not in possibleAnswers:
        print("\n 1. Register a new subscriber.\n 2. Register a new librarian.\n 3. Register a new publishing company.")
        answer = input(" >> ")
        if answer == "1":
            registerCustomer()
        elif answer == "2":
            registerEmployee()
        elif answer == "3":
            registerPublishingCompany()
        else:
            print("Command not recognized, please try again.")

def registerEmployee():
    print("To register a new employee we need some information about the employee.")
    username = input("Username -> ")
    password = input("Password -> ")
    name = input("Full name -> ")

    try:
        BE.Librarian.registerEmployee(name,username,password)
        print("\nEmployee succesfully registered.")
    except:
        print("\nRegistering went wrong. Please try again.")
        registerEmployee()
    addAnotherCustomer = ""
    possibleAnswers = ["1","2"]
    while addAnotherCustomer not in possibleAnswers:
        addAnotherCustomer = input("\nWould you like to register another librarian?\n 1. Yes, please.\n 2. No, thank you.\n")
        if addAnotherCustomer == "1":
            registerEmployee()
        elif addAnotherCustomer == "2":
            print("\n")
            RunProgram()
        else:
            print("Command not recognized, please try again.")

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
    phoneNumber = input("Phone number -> ")
    try:
        print("in try")
        BE.Librarian.registerCustomer(language, gender, firstName, lastName, adress, zipCode, city, email, phoneNumber)
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
            RunProgram()
        else:
            print("Command not recognized, please try again.")

def registerPublishingCompany():
    print("To register a new customer we need some information about the publishing company.")
    name = input("Name -> ")
    username = input("Username ->")
    password = input("Password ->")
    try:
        BE.Librarian.registerPublishingCompany(name, username, password)
        print("\nPublishing Company succesfully registered.")
    except:
        print("\nRegistering went wrong.")
        registerPublishingCompany()
    addAnotherPublishingCompany = ""
    possibleAnswers = ['1', '2']
    while addAnotherPublishingCompany not in possibleAnswers:
        addAnotherPublishingCompany = input("\nWould you like to register another Publishing Company?\n 1. Yes, please. \n 2. No, thank you.\n")
        if addAnotherPublishingCompany == "1":
            registerPublishingCompany()
        elif addAnotherPublishingCompany == "2":
            print("\n")
            RunProgram()
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
        AddToLoanItemsNew(title, author)
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
            RunProgram()
        else:
            print("Command not recognized, please try again.")

## bookbrowser
def BookBrowser():
        print("\nList of books\n")

        def bookView():
            global bookIDCounter
            bookIDCounter = BE.Catalog.GetInfo()
            answer = ""
            possibleanswers = ["1", "2", "3", "4", "5", "9"]
            while answer not in possibleanswers:
                print("Would you like to:\n 1. Pick a book by Book ID.\n 2. Search book by Title.\n 3. Search by Author. \n 4. Search by publishing year.\n 5. Search by Language. \n 9. Return to main menu")
                answer = input("\n>> ")
                if answer == "1":
                    detailedBookView(bookIDCounter)
                    a = input("Press any key to continue...sup")
                elif answer == "2":
                    searchBookCatalog("title")
                elif answer == "3":
                    searchBookCatalog("author")
                elif answer == "4":
                    searchBookCatalog("year")
                elif answer == "5":
                    searchBookCatalog("language")
                elif answer == "9":
                    RunProgram()
                else:
                    print("\nInput not recognised. Please try again.")
                    answer = ""

        def searchBookCatalog(value):
            print(f"\nPlease enter the exact phrase for {value} search.")
            answer = input("\n>> ")
            for book in data['books']:
                if answer.lower() == book[value].lower():
                    print('Title: ' + book['title'])
                    print('Author: ' + book['author'])
                    print('Total pages: ' + str(book['pages']))
                    print('Published year: ' + str(book['year']))
                    print('Language: ' + book['language'])
                    print('Country: ' + book['country'])
                    print('Cover Image link: ' + book['imageLink'])
                    print('Website link: ' + book['link'])
            else:
                print(f"\nDisplaying all search results with parameter: {value} = {answer}")
                possibleAnswers = ["1", "2"]
                answer = ""
                while answer not in possibleAnswers:
                    print("\nWhat would you like to do.\n 1. Try another search.\n 2. View all books\n")
                    answer = input(">>")
                    if answer == "1":
                        bookView()
                    elif answer == "2":
                        bookView()
                    else:
                        print("Command not recognized, please try again.")
                        answer = ""

        def detailedBookView(bookIDCounter):
            global currentUser
            print("\nPlease pick a book by Book ID to see a more detailed view.")
            pickedBookID = input(">> ")
            try:
                pickedBookID = int(pickedBookID)
            except:
                print("\nThis Book ID does not exist. Please try again.")
                detailedBookView(bookIDCounter)
            if pickedBookID > bookIDCounter:
                print("\nThis Book ID does not exist. Please try again.")
                detailedBookView(bookIDCounter)
            print('Title: ' + data['books'][pickedBookID-1]['title'])
            print('Author: ' + data['books'][pickedBookID-1]['author'])
            print('Total pages: ' + str(data['books'][pickedBookID-1]['pages']))
            print('Published year: ' + str(data['books'][pickedBookID-1]['year']))
            print('Language: ' + data['books'][pickedBookID-1]['language'])
            print('Country: ' + data['books'][pickedBookID-1]['country'])
            print('Cover Image link: ' + data['books'][pickedBookID-1]['imageLink'])
            print('Website link: ' + data['books'][pickedBookID-1]['link'])

            if currentUser != "guest":
                possibleAnswers = ["1", "2", "9"]
                answer = ""
                while answer not in possibleAnswers:
                    print("\nWould you like to:\n 1. Loan a book\n 2. Browse books\n 9. Return to the main menu.\n")
                    answer = input(">> ")
                    if answer == "1":
                        LoanMenu()
                    elif answer == "2":
                        bookView()
                    elif answer == "9":
                        RunProgram()
                    else:
                        print("Input not recognised. Please try again. ")
                        answer = ""
            else:
                possibleAnswers = ["1", "2", "9"]
                answer = ""
                while answer not in possibleAnswers:
                    print("\nWould you like to:\n 1. Browse books\n 9. Return to the main menu.\n")
                    answer = input(">> ")
                    if answer == "1":
                        bookView()
                    elif answer == "9":
                        RunProgram()
                    else:
                        print("\nInput not recognised. Please try again.")
                        answer = ""

        bookView()

def AddToLoanItemsNew(title, author):
    newloanitemdict = {"bookItem": title, "author": author, "dateOfLoan" : "none", "dateOfReturn" : "none", "userOfItem" : "none", "isAvailable" : True}
    for item in data['loanItems']:
        if (item['bookItem'] == title) and (item['author'] == author) :
            print(f"{item['bookItem']} already exists")
            return 

    data['loanItems'].append(newloanitemdict)
    BE.PublicLibrary.writeJson(abs_path + '/json/loanItems.json', data['loanItems'])

def LoanMenu():
    answer = ""
    if currentUser == "librarians":
        possibleanswers = ["1", "2", "3","9"]
        while answer not in possibleanswers:
            StartScreen()
            print(f"\nLoan Menu\n\n 1. Loan a book to a customer \n 2. Return a loaned book \n 3. View loan administration \n 9. Return to main menu. \n")
            answer = input()
            if answer == "1":
                LoanItemOut()
            elif answer == "2":
                ReturnLoanItem()
            elif answer == "3":
                print("You have selected 3. View loan administration")
                print("Viewing all loaned books. Press any key to continue... ")
                a = input()
                BE.LoanAdministration.GetInfo()
            elif answer == "9":
                RunProgram()
        RunProgram()
    elif currentUser == "customers" or currentUser == "publishingcompany":
        possibleanswers = ["1", "9"]
        while answer not in possibleanswers:
            StartScreen()
            print(f"\nLoan Menu\n\n 1. Loan a book\n 2. Return a loaned book\n 9. Return to main menu.\n")
            answer = input(">> ")
            if answer == "1":
                LoanItemOut()
            elif answer == "2":
                ReturnLoanItem()
            elif answer == "9":
                RunProgram()
    elif currentUser == "guest":
        possibleanswers = ["1", "9"]
        while answer not in possibleanswers:
            StartScreen()
            print("\nLoan Menu\n\nYou can only loan a book while logged in.\n")
            print(f"\n 1. Log in\n 9. Return to main menu.\n")
            if answer == "1":
                loginMenu()
            elif answer == "9":
                RunProgram()
            else:
                x = input("\nCommand not recognized. Enter any key and try again.\n")

def LoanItemOut():
    global currentUser, currentUserName
    StartScreen()
    if len(data['loanItems']) == 0:
        print("There are no books in the entire library. Add books first.")
        a = input("\nPress any key to return to the main menu.")
        RunProgram()
    BE.Catalog.GetInfo()
    print("Loan a Book Menu\n\nType the title of the book you would like to loan. (Use the book browser to see available books)\n")
    booktitle = input(">> ")
    decidedonbook = False
    foundbook = 0
    
    for item in data['loanItems']:
        if booktitle.lower() == item['bookItem'].lower():
            foundbook += 1
            targetbook = item['bookItem'] 
            targetauthor = item['author']
    if foundbook == 1:
        print("\nYou have selected " + targetbook + " by " + targetauthor)
        decidedonbook = True
    elif foundbook > 1: 
        print(f"\nThere are multiple books by the name {targetbook}")
        for item in data['loanItems']:
            if targetbook == item['bookItem']:
                print(f"{item['bookItem']} by {item['author']}")
        targetauthor = input("Which author? ")     
        authorcheck = False   
        for item in data['loanItems']: 
            if targetbook == item['bookItem'] and targetauthor.lower() == item['author'].lower():
                print(f"{item['bookItem']} by {item['author']} it is. ")
                authorcheck = True
                decidedonbook = True
        if authorcheck == False:
            print("\nCould not find the author. Please check your spelling. ")

    else: 
        print("\nCould not find book. Please check your spelling.\n")
        a = input(">> ")
        LoanMenu()


    for item in data['loanItems']:
        
        checkvar = json.loads(json.dumps(item))
        if checkvar['bookItem'] == targetbook and checkvar['author'] == targetauthor and checkvar['isAvailable'] == False:
            print("\nThis book is not available! Please return this book before trying to loan it.")
            decidedonbook = False
            a = input("\nPress any key to return to the loan menu.")
            LoanMenu()
    if decidedonbook:
        dateLoan = input("From when will the book be loaned? (DD-MM-YYYY): ")
        datereturn = input("When does the book have to be returned? (DD-MM-YYYY): ")
        if currentUser == "customers":
            loanerusername = currentUserName
        else:
            loanerusername = input("What is the username of the person who will loan this book?: ")

        jsontopy = data['loanItems']

        for item in jsontopy: 
            if item['bookItem'] == targetbook and item['author'] == targetauthor:
                item['dateOfLoan'] = dateLoan
                item['dateOfReturn'] = datereturn
                item['userOfItem'] = loanerusername
                item['isAvailable'] = False


        with open(abs_path + '/json/loanItems.json', 'w') as outfile:
            json.dump(jsontopy, outfile, indent = 4)
        print(f"This book has now been loaned to {loanerusername} from {dateLoan} untill {datereturn}")
        a = input("\nPress any key to return to the main menu.")
        RunProgram()

def ReturnLoanItem():
    global currentUser, currentUserName
    print("\nWhich item would you like to return? ")
    targetbook = input("\nTitle of the book: ")
    
    if currentUser == "customers":
        targetusername = currentUserName
    else:
        targetusername = input("Username: ")
    foundbook = False
    for item in data['loanItems']:
        if item['bookItem'].lower() == targetbook.lower():
            foundbook = True
            break
    
    if foundbook:
        print(f"\nThis book is due on {item['dateOfReturn']}")

        if currentUserName == item['userOfItem'] or currentUser == "librarians":

            availableanswers = ["1", "2"]
            answer = "" 
            while answer not in availableanswers:
                print("Are you sure you want to return the book now? \n 1. Yes\n 2. No")
                answer = input()
                if answer == "1":
                    print("\nOK, returning book.")
                    try: 
                        jsontopy = data['loanItems']
                        for item in jsontopy: 
                            if item['bookItem'].lower() == targetbook.lower() and item['userOfItem'] == targetusername:
                                item['dateOfLoan'] = "none"
                                item['dateOfReturn'] = "none"
                                item['userOfItem'] = "none"
                                item['isAvailable'] = True

                                with open(abs_path + '/json/loanItems.json', 'w') as outfile:
                                    json.dump(jsontopy, outfile, indent = 4)
                    except: 
                        print("Something went horribly wrong. Please contact the servicedesk.")

                    a = input("Press any key to continue ...")
                elif answer == "2":
                    print("OK, not returning book. Heading back to main menu")
                    a = input("Press any key to continue ...")
        else:
            print("\nSorry you are not a librarian nor the user who has loaned this book. Therefor you can not return this book.")
            x = input("\nPress any key to return to the loan menu.")
            LoanMenu()
    else:
        print("Could not find the specified title / username combination. Did you enter the credentials correctly?")
        a = input("Press any key to continue to return to the Loan Menu.")

def ImportCSV():

    filename = input("What is the name of the file you are trying to import?: ") + ".csv"

#0Number,1Gender,2NameSet,3GivenName,4Surname,5StreetAddress,6ZipCode,7City,8EmailAddress,9Username,10TelephoneNumber
#1,male,Dutch,Hisham,Altink,"Borkelsedijk 53","5571 GA",Bergeijk,HishamAltink@teleworm.us,Reech1950,06-16898224

    try:
        with open(abs_path + f"//{filename}") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for item in csv_reader:
                if item[0] != "Number" and item[1] != "NameSet":
                    data['customers'].append({
                        "Number": item[0],
                        "NameSet": item[2],
                        "Gender": item[1],
                        "GivenName": item[3],
                        "Surname": item[4],
                        "StreetAddress": item[5],
                        "ZipCode": item[6],
                        "City": item[7],
                        "EmailAddress": item[8],
                        "TelephoneNumber": item[10],
                        "name": item[9]
                        })
            BE.PublicLibrary.writeJson(abs_path + '/json/customers.json', data['customers'])
            print("\nCustomers succesfully registered.")
            a = input("Press any key to continue ...")
            # RunProgram()

    except: 
        print("Something went wrong. Please try again and check for spelling.")
        a = input("Press any key to continue ...")
        # RunProgram()

def RunProgram():
    global currentUser
    if currentUser == "guest":
        MenuNoLogin()
    elif currentUser == "customers":
        MenuLoggedIn()
    elif currentUser == "publishingcompany":
        MenuLoggedIn()
    elif currentUser == "librarians":
        MenuLibrarian()
    else:
        BE.clear()
        print(f"ERROR: CURRENTUSER({currentUser}) -> RUNPROGRAM METHOD")
        currentUser = "guest"
        print("\nSomething went wrong.\n")
        x = input("\nPress any key to restart the program.")
        RunProgram()

def CloseProgram():
    print('Have a nice day!')
    sys.exit(1)

###########################################################
# dit wordt de te runnen code, het begin van de interface #
###########################################################


RunProgram()