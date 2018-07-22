name=""
def printName(name, greeting=""):
    """This is a docstring"""
    if greeting:
        print greeting+" "+name.title()
    else:
        print name.title()
def printNames(*names):#Builds a tuple from arbitrary number or arguments
    for name in names:
        print name
def printInfo(name, **info):#info is a dictionary of arbitrary info
    print name
    for key, item in info.items():
        print key+" "+str(item)


printName("ethan", "hello")
printName(greeting="hi", name="connor")
printName("ethan")
print ""
printNames("Ethan", "Connor", "Bailey")
printInfo("Ethan", sport="XC/TF", grade=12, birthMonth="February")
