#!/usr/bin/env python3.6

import json

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

        self.write_to_file()

        print("#{0} {1}".format(key, argument))

    
    def do(self, key):
        print(key)

        key = key.strip('#')
        print(self.tasks)
        print(key)

        if key not in self.tasks:
            print("there is no such task")

        task = self.tasks.pop(key)

        self.write_to_file()

        print("completed #{0} {1}".format(key, task))

    
    def print_TODOs(self):
        if(len(self.tasks) == 0):
            print("there are no tasks")

        with open('backup.txt', 'r') as f:
            read_data = f.read() 
        f.close()    
        
        dictionary = json.loads(read_data)

        for key, task in dictionary.items():
            print("#{0} {1}".format(key, task))


    def write_to_file(self):
        json_object = json.dumps(self.tasks)

        with open('backup.txt', 'w') as f:
            f.write(json_object)
        f.close()
        

def shell():
    print('This is a console based to-do app.')
    print('To apply a task use the argument "ADD" and then the task to add')
    print('To do a task use the argument \"DO\" and the number of the task')
    print('To see all the tasks use the argument \"Print\"')
    print('To exit the app use the argument \"quit\"')

    choice = ''
    todo = TODO()

    with open('backup.txt', 'r') as f:
        read_data = f.read() 
    f.close()    
        
    dictionary = json.loads(read_data)

    todo.tasks = dictionary

    while(choice != 'quit'):
        choice = input("> ")
        
        argument = choice.split(' ', 1)

        operator = argument[0].lower()
        #print(argument[1])

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
    
    



        