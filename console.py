#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter"""

    prompt = "(hbnb) "

    classes = {"BaseModel":BaseModel}

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass



    def do_quit(self, arg):
        """Quit command to exit the program."""
        exit()

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        exit()

    def do_create(self, arg):
        """Create a new class instance and print its id"""
        arglist = parse(arg)
        if len(arglist) == 0:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_obj = HBNBCommand.classes[arglist[0]]()
            storage.new(new_obj)
            storage.save()

    
    def do_show(self, arg):
        """Display the string representation of a class instance of a given id"""
        arglist = parse(arg)
        objdict = storage.all()
        if len(arglist) == 0:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif f"{arglist[0]}.{arglist[1]}" not in objdict.keys():
            print("** no instance found **")
        else:
            print(objdict[f"{arglist[0]}.{arglist[1]}"])

    
    def do_destroy(self, arg):
        """Delete a class instance of a given id"""
        arglist = parse(arg)
        objdict = storage.all()
        if len(arglist) == 0:
            print("** class name missing **")
        elif arglist[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arglist) == 1:
            print("** instance id missing **")
        elif f"{arglist[0]}.{arglist[1]}" not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict[f"{arglist[0]}.{arglist[1]}"]
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()