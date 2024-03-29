#Ryan Wagner
#CSCI 102
#Section B
#Week 12 - Part A

def PrintOutput(inputString):
    print("OUTPUT %s" %inputString)
############################################################################
def LoadFile(inputString):
    contents = []
    with open(inputString, 'r') as file:
        filecontents = file.readlines()
        for line in filecontents:
            current = line[:-1]
            contents.append(current)
    return contents
############################################################################
def UpdateString(word, insert, index):
    firstHalf = word[:index]
    secondHalf = word[index+1:]
    PrintOutput(firstHalf+insert+secondHalf)
############################################################################
def FindWordCount(wordList,wordSearch):
    count = 0
    for i in range(0,len(wordList)):
        count = count + wordList[i].count(wordSearch)
    return count
############################################################################
def ScoreFinder(playersList,scoreList,name):
    index = 0;
    for i in range(0,len(playersList)):
        if playersList[i].lower() == name.lower():
            score = scoreList[i]
            print("OUTPUT %s got a score of %d" %(playersList[i],score))
            return
    print("OUTPUT player not found")
############################################################################
def Union(list1,list2):
    return list1+list2
############################################################################
def Intersection(list1,list2):
    intersections = []
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if (list2[j] == list1[i]):
                intersections.append(list2[j])
    return intersections
############################################################################
def NotIn(list1,list2):
    notin = []
    for i in range(0,len(list1)):
        if list1[i] not in list2:
            notin.append(list1[i])
    return notin
            
