#!/usr/bin/python3
"""module about a cmd"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class of cmd"""

    prompt = "(hbnb)"


    def quit(self, command):
        """method to quit from cmd"""
        exit()

    def EOF(self, command):
        """method to quit the program"""
        print()
        exit()

    def emptyline(self):
        """method about behaviour when press enter"""
        pass

    def help_quit(self):
        """method to implement help"""
        print("command to exit program")

    def help_EOF(self):
        """method to implement help"""
        print("command to exit program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()