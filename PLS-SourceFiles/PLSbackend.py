"""
Public Library System! 
Analyse 3 summative assignment. Gemaakt door Mike, Luuk en Bruno uit INF1D

"""
import os
import json
from data import data, abs_path

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

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


from PublicLibrary import PublicLibrary
from Book import Book
from BookItem import BookItem
from Catalog import Catalog
from LoanAdministration import LoanAdministration
from LoanItem import LoanItem
from Person import Person, Librarian, Subscriber