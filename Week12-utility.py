#Ryan Wagner
#CSCI 102
#Section B
#Week 12 - Part A

def PrintOutput(inputString):
    print("OUTPUT %s" %inputString)

def LoadFile(inputString):
    contents = []
    with open(inputString, 'r') as file:
        filecontents = file.readlines()
        for line in filecontents:
            current = line[:-1]
            contents.append(current)
    return contents
