lines=[]
path=("/Users/footballnerd12/Desktop/Python Crash Course/Python "
"Crash Course/Textbook Resources/chapter_10/pi_million_digits.txt")

with open(path) as digits:
    contents=digits.read()
    """
    for line in digits:
        lines.append(line.rst)
    #print contents.rstrip()#rstrip to remove extra '\n' from being added
    """
    lines=digits.readlines()

birthday=raw_input("what is your birthday (mmddyyyy)? ")

print birthday in contents

