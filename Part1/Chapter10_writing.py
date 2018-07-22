fileName="family.txt"

with open(fileName, "w") as file:#"w" to indicate write mode
    file.write("Ethan\nConnor\n")
with open(fileName, "a") as file:
    file.write("Bailey\n")

