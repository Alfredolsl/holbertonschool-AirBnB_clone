#!/usr/bin/python3
"""Defines the HBnB Console."""
import cmd

from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HolbertonBnB command interpreter.

    Attributes:
        prompt (str): Command prompt.
    """
    prompt = "(hbnb) "
    __classes = {"BaseModel"}

    def emptyline(self):
        """Overrides emptyline function."""
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel,
        saves it to a JSON file, and
        prints the id.
        """
        parser = arg.split()
        if len(parser) != 1:
            print("** class name missing **")
        elif parser[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(parser[0])().id)
            storage.save()

    def do_show(self, arg):
        """Print string representation of
        an instance based on the class name."""
        parser = arg.split()
        objdict = storage.all()

        if len(parser) == 0:
            print("** class name missing **")
        elif parser[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(parser) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(parser[0], parser[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(parser[0], parser[1])])

    def do_destroy(self, arg):
        """Deletes an instancae based on the
        class name and id."""
        parser = arg.split()
        objdict = storage.all()

        if len(parser) == 0:
            print("** class name missing **")
        elif parser[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(parser) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(parser[0], parser[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(parser[0], parser[1])]
            storage.save()

    def do_all(self, arg):
        objdict = storage.all()
        parser = arg.split()
        if len(parser) != 0 and parser[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            if len(arg) != 0:
                objlist = []
                for obj in objdict.values():
                    if obj.__class__.__name__ == parser[0]:
                        objlist.append(obj.__str__())
                print(objlist)
            else:
                print([obj.__str__() for obj in objdict.values()])

    def do_update(self, arg):
        """Updated an instancae based on the class name
        and id by adding or updating attribute.
        Example: Basemodel <ID> email 'email@email.com'"""
        objdict = storage.all()
        parser = arg.split()
        if len(parser) == 0:
            print("** class name missing **")
        elif parser[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(parser) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(parser[0], parser[1]) not in objdict:
            print("** no instance found **")
        elif len(parser) == 2:
            print("** attribute name missing **")
        elif len(parser) == 3:
            print("** value missing **")
        elif len(parser) == 4:
            obj = objdict["{}.{}".format(parser[0], parser[1])]
            attr = parser[2]
            value = parser[3]
            obj.__dict__[attr] = value
            storage.save()

    def do_EOF(self, arg):
        "Exit program."
        return True

    def do_quit(self, arg):
        "Exit program."
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
