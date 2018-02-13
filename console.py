#!/usr/bin/python3
""" Cmd line entry point """
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __ObjList = ['BaseModel']

    def do_create(self, args):
        'Creates and saves a new object ex. $ create MyModel'
        if args == '':
            print("** class name missing **")
            return
        objName = HBNBCommand.parseCheck_ForClass(args)
        if objName is not None:
            tmpObj = eval(objName)()
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

    def parseCheck_ForClass(args):
        'Convert a series of zero or more numbers to an argument tuple'
        tmp = None
        for obj in args.split():
            try:
                tmp = HBNBCommand.__ObjList[HBNBCommand.__ObjList.index(obj)]
            except ValueError:
                tmp = None
                pass
        return tmp



if __name__ == '__main__':
    HBNBCommand().cmdloop()