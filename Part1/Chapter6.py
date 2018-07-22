from Glossary import printDictionary

family={
    "Ethan": {"Sport":"Cross Country", "Initials": "ETC"},
        "Connor": {"Sport":"Lacross", "Initials": "CPC"},
        "Mom": {"Sport":"Basketball", "Initials": "ARC"},
        "Dad": {"Sport":"Baseball", "Initials": "DRC"}
        }

for item in family:
    print item+" "
    printDictionary(family[item])
    print "\n"
