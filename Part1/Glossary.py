def printDictionary(dictionary):
    for key, definition in dictionary.items():
        print str(key)+": "+str(definition)
objects={
    "List": "Effectively a List from Java that is defined with square braces [ ] and a comma separates each element",
    "Tuple": "A List that cannot be edited, it is defined with parentheses ( ) instead",
    "Dictionary": "A HashMap-like Object that stores key:element pairs separated by a colon"+
        " with a comma separating pairs.  It is defined ith curly braces { }."
    }
keywords={
    "elif": "Else-if shortened into 'elif'",
    "break": "Break out of a loop",
    "continue": "Skips the remaining code in a loop and goes back to "+
        "the beginning of the loop.",
    "*<parameter name>": "Builds a tuple argument of arbitray size",
    "**<parameter name>": "Builds a dictionary argument of arbitray size",
    "pass": "Skips a block, in if-elif-else, try-catch-else, etc.",
    "None": "Equivalent to null"
    }
importSyntax={
    "import <file name (without extension)>": "Imports the entire module",
    "from <file name> import <method 1>, <method 2>, etc.":  "Imports specific functions",
    "from <file name> import <method 1> as <new name>":  "Imports a specific function, renamed as <new name>",
    "import <module name> as <new name>": "Imports a specific module, renamed as <new name>",
    "from <module name> import *":  "Import everything in a given module",
    "__": "Makes a variable or method private, not often used by convention as responsibility is"+
        "emphasized rather than public/private/protected",
    "_": "Convention used to indicate method or variable that should be treated as private"
    }
functions={
    ".append(object)": "Adds an item to the end of a list.",
    ".insert(index, object)": "Inserts an item at a specified index.",
    "set(List)": "Wraps a List and removes duplicates.",
    ".remove(object)": "Removes a specified element from a List.",
    "str(object)": "Cast that is similar to toString() in Java.",
    "len(List)": "Returns the length of a List.",
    "raw_input(prompt)": "Returns the users input as a String",
    "int(String)": "Casts a String to an int"
    }
fileSyntax={
    "open(fileName, '<indicator>')": "Opens a file in read mode 'r', write mode 'w',"+
    "append mode 'a', read and write mode 'r+', and no indicator argument for read-only."
    }
listSyntax={
    "[n]": "Object at index n.",
    "[-n]": "Retrieves item when indexing from the back of the list starting at -1.\n"+
        "-1 returns last element, -2 returns second-to-last, etc.",
    "[:n]": "Returns a sublist up to but not including element n.",
    "[n:]": "Returns a sublist containing elements n through the end of the list.",
    "[a:b]": "Returns a sublist containing elements from a up to, but not including, b.",
    "<list name>": "Returns true if the list is not empty, false if it is empty.",
    "[:]":  "Returns a clone of the list"
    }
jsonFunctions={
    ".dump(<data>, <filePath>)": "Stores the data to the file path."
    }