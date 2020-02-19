# Assignment 2
# By Joshua Rifkin


import requests
import csv
import datetime
import logging

logging.basicConfig(filename= "errors.log",
                    level= logging.ERROR,
                    filemode= 'w')
logger = logging.getLogger('assignment2')



def downloadData(url):
    file = requests.get(url)
    csvFile = file.content.decode()

    return csvFile

def processData(data):

    personDict = {}

    file = csv.reader(data.splitlines())
    next(file)

    for line in file:
        idNum = int(line[0])
        currLine = int(idNum)

        try:
            bDay = datetime.datetime.strptime(line[2], "%d/%m/%Y")

        except ValueError:
            logger.error(("\nError processing line {} for ID #{}").format((currLine+1), idNum))
            #Added in a continue so as not to add in any individuals with invalid birthdays.
            continue

        personDict[currLine] = (line[1], bDay)

    return personDict

def displayPerson(id, personData):
    if id in personData.keys():
        print("Person #{} is {} with a birthday of {}.".format(id, personData[id][0], (personData[id][1]).strftime(
            '%Y-%m-%d')))
    else:
        print("No user found with that id.")


def main():
    try:
        source = input('File Source: ')
        csvData = downloadData(source)
    except ValueError:
        print('Invalid URL.')
        exit()

    personData = processData(csvData)

    while True:
        try:
            user = int(input("Please enter the ID of the person you are trying to look up: "))
        except ValueError:
            print("The value you entered is invalid.")
        if user > 0:
            displayPerson(user, personData)
        else:
            print("Invalid ID.")
            exit()




if __name__ == '__main__':
    main()