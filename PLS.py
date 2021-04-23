"""
Public Library System! 
Analyse 3 summative assignment. Gemaakt door Mike, Luuk en Bruno uit INF1D

"""
import os

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
        global currentUser
        """
        het loginscherm 
        """

        print("You typed: 1. Login .")

        username = input("Type username: ")
        password = input("Type password: ")

        if username == "librarian" and password == "secret":
            currentUser = "librarian"
            MenuLibrarian()
        else:
            print("Input not recognised")
            RunProgram()

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

    def createSubscriber(self):
        """
        Maak een nieuwe klantaccount (Subscriber)
        """
        pass
    
    def createBook(self):
        """
        Maak een nieuw boek aan met ISBN en naam enzo
        """
        pass



class Subscriber(Person):
    """
    Subscriber is een klant. Objecten van deze class kunnen boeken zoeken, boekeninformatie inzien, boeken lenen voor een
    bepaalde tijd. 
    """

    # nu worden deze variableen nog in Customer class gemaakt, maar misschien kunen die al in
    # person class gedefineerd worden? 

    def __init__(self, userNumber, gender, nameSet, givenName, surName, streetAdress, zipCode, city, emailAdress, userName, password, telephoneNumber):
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
        self.password = password
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
        print("You typed: 2. Browse Books . But I also don't know how to do that yet. Please check back later")

    

class LoanAdministration: 
    """
    In deze class LoanAdministration staan de LoanItems oftewel de informatie over uitgeleende items.
    Dat zijn uitgeleende boeken met bijbehorende informatie over wanneer ze terug moeten
    """
    # een lijst met alle loanitems
    loanItems = list()

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



print("Welcome to MLB Public Library System \nThis interface was made by Mike, Luuk and Bruno from class INF1D")


######
# hieronder zijn allemaal functies die bepalen welk menu er getoond wordt aan de hand van 
# wie er preces ingelogd is. of als er niemand is ingelogd krijg je het meest algemene scherm te zien 
######

def MenuNoLogin(): 
    global currentUser
    possibleanswers = ["1", "2", "3", "4", "5"]
    answer = ""
    while answer not in possibleanswers:
        print("Hi, anonymous user. \nWhat would you like to do? (type the number) \n 1. Login \n 2. Browse books \n 3. Exit Program \n 4. (test boekje) \n 5. (test user object) \n")

        answer = input()


        if answer == "1" :
            PublicLibrary.loginUser()

        elif answer == "2": 
            Catalog.BookBrowser()

        elif answer == "3":
            print("OK, cya")
            break

        elif answer == "4":
            boekje = Book("jezus", "israel", "heb ik niet", "hebreeuws", "internet hadden ze toen nog niet", 800, "de bijbel", 0)

            boekje.GetInfo()
        
        elif answer == "5":
            hans = Subscriber(5,"male", "Dutch", "Hans", "de Boer", "Lange Lindelaan 14", "3011BB", "Rotterdam", "hansjepansje@gmail.com", "masterhans123", "zomaareenwachtwoord", "0619283755")

            print(hans)
        else:
            print("Unrecognized command")

        answer = input("Press any key to continue ...")

def MenuLibrarian():
    global currentUser
    answer = ""
    possibleanswers = ["1", "2","3","4"]

    while answer not in possibleanswers:
        print(" 1. Modify catalog \n 2. Load / make system backup \n 3. Do something else idk \n 4. Logout ")

        answer = input()

        if answer == "1":
            print(r"¯\(°_o)/¯")
            a = input()
            MenuLibrarian()
        elif answer == "2":
            print(r"¯\(°_o)/¯")
            a = input()
            MenuLibrarian()
        elif answer == "3":
            print(r"¯\(°_o)/¯")
            a = input()
            MenuLibrarian()
        elif answer == "4":
            currentUser = "nobody"
            print("Logging out...")
            a = input()
            RunProgram()

        else: 
            print("Unrecognised command!")

        answer = input("Press any key to continue ...")


def RunProgram():
    if currentUser == "nobody":
        MenuNoLogin()
    elif currentUser == "Librarian":
        print(f"Welcome, Librarian. What would you like to do?")
        MenuLibrarian()


###########################################################
# dit wordt de te runnen code, het begin van de interface #
###########################################################


RunProgram()


