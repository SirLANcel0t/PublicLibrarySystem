import os
import json
from data import data, abs_path

from PublicLibrary import PublicLibrary

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
        PublicLibrary.writeJson(abs_path + '/json/librarians.json', data['librarians'])

    mayAddBooks = True
    @staticmethod
    def registerCustomer(nameSet, customergender, customerfirstname, customerlastname, customerstreetaddress, customerzipcode, customercity, customeremailaddress, customertelephonenumber):
        
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
            'TelephoneNumber' : customertelephonenumber,
            'name': customerfirstname,
        })
        PublicLibrary.writeJson(abs_path + '/json/customers.json', data['customers'])
    @staticmethod
    def registerPublishingCompany(pCompanyName, pCompanyUsername, pCompanyPassword):
        
        pCompanyNumber = str(len(data['publishingcompany'])+1)
        data['publishingcompany'].append({
            'number': pCompanyNumber,
            'name': pCompanyName,
            'username': pCompanyUsername,
            'password': pCompanyPassword,
        })
        PublicLibrary.writeJson(abs_path + '/json/publishingcompany.json', data['publishingcompany'])

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
        PublicLibrary.writeJson(abs_path + '/json/books.json', data['books'])


class Subscriber(Person):
    """
    Subscriber is een klant. Objecten van deze class kunnen boeken zoeken, boekeninformatie inzien, boeken lenen voor een
    bepaalde tijd. 
    """

    # nu worden deze variableen nog in Customer class gemaakt, maar misschien kunen die al in
    # person class gedefineerd worden? 

    def __init__(self, userNumber, gender, nameSet, givenName, surName, streetAdress, zipCode, city, emailAdress, telephoneNumber):
        self.userNumber = userNumber
        self.gender = gender
        self.nameSet = nameSet
        self.givenName = givenName
        self.surName = surName
        self.streetAdress = streetAdress
        self.zipCode = zipCode
        self.city = city
        self.emailAdress = emailAdress
        self.telephoneNumber = telephoneNumber
        self.name = givenName

    def __str__(self):
        return f"Usernumber: {self.userNumber}\nName: {self.givenName} {self.surName}\nUsername: {self.emailAdress} \n"

    @staticmethod
    def revealpassword(self):
        print(self.zipCode)


class PublishingCompany(Person):

    def __init__(self, pCompanyName, pCompanyUser, pCompanyPassword):
        self.pCompanyName = pCompanyName
        self.pCompanyUser = pCompanyUser
        self.pCompanyPassword = pCompanyPassword

    def __str__(self):
        return f"Publishing Company Number: {self.pCompanyNumber}\nCompany Name: {self.pCompanyName}\n"

    @staticmethod
    def revealpassword(self):
        print(self.zipCode)