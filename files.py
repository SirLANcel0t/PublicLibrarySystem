import csv

def loadCustomers():
    with open("FakeNameSet20.csv", "r") as f:
        reader = csv.DictReader(f)
        return list(reader)