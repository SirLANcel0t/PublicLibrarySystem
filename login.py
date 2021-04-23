import json

data = {}
data['people'] = []

def registerEmployee(name, username, password):
    data['people'].append({
        'name': name,
        'username': username,
        'password': password
    })

    with open('login.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

def login(username, password):

    with open('login.json') as json_file:
        data = json.load(json_file)

    user = ""
    loggedIn = False

    for p in data['people']:
        if username == str(p['username']) and password == str(p['password']):
            loggedIn = True
            user = p['name']
            break
    
    return (loggedIn, user)