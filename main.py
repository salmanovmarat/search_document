import inquirer
from function import *

while True:
    questions = [
    inquirer.List('question',
                    message="What would you like to do?",
                    choices=['Search for documents', 'Read documents', 'Quit proqram'],
                ),
    ]
    answers = inquirer.prompt(questions)


    if answers['question'] == 'Search for documents':
        word = input("Enter search words: ")
        search_document(word)
        continue
    if answers["question"] == "Read documents":
        number = int(input("Enter document number: "))
        read_document(number)
        continue
    else:
        exit()