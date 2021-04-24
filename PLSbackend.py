"""
Public Library System! 
Analyse 3 summative assignment. Gemaakt door Mike, Luuk en Bruno uit INF1D

"""
import os
import json

data = {}
data['librarians'] = []
data['customers'] = []
data['books'] = []

with open('json/books.json') as f:
    data['books'] = json.load(f)

with open('json/customers.json') as f:
    data['customers'] = json.load(f)

with open('json/librarians.json') as f:
    data['librarians'] = json.load(f)

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

currentUser = "nobody"

"""
Volgorde van classes: 
PublicLibrary
Person
Subscriber
Book
BookItem
Catalog
LoanAdministration
LoanItem
"""

# het maken van PublicLibrary, de class
class PublicLibrary:
    """
    De PublicLibrary class heeft onder andere de lijst van klanten, de functionaliteit om alle informatie van 
    boeken en klanten te backuppen en weer in te laden. Klanten kunnen ingeladen worden vanuit een CSV bestand,
    en klanten moeten hoogstwaarschijnlijk ook opgeslagen worden in een CSV bestand. 

    Is dit een abstract class? worden hier objecten van gemaakt? of blijft het alleen bij deze class? 
    """
    listOfCustomers = list()

    @staticmethod
    def writeJson(filePath, dataName):
        with open(filePath, 'w') as json_file:
            json.dump(dataName, json_file, indent=4)

    @staticmethod
    def backupSystem():
        global data
        """
        een systeembackup slaat alle informatie over boeken en gebruikers op. 
        De vraag is alleen, moet alles in een .JSON bestand? Of gaan de boeken in een JSON bestand en de klanten
        in een .CSV bestand? 
        """
        with open('json/backup.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def loadSystemBackup():
        global data
        """
        Het inladen van een gemaakte backup. Waarschijnlijk bestaat dit uit een .JSON bestand met boeken, en een .CSV bestand
        met klanten.
        """ 
        with open('json/backup.json') as f:
            data = json.load(f)

    @staticmethod
    def loginUser(userInput, passInput):
        global data
        loggedIn = False
        with open('json/librarians.json') as f:
            data['librarians'] = json.load(f)
            for i in data['librarians']:
                if userInput == i['username'] and passInput == i['password']:
                    loggedIn = True
                else:
                    loggedIn = False
        return (loggedIn, userInput)

class Person:
    """
    dit is de class Person, een superclass van librarian  en Customer. person is een 
    abstract class want van Person bestaan geen objecten (als het goed is). 

    """ 

    #de constructor van Person
    def __init__(self, name, username):
        self.Name = name
        self.userName = username


    
class Librarian(Person):
    global data
    """
    librarian is een subclass van Person. de librarian is de beheerder van het systeem en kan het systeem backuppen,
    een backup inladen, bookitems toevoegen en verwijderen, klanten toevoegen (zowel individueel als via een CSV bestand)
    boeken uitlenen voor klanten, en via een JSON bestand allemaal boeken inladen. 
    van librarian kunnen wel objecten gemaakt worden. je zou immers meerdere librarians kunnen hebben

    een voorbeeld hoe je een librarian maakt (in PLS.py) : 

    Bibliotheekmedewerker_Marianne = BE.Librarian("Marianne", "marriewarrie12345", "supergeheimwachtwoord")
    print(Bibliotheekmedewerker_Marianne)
    Bibliotheekmedewerker_Marianne.revealpassword()
    """



    def __init__(self, name, username, password):
        Person.__init__(self, name, username)
        self.password = password

    def __str__(self):
        return f" Name: {self.Name} \n Username: {self.userName} \n"
    
    def revealpassword(self):
        print(self.password)


    mayAddBooks = True
    @staticmethod
    def registerEmployee(fullName, username, password):
        data['librarians'].append({
            'name': fullName,
            'username': username,
            'password': password
        })
    PublicLibrary.writeJson('json/librarians.json', data['librarians'])

    mayAddBooks = True
    @staticmethod
    def registerCustomer(nameSet, customergender, customerfirstname, customerlastname, customerstreetaddress, customerzipcode, customercity, customeremailaddress, customerusername, customertelephonenumber):
        
        customerNumber = str(len(data['customers'])+1)
        data['customers'].append({
            'Number' : customerNumber,
            'NameSet' : nameSet,
            'Gender' : customergender,
            'GivenName' : customerfirstname,
            'Surname' : customerlastname,
            'StreetAddress' : customerstreetaddress,
            'ZipCode' : customerzipcode,
            'City' : customercity,
            'EmailAddress' : customeremailaddress,
            'Username' : customerusername,
            'TelephoneNumber' : customertelephonenumber,
        })
        PublicLibrary.writeJson('json/customers.json', data['customers'])


    @staticmethod
    def registerBook(author, country, imageLink, language, link, pages, title, year):
        data['books'].append({
            'title': title,
            'author': author,
            'pages': pages,
            'year': year,
            'country': country,
            'language': language,
            'imageLink': imageLink,
            'link': link
        })
        PublicLibrary.writeJson('json/books.json', data['books'])






class Subscriber(Person):
    """
    Subscriber is een klant. Objecten van deze class kunnen boeken zoeken, boekeninformatie inzien, boeken lenen voor een
    bepaalde tijd. 
    """

    # nu worden deze variableen nog in Customer class gemaakt, maar misschien kunen die al in
    # person class gedefineerd worden? 

    def __init__(self, userNumber, gender, nameSet, givenName, surName, streetAdress, zipCode, city, emailAdress, userName, telephoneNumber):
        self.userNumber = userNumber
        self.gender = gender
        self.nameSet = nameSet
        self.givenName = givenName
        self.surName = surName
        self.streetAdress = streetAdress
        self.zipCode = zipCode
        self.city = city
        self.emailAdress = emailAdress
        self.userName = userName
        self.telephoneNumber = telephoneNumber

    def __str__(self):
        return f"Usernumber: {self.userNumber}\nName: {self.givenName} {self.surName}\nUsername: {self.userName} \n"


class Book:
    def __init__(self, author, country, imageLink, language, link, pages, title, year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.title = title
        self.year = year
    
    def GetInfo(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nCountry: {self.country}\nLanguage: {self.language}\nYear: {self.year}\nPages: {self.pages}\nLink: {self.link}\nImage link: {self.imageLink}")

class BookItem:
    """
    Het verschil met Book en BookItem is dat Book zegmaar de informatie is over het boek in de applicatie,
    en BookItem is het daadwerkelijke boek. Als je een boek leent dan leen je een BookItem en niet een Book. 
    """
    pass

class Catalog:

    """
    In de catalogus staan alle boeken die in de bibliotheek te vinden zijn. Hier binnen komt hoogst waarschijnlijk
    de lijst met alle boeken, en deze class wordt geraadpleegd wanneer klanten op zoek zijn naar een boek. 
    Als een boek geleend wordt, werkt deze class samen met class LoanAdministration en wordt er een loanItem
    aangemaakt.

    In deze class komt een lijst met Books. Dus niet de bookItems, want dat is voor de LoanAdministration. 
    """

    @staticmethod 
    def BookBrowser():
        clear()
        print("\nTada een lijst met boeken\n")

        def bookView():
            bookIDCounter = 1
            for book in data['books']:
                print(f"Book ID: {bookIDCounter}")
                print('Title: ' + book['title'])
                print('Author: ' + book['author'])
                print('Language: ' + book['language'])
                print('')
                bookIDCounter += 1
            print("\nWould you like to:\n 1. Pick a book.\n 2. Search book by Title.\n 3. Search by Author. \n 4. Search by publishing year.\n 5. Search by Language.")
            bookViewMenuChoice = input("\n>>> ")
            if bookViewMenuChoice == "1":
                detailedBookView(bookIDCounter)
            elif bookViewMenuChoice == "2":
                searchBookCatalog("title")
            elif bookViewMenuChoice == "3":
                searchBookCatalog("author")
            elif bookViewMenuChoice == "4":
                searchBookCatalog("year")
            elif bookViewMenuChoice == "5":
                searchBookCatalog("language")
            else:
                print("Entered wrong number. Please try again.")

        def searchBookCatalog( value):
            bookFound = False
            userBookSearch = input(f"\nPlease enter the exact phrase for {value} search.\n>>> ")
            for book in data['books']:
                if userBookSearch == book[value]:
                    print('Title: ' + book['title'])
                    print('Author: ' + book['author'])
                    print('Total pages: ' + book['pages'])
                    print('Published year: ' + book['year'])
                    print('Language: ' + book['language'])
                    print('Country: ' + book['country'])
                    print('Cover Image link: ' + book['imageLink'])
                    print('Website link: ' + book['link'])
                    bookFound = True
            if bookFound == True:
                detailedBookChoice()
            else:
                print(f"\nThere is no book which {value} matches your search phrase.")
                possibleAnswers = ["1", "2"]
                answer = ""
                while answer not in possibleAnswers:
                    answer = input("\nWhat would you like to do.\n 1. Try another search.\n 2. View all books\n >> ")
                    if answer == "1":
                        bookView()
                    elif answer == "2":
                        bookView()
                    else:
                        print("Command not recognized, please try again.")





        def detailedBookView(bookIDCounter):
            print("\nPlease pick a book to see a more detailed view.")
            pickedBookID = int(input(">>> "))
            if pickedBookID > bookIDCounter:
                print("\nThis Book ID does not exist. Please try again.")
                detailedBookView(bookIDCounter)
            clear()
            print('Title: ' + data['books'][pickedBookID-1]['title'])
            print('Author: ' + data['books'][pickedBookID-1]['author'])
            print('Total pages: ' + data['books'][pickedBookID-1]['pages'])
            print('Published year: ' + data['books'][pickedBookID-1]['year'])
            print('Language: ' + data['books'][pickedBookID-1]['language'])
            print('Country: ' + data['books'][pickedBookID-1]['country'])
            print('Cover Image link: ' + data['books'][pickedBookID-1]['imageLink'])
            print('Website link: ' + data['books'][pickedBookID-1]['link'])
            detailedBookChoice()


        def detailedBookChoice():
            print("\nWould you like to loan this book?\n 1. Hell yeah brother!\n 2. Show me all books again.\n 3. I would like to go to Hawaii, please.")
            userDetailedChoise = int(input(">>> "))

            if userDetailedChoise == 1:
                print("\nRight on, enjoy the book mate!")
                exit()
            elif userDetailedChoise == 2:
                Catalog.BookBrowser()
            elif userDetailedChoise == 3:
                print("\nSir, this is a Public Library System")
                detailedBookChoice()
            else:
                detailedBookChoice()

        bookView()


class LoanAdministration: 
    """
    In deze class LoanAdministration staan de LoanItems oftewel de informatie over uitgeleende items.
    Dat zijn uitgeleende boeken met bijbehorende informatie over wanneer ze terug moeten
    """
    # een lijst met alle loanitems
    loanItems = list()

    @staticmethod
    def LoanMenu():
        print("Entering loan administration menu ...")
        print("")
        possibleanswers = ["1", "2", "3", "4", "5", "9"]
        answer = ""
        while answer not in possibleanswers:
            pass
    @staticmethod
    def GetInfo(self):
        for item in self.loanItems:
            print(f" Book: {item.bookItem}\n Date loaned: {item.dateOfLoan}\n Expected return date: {item.dateOfReturn}\n")

class LoanItem:
    """
    In deze class staat informatie van boeken en van wanneer tot wanneer ze uitgeleend zijn. Dit is 
    eigenlijk het fysieke boek in de bibliotheek.  
    """

    def __init__(self, whichBook, dateOfLoan, dateOfReturn, username):
        """
        whichBook moet een bookItem zijn
        dateOfLoan is een string met wanneer hij uitgeleend is
        dateOfReturn is een string wanneer hij terug moet zijn
        userOfItem wordt de persoon die het boek geleend heeft. 
        """
        self.bookItem = whichBook
        self.dateOfLoan = dateOfLoan
        self.dateOfReturn = dateOfReturn
        self.userOfItem = username
