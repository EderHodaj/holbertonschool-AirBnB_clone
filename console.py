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
            print(new_obj.id)
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

    def do_all(self, arg):
        """Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        arglist = parse(arg)
        if len(arglist) > 0 and arglist[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objlist = []
            for obj in storage.all().values():
                if len(arglist) > 0 and arglist[0] == obj.__class__.__name__:
                    objlist.append(obj.__str__())
                elif len(arglist) == 0:
                    objlist.append(obj.__str__())
            print(objlist)

    def do_update(self, arg):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        arglist = parse(arg)
        objdict = storage.all()

        if len(arglist) == 0:
            print("** class name missing **")
            return False
        if arglist[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(arglist) == 1:
            print("** instance id missing **")
            return False
        if f"{arglist[0]}.{arglist[1]}" not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arglist) == 2:
            print("** attribute name missing **")
            return False
        if len(arglist) == 3:
            try:
                type(eval(arglist[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arglist) == 4:
            obj = objdict[f"{arglist[0]}.{arglist[1]}"]
            if arglist[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arglist[2]])
                obj.__dict__[arglist[2]] = valtype(arglist[3])
            else:
                obj.__dict__[arglist[2]] = arglist[3]
        elif type(eval(arglist[2])) == dict:
            obj = objdict[f"{arglist[0]}.{arglist[1]}"]
            for k, v in eval(arglist[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()