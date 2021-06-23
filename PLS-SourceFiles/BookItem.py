import os
import json
from data import data, abs_path

class BookItem:
    """
    Het verschil met Book en BookItem is dat Book zegmaar de informatie is over het boek in de applicatie,
    en BookItem is het daadwerkelijke boek. Als je een boek leent dan leen je een BookItem en niet een Book. 
    """
    def __init__(self, book, amount):
        self.book = book
        self.amount = amount