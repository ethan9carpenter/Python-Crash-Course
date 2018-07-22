from Glossary import printDictionary
"""
Because I'm using Python 2.7, I cannot use input(), 
I have to use raw_input instead.
"""

name=""

while name == "":
    name=raw_input("What is your name? ")
print str(name)

numbers={}

for i in range(1, 11):
    numbers[i]=i**2
printDictionary(numbers)
