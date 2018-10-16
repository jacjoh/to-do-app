#!/usr/bin/env python3.6

import json

class TODO:
    def __init__(self):
        self.tasks = {}
    
    def add(self, new_task):
        new_task = new_task.strip('"')
        
        if len(new_task) == 0:
            print("need a task to add")
            return

        key = 1
        while(True):
            if str(key) not in self.tasks:
                self.tasks[str(key)] = new_task
                break
            key += 1

        self.write_to_file()

        print("#{0} {1}".format(key, new_task))

    
    def do(self, key):
        key = key.strip('# ')
        
        if key not in self.tasks:
            print("there is no such task")
            return

        task = self.tasks.pop(key)

        self.write_to_file()

        print("completed #{0} {1}".format(key, task))

    
    def print_TODOs(self):
        if(len(self.tasks) == 0):
            print("there are no tasks")
            return
        
        with open('backup.txt', 'r') as f:
            read_data = f.read()     
        
        self.tasks = json.loads(read_data)

        for key, task in self.tasks.items():
            print("#{0} {1}".format(key, task))


    def write_to_file(self):
        json_object = json.dumps(self.tasks)

        with open('backup.txt', 'w') as f:
            f.write(json_object)

def shell():
    print('This is a console based to-do app.')
    print('To apply a task use the argument "add" and then the task to add')
    print('To do a task use the argument "do" and the number of the task')
    print('To see all the tasks use the argument "print"')
    print('To exit the app use the argument "quit"')

    choice = ''
    todo = TODO()

    file_path = 'backup.txt'
    
    try:
        with open(file_path, 'r') as f:
            read_data = f.read()
        if len(read_data) != 0:
            todo.tasks = json.loads(read_data)
    except IOError:
        fp = open(file_path, 'w+')           


    while(choice != 'quit'):
        choice = input("> ")
        
        argument = choice.split(' ', 1)

        operator = argument[0].lower()

        if(operator == "add"):
            if len(argument) == 1:
                print("need a task to add")
            else:
                todo.add(argument[1])

        elif(operator == "do"):
            if len(argument) == 1:
                 print("need a tasknumber to do")
            else:
                todo.do(argument[1])
        
        elif(operator == "print"):
            todo.print_TODOs()
        
        elif(operator == "quit"):
            break
        
        else:
            print('invalid argument. Valid arguments: print, add "task", do #tasknumber or quit')

if __name__ == "__main__":
    shell()
    
    



        