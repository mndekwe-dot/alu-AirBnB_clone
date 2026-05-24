#!/usr/bin/python3
"""Console module — entry point of the AirBnB clone command interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


CLASSES = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


def parse(line):
    """Split line into tokens, respecting quoted strings."""
    try:
        return shlex.split(line)
    except ValueError:
        return line.split()


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Usage: create <class>
Creates a new instance, saves it, and prints the id."""
        args = parse(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        obj = CLASSES[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Usage: show <class> <id>
Prints the string representation of an instance."""
        args = parse(arg)
        objs = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objs:
            print("** no instance found **")
        else:
            print(objs["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>
Deletes an instance based on the class name and id."""
        args = parse(arg)
        objs = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objs:
            print("** no instance found **")
        else:
            del objs["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all [class]
Prints all string representations of all instances."""
        args = parse(arg)
        if args and args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        objs = storage.all()
        result = []
        for key, obj in objs.items():
            if not args or key.startswith(args[0] + "."):
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
Updates an instance based on the class name and id."""
        args = parse(arg)
        objs = storage.all()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objs[key]
        attr_name = args[2]
        attr_value = args[3]
        try:
            attr_value = int(attr_value)
        except ValueError:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
