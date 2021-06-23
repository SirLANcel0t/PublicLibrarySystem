import os
import json

abs_path = os.path.dirname(__file__)

data = {}
data['librarians'] = []
data['customers'] = []
data['books'] = []
data['loanItems'] = []
data['publishingcompany'] = []

with open(abs_path + '/json/books.json') as f:
    data['books'] = json.load(f) 

with open(abs_path + '/json/customers.json') as f:
    data['customers'] = json.load(f)

with open(abs_path + '/json/librarians.json') as f:
    data['librarians'] = json.load(f)

with open(abs_path + '/json/loanItems.json') as f:
    data['loanItems'] = json.load(f)

with open(abs_path + '/json/publishingcompany.json') as f:
    data['publishingcompany'] = json.load(f)