#!/usr/bin/env python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Subclass of Cmd"""
    def __init__(self):
        cmd.Cmd.__init__(self)
        """custom hbnb prompt"""
        self.prompt = '(hbnb) '

    """send exit signal"""
    def do_quit(self, arg):
        sys.exit(1)

    """define quit"""
    def help_quit(self):
        print('Quit command to exit the program\n')

    """return EOF signal"""
    def do_EOF(self, line):
        return True

    """define EOF"""
    def help_EOF(self):
        print('Indicate end of input\n')

    """disable repetition of last command"""
    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
