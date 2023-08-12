#!/usr/bin/env python3
"""
contains the entry point of the command interpreter
"""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = '(hbnb)'
    class_list = ["BaseModel"]

    @staticmethod
    def error_message(caller, arg):
        list_message = ["** class name missing **",
                        "** class doesn't exist **",
                        "** instance id missing **",
                        "** no instance found **"]
        if not arg:
            print(list_message[0])
        elif caller == 'show' and arg.split()[0] not in HBNBCommand.class_list:
            print(list_message[1])
        elif caller == 'create' and arg not in HBNBCommand.class_list:
            print(list_message[1])
        elif caller == "show" and len(arg.split()) < 2:
            print(list_message[2])
        elif caller == "destroy" and len(arg.split()) < 2:
            print(list_message[2])
        else:
            return 0

        
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it"""
        if HBNBCommand.error_message("create", arg) == None:
            return
        else:
            base = BaseModel()
            base.save()
            base_id = base.id
            print(base_id)

    def do_show(self, arg):
        """string representation of an instance based on the class name / id"""
        objects = {}
        args = arg.split()
        if HBNBCommand.error_message("show", arg) == None:
            return
        else:
            objects = FileStorage().all()
            key = f"{args[0]}.{args[1]}"
            if (key not in tuple(objects.keys())):
                print("** no instance found **")
            else:
                print(objects.get(key))

    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")

    def emptyline(self):
        """empty file should execute nothing"""
        pass

    def do_EOF(self, line):
        """when you ctrl + D you are able to exit the file"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def postloop(self):
        """print a new line after you exit the program"""
        print()


if __name__ == "__main__":
    my_cmd = HBNBCommand()
    my_cmd.cmdloop()
