import os
import json
from data import data, abs_path

class Catalog:

    """
    In de catalogus staan alle boeken die in de bibliotheek te vinden zijn. Hier binnen komt hoogst waarschijnlijk
    de lijst met alle boeken, en deze class wordt geraadpleegd wanneer klanten op zoek zijn naar een boek. 
    Als een boek geleend wordt, werkt deze class samen met class LoanAdministration en wordt er een loanItem
    aangemaakt.

    In deze class komt een lijst met Books. Dus niet de bookItems, want dat is voor de LoanAdministration. 
    """
    @staticmethod
    def GetInfo():
        bookIDCounter = 0
        for book in data['books']:
            bookIDCounter += 1
            print(f"Book ID: {bookIDCounter}")
            print('Title: ' + book['title'])
            print('Author: ' + book['author'])
            print('Language: ' + book['language'])
            print('')
        return bookIDCounter
