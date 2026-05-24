# AirBnB Clone

## Project Description

This is the first phase of the AirBnB Clone project. A command-line
interpreter is built to manage AirBnB objects: Users, Places, States,
Cities, Amenities, and Reviews. Data is persisted to a JSON file.

## The Command Interpreter

### How to Start

**Interactive mode:**
```
$ ./console.py
(hbnb)
```

**Non-interactive mode:**
```
$ echo "help" | ./console.py
```

### How to Use

| Command | Usage | Description |
|---------|-------|-------------|
| `create` | `create <class>` | Creates an instance, saves it, prints id |
| `show` | `show <class> <id>` | Prints string representation of instance |
| `destroy` | `destroy <class> <id>` | Deletes an instance |
| `all` | `all [class]` | Prints all string representations |
| `update` | `update <class> <id> <attr> <value>` | Updates an attribute |
| `quit` | `quit` | Exits the console |
| `EOF` | `EOF` | Exits the console |

**Available Classes:** BaseModel, User, State, City, Amenity, Place, Review

### Examples

```
$ ./console.py
(hbnb) create User
0b58878f-fa14-4b16-b2f2-fb92f3d1b4f5
(hbnb) show User 0b58878f-fa14-4b16-b2f2-fb92f3d1b4f5
[User] (0b58878f-...) {'id': '0b58878f-...', 'created_at': ..., 'updated_at': ...}
(hbnb) all
["[User] (0b58878f-...) {...}"]
(hbnb) update User 0b58878f-fa14-4b16-b2f2-fb92f3d1b4f5 email "test@example.com"
(hbnb) destroy User 0b58878f-fa14-4b16-b2f2-fb92f3d1b4f5
(hbnb) quit
$
```

```
$ echo "all BaseModel" | ./console.py
(hbnb) []
(hbnb)
$
```

## Authors

See [AUTHORS](AUTHORS).
