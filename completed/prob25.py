def FlipString(tempString):
    returnString = ""
    i = len(tempString)-1
    while i >= 0:
        returnString += tempString[i]
        i -= 1
    return returnString

def AddFibStrings(prevTerm, currTerm):
    #I'm sorry this ended up so complicated
    tempString = ""
    returnString = ""
    i = len(currTerm)-1
    carryOne = 0
    while i >= 0:
        #If the strings are of uneven lengths
        if len(currTerm) > len(prevTerm):
            #For the uneven digit
            if (i == 0):
                nextInt = int(currTerm[i]) + carryOne
            #i-1 to balance out the string length disparity
            else:
                nextInt = int(currTerm[i]) + int(prevTerm[i-1]) + carryOne
        else:
            nextInt = int(currTerm[i]) + int(prevTerm[i]) + carryOne

        lenInt = len(str(nextInt))
        if (lenInt > 1):
            carryOne = 1
        else:
            carryOne = 0
            
        tempString += str(nextInt)[lenInt-1]
        
        if i == 0 and carryOne == 1:
            tempString += "1"
        i -= 1
    return FlipString(tempString)

def Main():
    count = 2
    prevTerm = "1"
    currTerm = "1"
    while (len(currTerm) < 1000):
        tempTerm = AddFibStrings(prevTerm, currTerm)
        prevTerm = currTerm
        currTerm = tempTerm
        count += 1
        print "Count: "+str(count)

Main()
