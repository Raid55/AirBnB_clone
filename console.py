#!/usr/bin/python3
""" Cmd line entry point """
import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_show(self, args):
        'Fetches and displayed stored obj by id, ex. $ show BaseModel 1234-1234-1234'
        if args == '':
            print("** class name missing **")
            return
        objName = HBNBCommand.parseCheck_ForClass(args)
        if objName is not None:
            if len(args.split()) <= 1:
                print("** instance id missing **")
                return
            print(HBNBCommand.parseCheck_ForId(args))


        else:
            print("** class doesn't exist **")

    def do_EOF(self, args):
        'Quit command to exit the program'
        return True
    def do_quit(self, args):
        'Quit command to exit the program'
        return True

    def parseCheck_ForClass(args):
        'Looks for class name imported to check against args'
        tmp = None
        try:
            tmp = HBNBCommand.__ObjList[HBNBCommand.__ObjList.index(args.split()[0])]
        except ValueError:
            tmp = None
            pass
        return tmp
    def parseCheck_ForId(args):
        'checks for Id in objects in storage'
        for key, val in storage.all().items():
            if key == args.split()[0] + '.' +args.split()[1]:
                return val
        return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()