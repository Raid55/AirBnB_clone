#!/usr/bin/python3
""" Cmd line entry point """
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __ObjList = ['BaseModel']

    def do_create(self, args):
        'Creates and saves a new object ex. $ create MyModel'
        objname = None
        if args == '':
            print("** class name missing **")
            return
        for obj in args.split():
            try:
                inst = HBNBCommand.__ObjList[HBNBCommand.__ObjList.index(obj)]
            except ValueError:
                inst = None
                pass
        if inst is not None:
            tmpObj = eval(inst)()
            print(tmpObj.id)
            tmpObj.save()
        else:
            print("** class doesn't exist **")


    def do_EOF(self, args):
        'Quit command to exit the program'
        return True
    def do_quit(self, args):
        'Quit command to exit the program'
        return True

    def parse(arg):
        'Convert a series of zero or more numbers to an argument tuple'
        return tuple(map(int, arg.split()))



if __name__ == '__main__':
    HBNBCommand().cmdloop()