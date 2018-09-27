from random import randint
user_input, file, count, extension, add, remove, removeAll, search, print_Amount, searches = "", "", "", "", "", "", "", "", "", ""
delim = " "
addLim = "A"
removeLim = "RO"
printLim = "P"
removeAllLim = "RA"
searchLim = "S"
quitLim = 'Q'
check = False

print("Welcome to the test generator!\n" )
while not isinstance(user_input, int):
    user_input = (input("Please enter the sample size you would like: "))
    try:
        user_input = int(user_input)
    except ValueError:
        print("Not a integer!")

while not isinstance(remove, int):
    remove = (input("Please enter the number of removals you would like: "))
    try:
        remove = int(remove)
    except ValueError:
        print("Not a integer!")

while not isinstance(searches, int):
    searches = (input("Please enter the number of searches you would like: "))
    try:
        searches = int(searches)
    except ValueError:
        print("Not a integer!")
removeAll = input("Would you like a remove all(Y/N): ")
if removeAll.lower() == "y":
    removeInt = int(input("Enter your digit: "))
print_Amount = input("Would you like a print(Y/N): ")
extension = input("Please enter an extension for the test: ")
extension = "Test" + extension +".txt"
file = open(extension, 'x')
count = 0
while count < user_input:
    data = randint(1, user_input)
    file.write("{}{}{}\n".format(addLim, delim, data))
    count = count + 1
count = 0
while count < remove:
    data = randint(1, user_input)
    file.write("{}{}{}\n".format(removeLim, delim, data))
    count = count + 1
count = 0
while count < searches:
    data = randint(1, user_input)
    file.write("{}{}{}\n".format(searchLim, delim, data))
    count = count + 1
if print_Amount.lower() == "y":
    file.write("{}\n".format(printLim))
if removeAll == "y" or removeAll == "Y":
    file.write("{}{}{}\n".format(removeAllLim, delim, removeInt))
file.write("Q\n")
file.close()


