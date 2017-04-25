from Core.spider import *
from Core.export import *
from Core.config import *
import csv
import os.path
debug = True
# Debug mode variable


def debugMode():
    global debug
    debug = not debug
# Toggles Debug mode


def printMenu():
    print("**********")
    print("Currently " + str(config.csv) + " is loaded in")
    print("Press * to toggle debug mode. Debug is currently " + str(debug))
    print("Press 1 to load in a csv and run tests")
    print("Press 2 to generate the SQL file")
    print("Press 3 view config")
    print("Press q to exit")
    print("**********")
# Function to print menu


def menu():
    global debug
    printMenu()
    option = input("Enter your option: ")
    if option == "q":
        return True
    elif option == "1":
        if os.path.exists('./'+config.csv):
            ifile = open(config.csv, "r", encoding='utf-8-sig')
            test = Spider(csv.reader(ifile), config.hostname, [1, 4], debug)
            # (CSV file name, hostname of site, positions of the old url and new, debug variable)
            test.crawl()
            return False
        else:
            print("File was not found, please try again")
            return False

    elif option == "2":
        print("Saving")
        Export.exportSQL()
        return False

    elif option == "3":
        print(config)

    elif option == "*":
        debugMode()
        return False
# Handles the users selections from the Menu

config = Config()
# Create our config object to store info
print(config)

while True:
    if menu():
        break
# Infinite loop keeps the menu running until the Menu Function returns True
