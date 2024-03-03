#!/usr/bin/python3
"""Defines the HBnB Console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HolbertonBnB command interpreter.

    Attributes:
        prompt (str): Command prompt.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Overrides emptyline function."""
        pass

    def do_EOF(self, arg):
        "Exit program."
        return True

    def do_quit(self, arg):
        "Exit program."
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
