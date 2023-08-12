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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            base = BaseModel()
            base.save()
            base_id = base.id
            print(base_id)

    def do_show(self, line):
        """string representation of an instance based on the class name / id"""
        args = line.split()
        objects = {}
        found_object = {}
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = FileStorage().all()
            key = f"{args[0]}.{args[1]}"
            if (key not in tuple(objects.keys())):
                print("** no instance found **")
            else:
                print(objects.get(key))

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
    if len(sys.argv) > 1:
        # Read commands from stdin
        commands = sys.stdin.readlines()
        my_cmd = HBNBCommand(stdin=commands)
        my_cmd.cmdloop()
    else:
        # Interactive mode
        my_cmd = HBNBCommand()
        my_cmd.cmdloop()
