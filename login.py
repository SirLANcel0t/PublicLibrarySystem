import json

#data = {}
#data['people'] = []
#data['people'].append({
#    'name': 'Scott',
#    'website': 'stackabuse.com',
#    'from': 'Nebraska'
#})
#data['people'].append({
#    'name': 'Larry',
#    'website': 'google.com',
#    'from': 'Michigan'
#})
#data['people'].append({
#    'name': 'Tim',
#    'website': 'apple.com',
#    'from': 'Alabama'
#})

#with open('login.json', 'w') as outfile:
#    json.dump(data, outfile, indent=4)


with open('login.json') as json_file:
    data = json.load(json_file)

usernameInput = input("Please enter username > \n")
passwordInput = input("Please enter password > \n")
user = ""
loggedIn = False

for p in data['people']:
    if usernameInput == str(p['username']) and passwordInput == str(p['password']):
        loggedIn = True
        user = p['name']
        break

if loggedIn == True:
    print(f"Welcome {user}, you are now logged in!")
else:
    print("Username or password incorrect")