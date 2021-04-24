import json

data = {}
data['librarians'] = []
data['customers'] = []
data['books'] = []

with open('json/books.json') as f:
    data['books'] = json.load(f)

with open('json/customers.json') as f:
    data['customers'] = json.load(f)

with open('json/librarians.json') as f:
    data['librarians'] = json.load(f)

def writeJson(filePath, dataName):
    with open(filePath, 'w') as json_file:
        json.dump(dataName, json_file, indent=4)



def registerEmployee(fullName, username, password):
    data['librarians'].append({
        'name': fullName,
        'username': username,
        'password': password
    })
    writeJson('json/librarians.json', data['librarians'])


def registerCustomer(customernumber, nameSet, customergender, customerfirstname, customerlastname, customerstreetaddress, customerzipcode, customercity, customeremailaddress, customerusername, customertelephonenumber):
    data['customers'].append({
            'Number' : customernumber,
            'NameSet' : nameSet,
            'Gender' : customergender,
            'GivenName' : customerfirstname,
            'Surname' : customerlastname,
            'StreetAddress' : customerstreetaddress,
            'ZipCode' : customerzipcode,
            'City' : customercity,
            'EmailAddress' : customeremailaddress,
            'Username' : customerusername,
            'TelephoneNumber' : customertelephonenumber,
        })
    writeJson('json/customers.json', data['customers'])


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
    writeJson('json/books.json', data['books'])

def login(userInput, passInput):
    global data
    loggedIn = False
    with open('json/librarians.json') as f:
        data['librarians'] = json.load(f)
        for i in data['librarian']:
            if userInput == i['username'] and passInput == i['password']:
                loggedIn = True
            else:
                loggedIn = False
    return loggedIn