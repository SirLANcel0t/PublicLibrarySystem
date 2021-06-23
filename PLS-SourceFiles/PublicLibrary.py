import os
import json

from data import data, abs_path


class PublicLibrary:
    """
    De PublicLibrary class heeft onder andere de lijst van klanten, de functionaliteit om alle informatie van 
    boeken en klanten te backuppen en weer in te laden. Klanten kunnen ingeladen worden vanuit een CSV bestand,
    en klanten moeten hoogstwaarschijnlijk ook opgeslagen worden in een CSV bestand. 

    Is dit een abstract class? worden hier objecten van gemaakt? of blijft het alleen bij deze class? 
    """
    listOfCustomers = list()

    @staticmethod
    def writeJson(filePath, dataName, readmode = 'w'):
        with open(filePath, readmode) as json_file:
            json.dump(dataName, json_file, indent=4)

    @staticmethod
    def backupSystem():
        global data
        """
        een systeembackup slaat alle informatie over boeken en gebruikers op. 
        De vraag is alleen, moet alles in een .JSON bestand? Of gaan de boeken in een JSON bestand en de klanten
        in een .CSV bestand? 
        """
        with open(abs_path + '/json/backup.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)


    @staticmethod
    def loadSystemBackup():
        global data
        """
        Het inladen van een gemaakte backup. Waarschijnlijk bestaat dit uit een .JSON bestand met boeken, en een .CSV bestand
        met klanten.
        """ 
        filename = input("Enter backup filename here: ")
        with open(abs_path + f'/json/{filename}.json') as f:
            data = json.load(f)
            PublicLibrary.writeJson(abs_path + '/json/customers.json', data['customers'])
            PublicLibrary.writeJson(abs_path + '/json/librarians.json', data['librarians'])
            PublicLibrary.writeJson(abs_path + '/json/loanItems.json', data['loanItems'])
            PublicLibrary.writeJson(abs_path + '/json/books.json', data['books'])
        with open(abs_path + '/json/books.json') as f:
        	data['books'] = json.load(f)

    @staticmethod
    def loginUser(userInput, passInput, loginType, nameType = "username", passwordType = "password"):
        global data
        loggedIn = False
        with open(abs_path + f'/json/{loginType}.json') as f:
            data[loginType] = json.load(f)
            for i in data[loginType]:
                if userInput == i[nameType] and passInput == i[passwordType]:
                    loggedIn = True
                    return (loggedIn, loginType, i["name"])
                else:
                    loggedIn = False
        return (loggedIn, loginType, "guest")

    