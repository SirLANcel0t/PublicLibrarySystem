"""
Public Library System! 
Analyse 3 summative assignment. Gemaakt door Mike, Luuk en Bruno uit INF1D

"""
import os
import json
import jsonloads
from jsonloads import data

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
    def backupSystem():
        """
        een systeembackup slaat alle informatie over boeken en gebruikers op. 
        De vraag is alleen, moet alles in een .JSON bestand? Of gaan de boeken in een JSON bestand en de klanten
        in een .CSV bestand? 
        """
        pass
    @staticmethod
    def loadSystemBackup(backupFile):
        """
        Het inladen van een gemaakte backup. Waarschijnlijk bestaat dit uit een .JSON bestand met boeken, en een .CSV bestand
        met klanten.
        """ 
        pass
    @staticmethod
    def loadCustomers(customerFile):
        """
        Het inladen van een lijst met klanten middels een .CSV bestand.
        """
        pass
    @staticmethod
    def exportCustomers():
        """
        Klanten worden ingeladen middels het .CSV bestand wat we meegekregen hebben vanuit de opdracht, dus het is aannemelijk
        om er vanuit te gaan dat het exporteren van klanten ook in een .CSV bestand moet.
        Is deze functie overbodig? Is dit onderdeel van de functie backupSystem? 
        """
        pass
    @staticmethod
    def loginUser():
        pass

    @staticmethod
    def BookBrowser():
        """
        Het zoeken van boeken. w8 moet dit niet in de Catalog?
        """
        print("You typed: 2. Browse Books . But I also don't know how to do that yet. Please check back later")




class Person:
    """
    dit is de class Person, een superclass van librarian  en Customer. person is een 
    abstract class want van Person bestaan geen objecten (als het goed is). 

    """ 
    mayAddBooks = False
class Librarian(Person):
    """
    librarian is een subclass van Person. de librarian is de beheerder van het systeem en kan het systeem backuppen,
    een backup inladen, bookitems toevoegen en verwijderen, klanten toevoegen (zowel individueel als via een CSV bestand)
    boeken uitlenen voor klanten, en via een JSON bestand allemaal boeken inladen. 
    van librarian kunnen wel objecten gemaakt worden. je zou immers meerdere librarians kunnen hebben
    """

    mayAddBooks = True
    @staticmethod
    def createSubscriber():
        """
        Maak een nieuwe klantaccount (Subscriber)
        """

        newcustomernumber = int(input("Enter a customer number: "))
        # if customernumber in customer.json ofzoiets return een error
        # zegmaar dat als dit getal al bestaat in de customerlijst dat je dan een waarschuwing krijgt

        newcustomergender = ""
        while (newcustomergender != "male") and (newcustomergender != "female") and (newcustomergender != "other"):
            newcustomergender = input("Enter customer gender (male / female / other): ")
        nameSet = "Dutch"
        newcustomerfirstname = input("Enter customer's first name: ")
        newcustomerlastname = input("Enter customer's last name: ")
        newcustomerstreetaddress = input("Enter customer's adress: ")
        newcustomerzipcode = input("Enter customer's zipcode: ")
        newcustomercity = input("Enter customer's city: ")
        newcustomeremailaddress = input("Enter customer's email adress: ")
        newcustomerusername = input("Enter customer's username: ")
        newcustomertelephonenumber = int(input("Enter customer's telephone number: "))

        # en dit dan converteren naar JSON om het daarna in een bestand te schrijven
        newcustomerdict =  {
            "Number" : newcustomernumber,
            "NameSet" : nameSet,
            "Gender" : newcustomergender,
            "GivenName" : newcustomerfirstname,
            "Surname" : newcustomerlastname,
            "StreetAddress" : newcustomerstreetaddress,
            "ZipCode" : newcustomerzipcode,
            "City" : newcustomercity,
            "EmailAddress": newcustomeremailaddress,
            "Username" : newcustomerusername,
            "TelephoneNumber" : newcustomertelephonenumber,
        }
        outfile = open("newcustomerfile.json", "a")
        print(json.dumps(newcustomerdict))
        json.dump(newcustomerdict, outfile)


    
    def createBook(self):
        """
        Maak een nieuw boek aan met naam enzo
        """
        pass






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
        print("Tada een lijst met boeken")

        def bookView():
            bookIDCounter = 1
            with open('books.json') as json_file:
                bookCatalog = json.load(json_file)
                for book in bookCatalog['books']:
                    print(f"Book ID: {bookIDCounter}")
                    print('Title: ' + book['title'])
                    print('Author: ' + book['author'])
                    print('Language: ' + book['language'])
                    print('')
                    bookIDCounter += 1
            print("""
            Would you like to:
            1. Pick a book.
            2. Search book by Title.
            3. Search by Author. 
            4. Search by publishing year.
            5. Search by Language.
            """)
            bookViewMenuChoice = int(input(">>> "))
            if bookViewMenuChoice == 1:
                detailedBookView(bookIDCounter, bookCatalog)
            elif bookViewMenuChoice == 2:
                searchBookCatalog(bookCatalog, "title")
            elif bookViewMenuChoice == 3:
                searchBookCatalog(bookCatalog, "author")
            elif bookViewMenuChoice == 4:
                searchBookCatalog(bookCatalog, "year")
            elif bookViewMenuChoice == 5:
                searchBookCatalog(bookCatalog, "year")
            else:
                print("Entered wrong number. Please try again.")

        def searchBookCatalog(bookCatalog, value):
            userBookSearch = input("Please enter the exact phrase.\n>>> ")
            for book in bookCatalog['books']:
                if userBookSearch == book[value]:
                    print('Title: ' + book['title'])
                    print('Author: ' + book['author'])
                    print('Language: ' + book['year'])
                    print('Language: ' + book['language'])
                    print('Country: ' + book['country'])
                    print('Cover Imagse: ' + book['imageCover'])

        def detailedBookView(bookIDCounter, bookCatalog):
            print("Please pick a book to see a more detailed view.")
            pickedBookID = int(input(">>> "))
            if pickedBookID > bookIDCounter:
                print("This Book ID does not exist. Please try again.")
                detailedBookView(bookIDCounter, bookCatalog)
            clear()
            print('Title: ' + bookCatalog['books'][pickedBookID-1]['title'])
            print('Author: ' + bookCatalog['books'][pickedBookID-1]['author'])
            print('Language: ' + bookCatalog['books'][pickedBookID-1]['year'])
            print('Language: ' + bookCatalog['books'][pickedBookID-1]['language'])
            print('Country: ' + bookCatalog['books'][pickedBookID-1]['country'])
            print('Cover Imagse: ' + bookCatalog['books'][pickedBookID-1]['imageCover'])
            detailedBookChoice()


        def detailedBookChoice():
            print("\nWould you like to loan this book?\n 1. Hell yeah brother!\n 2. Show me all books again.\n 3. I would like to go to Hawaii, please.")
            userDetailedChoise = int(input(">>> "))

            if userDetailedChoise == 1:
                print("Right on, enjoy the book mate!")
                exit()
            elif userDetailedChoise == 2:
                Catalog.BookBrowser()
            elif userDetailedChoise == 3:
                print("Sir, this is a Public Library System")
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

