try:
    first=int(input("Enter a number: ").strip())
    second=int(input("Enter another number: ").strip())
    print ("Sum: "+str(first+second)+"\n")
except ValueError:
    print ("You must enter numbers for them to be added.\n")

def textInfo(filePath):
    try:
        with open(filePath) as alice:
            words=alice.read().split()
    except IOError:
        pass
    else:
        wordSet=set(words)
        print ("Number of words: "+str(len(words)))
        print ("Number of unique words: "+str(len(wordSet)))
        word=input("Enter a word: ")
        if word in wordSet:
            print ("The word is in the text as entered")
        else:
            print ("the word is not in the text as entered")
   
    
textInfo("family.txt")

