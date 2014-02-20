inputFile = open("../bin/prob13.input", 'r')
textString = inputFile.read()
textString = textString.split("\n")
counter=0
mySum=0
while (counter<100):
    mySum+=int(textString[counter])
    #print int(textString[counter])
    counter+=1
print mySum
