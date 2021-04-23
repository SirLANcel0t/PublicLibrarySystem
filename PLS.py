"""
Public Library System! 
Analyse 3 summative assignment. Gemaakt door Mike, Luuk en Bruno uit INF1D

"""
import PLSbackend as BE

currentUser = "Librarian"

print(

"▒█▀▄▀█ ▒█░░░ ▒█▀▀█ 　 ▒█░░░ ░▀░ █▀▀▄ █▀▀█ █▀▀█ █▀▀█ █░░█ 　 █▀▀ █░░█ █▀▀ ▀▀█▀▀ █▀▀ █▀▄▀█ \n"+
"▒█▒█▒█ ▒█░░░ ▒█▀▀▄ 　 ▒█░░░ ▀█▀ █▀▀▄ █▄▄▀ █▄▄█ █▄▄▀ █▄▄█ 　 ▀▀█ █▄▄█ ▀▀█ ░░█░░ █▀▀ █░▀░█ \n"+
"▒█░░▒█ ▒█▄▄█ ▒█▄▄█ 　 ▒█▄▄█ ▀▀▀ ▀▀▀░ ▀░▀▀ ▀░░▀ ▀░▀▀ ▄▄▄█ 　 ▀▀▀ ▄▄▄█ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░░▀\n"
)


print("Welcome to MLB Public Library System \nThis interface was made by Mike, Luuk and Bruno from class INF1D")


######
# hieronder zijn allemaal functies die bepalen welk menu er getoond wordt aan de hand van 
# wie er preces ingelogd is. of als er niemand is ingelogd krijg je het meest algemene scherm te zien 
######

def MenuNoLogin(): 
    global currentUser
    possibleanswers = ["1", "2", "3", "4", "5", "9"]
    answer = ""
    while answer not in possibleanswers:
        print("Hi, anonymous user. \nWhat would you like to do? (type the number) \n 1. Login \n 2. Browse books \n 3. Exit Program \n 4. (test boekje) \n 5. (test user object) \n")

        answer = input()


        if answer == "1" :
            BE.PublicLibrary.loginUser()

        elif answer == "2": 
            BE.Catalog.BookBrowser()

        elif answer == "4":
            boekje = BE.Book("jezus", "israel", "heb ik niet", "hebreeuws", "internet hadden ze toen nog niet", 800, "de bijbel", 0)

            boekje.GetInfo()
        
        elif answer == "5":
            hans = BE.Subscriber(5,"male", "Dutch", "Hans", "de Boer", "Lange Lindelaan 14", "3011BB", "Rotterdam", "hansjepansje@gmail.com", "masterhans123", "0619283755")

            print(hans)

        elif answer == "9":
            print("OK, cya")
            break
        else:
            print("Unrecognized command")

        answer = input("Press any key to continue ...")

def MenuLibrarian():
    global currentUser
    answer = ""
    possibleanswers = ["1", "2","3","4","9"]

    while answer not in possibleanswers:
        print(" 1. Modify catalog \n 2. Create new subscriber \n 3. View loaned items \n 4. Load / make system backup \n 9. Logout ")

        answer = input()

        if answer == "1":
            print(r"¯\(°_o)/¯")
            a = input()
            MenuLibrarian()
        elif answer == "2":
            BE.Librarian.registerCustomer('1', 'Dutch', 'Male', 'Mike', 'Jansen', 'test', '1234', 'Ridderkerk', 'test@test.nl', 'test', '0612345678')
        elif answer == "3":
            print(r"¯\(°_o)/¯")
            a = input()
            MenuLibrarian()
        elif answer == "4":
            print(r"¯\(°_o)/¯")
            a = input()
            MenuLibrarian()
        elif answer == "9":
            currentUser = "nobody"
            print("Logging out...")
            a = input()
            RunProgram()

        else: 
            print("Unrecognised command!")

        answer = input("Press any key to continue ...")


# currentUser = "nobody"

def RunProgram():
    if currentUser == "nobody":
        MenuNoLogin()
    elif currentUser == "Librarian":
        print(f"Welcome, Librarian. What would you like to do?")
        MenuLibrarian()


###########################################################
# dit wordt de te runnen code, het begin van de interface #
###########################################################


RunProgram()

