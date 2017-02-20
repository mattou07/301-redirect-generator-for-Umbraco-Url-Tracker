from Core.spider import *
from Core.export import *
from Core.utils import *
import csv
import os.path
debug = False


def debugMode():
    global debug
    debug = not debug


def debugMenu():
    print("**********")
    print("Press 1 to toggle logging, currently "+str())
    print("Press 2 to toggle step mode, currently "+str())
    print("Press 3 to return to menu")
    print("Press q to quit")
    print("**********")


def menu():
    global debug
    print("**********")
    print('Press * to toggle debug mode. Debug is currently '+str(debug))
    print("Press 1 to load in a csv and run tests")
    print("Press 2 to generate the SQL file")
    print("Press q to exit")
    print("**********")
    option = input("Enter your option: ")
    if option == "q":
        return True
    elif option == "1":
        while True:
            file = input("Please provide the name of the file: ")

            if os.path.exists('./'+file):
                break
            else:
                print("File was not found, please try again")
        ifile = open(file, "r", encoding='utf-8-sig')
        test = Spider(csv.reader(ifile), "", [0, 2])
        test.crawl()
        return False
    elif option == "2":
        generate()
        return False

    elif option == "*":
        debugMode()
        return False


def generate():
    print("Saving")
    Export.exportSQL()

while True:
    if menu():
        break
