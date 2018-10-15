#!/usr/bin/env python3.6

from collections import OrderedDict

class TODO:
    def __init__(self):
        self.tasks = {}
    
    def add(self, argument):
        argument = argument.strip('"')
        
        if argument in self.tasks:
            print("already a task")

        key = 1
        while(True):
            if key not in self.tasks:
                self.tasks[key] = argument
                break
            key += 1

        print("#{0} {1}".format(key, argument))

    def do(self, id):
        pass

    def print_TODOs(self):
        for key, task in self.tasks.items():
            print("#{0} {1}".format(key, task)) 
        

def shell():
    print('This is a console based to-do app.')
    print('To apply a task use the argument "ADD" and then the task to add')
    print('To do a task use the argument \"DO\" and the number of the task')
    print('To see all the tasks use the argument \"Print\"')
    print('To exit the app use the argument \"quit\"')

    choice = ''
    todo = TODO()

    while(choice != 'quit'):
        choice = input("> ")
        
        argument = choice.split(' ', 1)

        operator = argument[0].lower()

        if(operator == "add"):
            todo.add(argument[1])
        elif(operator == "do"):
            todo.do(argument[1])
        elif(operator == "print"):
            todo.print_TODOs()
        elif(operator == "quit"):
            break
        else:
            print("invalid argument. Valid arguments: print, add, do or quit")

if __name__ == "__main__":
    shell()
    
    



        