#!/usr/bin/python3
""" Cmd line entry point """
import re
import sys
import cmd
import models
import inspect
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Cmd line interpreter for Hbnbn Proj """
    prompt = "(hbnb) "
    __ObjList = [n for n, o, in inspect.getmembers(
        sys.modules[__name__],
        inspect.isclass
    )]
    # __do_funcs = [(n, o) for n, o in .__dict__.items()]

    def do_create(self, args):
        print(__do_funcs)
        'Creates and saves a new object ex. $ create MyModel'
        if args == '':
            HBNBCommand.err_noClassName()
            return
        objName = HBNBCommand.parseCheck_ForClass(args)
        if objName is not None:
            tmpObj = eval(objName)()
            print(tmpObj.id)
            tmpObj.save()
        else:
            HBNBCommand.err_noClass()

    def do_show(self, args):
        'Fetches and displayed stored obj by id, \
        ex. $ show BaseModel 1234-1234-1234'
        # for key, val in storage._FileStorage__objects.items():
        #     print(key, " /|\ ", val)
        if args == '':
            HBNBCommand.err_noClassName()
            return
        objName = HBNBCommand.parseCheck_ForClass(args)
        if objName is not None:
            if len(args.split()) <= 1:
                HBNBCommand.err_noInstanceId()
                return
            tmpObj = HBNBCommand.parseCheck_ForId(args)
            if tmpObj is not None:
                print(tmpObj[1])
            else:
                HBNBCommand.err_noInstance()
        else:
            HBNBCommand.err_noClass()

    def do_destroy(self, args):
        'Destroys object from object storage list, \
        ex. $ destroy BaseModel 1234-1234-1234'
        if args == '':
            HBNBCommand.err_noClassName()
            return
        objName = HBNBCommand.parseCheck_ForClass(args)
        if objName is not None:
            if len(args.split()) <= 1:
                HBNBCommand.err_noInstanceId()
                return
            tmpObj = HBNBCommand.parseCheck_ForId(args)
            if tmpObj is not None:
                del storage._FileStorage__objects[tmpObj[0]]
                storage.save()
            else:
                HBNBCommand.err_noInstance()
        else:
            HBNBCommand.err_noClass()

    def do_all(self, args):
        'Prints all objects loaded in storage'
        if args == '':
            print([obj for key, obj in storage.all().items()])
            return
        # print(storage.all())
        objName = HBNBCommand.parseCheck_ForClass(args)
        print(objName)
        if objName is not None:
            print([obj for key, obj in storage.all().items()
                  if key.split('.')[0] == objName])
        else:
            HBNBCommand.err_noClass()

    def do_update(self, args):
        'Updates selected object with key value, ex. \
        $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"'
        if args == '':
            HBNBCommand.err_noClassName()
            return
        objName = HBNBCommand.parseCheck_ForClass(args)
        if objName is not None:
            if len(args.split()) <= 1:
                HBNBCommand.err_noInstanceId()
                return
            tmpObj = HBNBCommand.parseCheck_ForId(args)
            if tmpObj is not None:
                if len(args.split()) <= 2:
                    HBNBCommand.err_noAttr()
                    return
                if len(args.split()) <= 3:
                    HBNBCommand.err_noValue()
                    return
                if args.split()[2] != "id" and \
                        args.split()[2] != "created_at" and \
                        args.split()[2] != "updated_at":
                    tmpVal = HBNBCommand.validate_value(args.split()[3])
                    setattr(
                        storage._FileStorage__objects[tmpObj[0]],
                        args.split()[2],
                        tmpVal
                    )
                    storage.save()
            else:
                HBNBCommand.err_noInstance()
        else:
            HBNBCommand.err_noClass()

    # def default(self, line):
    #     print('default({})'.format(line))

    def emptyline(self):
        pass

    def do_EOF(self, args):
        'Quit command to exit the program'
        return True

    def do_quit(self, args):
        'Quit command to exit the program'
        return True

    def parseCheck_ForClass(args):
        'Looks for class name imported to check against args'
        try:
            return HBNBCommand.__ObjList[HBNBCommand.__ObjList.index(
                args.split()[0]
            )]
        except ValueError:
            return None

    def parseCheck_ForId(args):
        'checks for Id in objects in storage'
        for key, val in storage.all().items():
            if key == args.split()[0] + '.' + args.split()[1]:
                return [key, val]
        return None

    def validate_value(val):
        val = val[1:-1]
        if re.match("^\d+?\.\d+?$", val) is None:
            if val.isdigit():
                return int(val)
            else:
                return val
        else:
            return float(val)

    def err_noClass():
        print("** class doesn't exist **")

    def err_noClassName():
        print("** class name missing **")

    def err_noInstance():
        print("** no instance found **")

    def err_noValue():
        print("** value missing **")

    def err_noAttr():
        print("** attribute name missing **")

    def err_noInstanceId():
        print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
