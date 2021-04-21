"""
Public Library System! 
Analyse 3 summative assignment. Gemaakt door Mike, Luuk en Bruno uit INF1D.

"""
import os

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

# het maken van PublicLibrary, de class
class PublicLibrary:
    """
    De PublicLibrary class heeft onder andere de lijst van klanten, de functionaliteit om alle informatie van 
    boeken en klanten te backuppen en weer in te laden. Klanten kunnen ingeladen worden vanuit een CSV bestand,
    en klanten moeten hoogstwaarschijnlijk ook opgeslagen worden in een CSV bestand. 

    Is dit een abstract class? worden hier objecten van gemaakt? of blijft het alleen bij deze class? 
    """
    def __init__(self, listofcustomers):
        self.listofcustomers = listofcustomers
    
    def backupSystem(self):
        """
        een systeembackup slaat alle informatie over boeken en gebruikers op. 
        De vraag is alleen, moet alles in een .JSON bestand? Of gaan de boeken in een JSON bestand en de klanten
        in een .CSV bestand? 
        """
        pass

    def loadSystemBackup(self):
        """
        Het inladen van een gemaakte backup. Waarschijnlijk bestaat dit uit een .JSON bestand met boeken, en een .CSV bestand
        met klanten.
        """ 
        pass

    def loadCustomers(self):
        """
        Het inladen van een lijst met klanten middels een .CSV bestand.
        """
        pass

    def exportCustomers(self):
        """
        Klanten worden ingeladen middels het .CSV bestand wat we meegekregen hebben vanuit de opdracht, dus het is aannemelijk
        om er vanuit te gaan dat het exporteren van klanten ook in een .CSV bestand moet.
        Is deze functie overbodig? Is dit onderdeel van de functie backupSystem? 
        """
        pass



class Person:
    """
    dit is de class Person, een superclass van librarian  en Customer. person is een 
    abstract class want van Person bestaan geen objecten. 

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
    
    # het is misschien niet heel logisch om login bij Customer te hebben
    # ik bedoel de customer krijg je als je inlogt, toch? 
    def login(self):
        pass


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

        #print(f"Author: {self.author}\n")
    


class Catalog:

    """
    In de catalogus staan alle boeken die in de bibliotheek te vinden zijn. Hier binnen komt hoogst waarschijnlijk
    de lijst met alle boeken, en deze class wordt geraadpleegd wanneer klanten op zoek zijn naar een boek. 
    Als een boek geleend wordt, werkt deze class samen met class LoanAdministration en wordt er een loanItem
    aangemaakt.
    """
    def __init__(self):
        pass





nextInLine = 5
# json bestand uitlezen en laatste cijfer zoeken

hans = Subscriber(nextInLine,"male", "Dutch", "Hans", "de Boer", "Lange Lindelaan 14", "3011BB", "Rotterdam", "hansjepansje@gmail.com", "masterhans123", "zomaareenwachtwoord", "0619283755")



# dit wordt de te runnen code, het begin van de interface
print("Welcome to MLB Public Library System \nThis interface was made by Mike, Luuk and Bruno from class INF1D")

answer = ""

possibleanswers = ["1", "2", "3", "4"]
while answer not in possibleanswers:
    print("What would you like to do? (type the number) \n 1. Login \n 2. Browse books \n 3. Exit Program \n 4. (test boekje)")

    answer = input()


    if answer == "1" :
        print("You typed: 1. Login . But I don't know how to do that yet. Please check back later")

    elif answer == "2": 
        print("You typed: 2. Browse Books . But I also don't know how to do that yet. Please check back later")

    elif answer == "3":
        print("OK, cya")
        break

    elif answer == "4":
        boekje = Book("jezus", "israel", "heb ik niet", "hebreeuws", "internet hadden ze toen nog niet", 800, "de bijbel", 0)

        boekje.GetInfo()

    else:
        print("Unrecognized command")

    answer = input("Press any key to continue ...")

