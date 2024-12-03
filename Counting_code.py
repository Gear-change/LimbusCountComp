def trimChar(inString: str, strTrimChar:str):
    return inString.replace(strTrimChar, "")

def trimCharFromlist(inStringList: list[str], strTrimChar:str):
    for i in range(len(inStringList)):
        inStringList[i] = inStringList[i].replace(strTrimChar,"")
    return inStringList

def trimCharlist(inStringList: list[str], strTrimChars:list[str]):
    for i in range(len(inStringList)):
        for j in range(len(strTrimChars)):
            inStringList[i] = inStringList[i].replace(strTrimChars[j],"")
    return inStringList

def trimListOfListstr(inStringList: list[list[str]], strTrimChar:str):
    for i in range(len(inStringList)):
        inStringList[i] = trimCharFromlist(inStringList[i], strTrimChar)
    return inStringList

def trimlistofListStrCharList(inStringList: list[list[str]], strTrimChar:list[str]):
    for i in range(len(inStringList)):
        inStringList[i] = trimCharlist(inStringList[i], strTrimChar)
    return inStringList

def postImport():
    global listofnames, listoflists,listoftypes
    intlist = []
    tempint = 0
    for i in range(20):
        tempint2 = 0
        #print(listoflists[i])
        for j in range(len(listoflists[i])):
            #print(listoflists[i][j])
            tempint2 += listoflists[i][j].count("1")
        print(str(tempint2))
        if (len(listoflists[i]) == 0):
            break
        intlist.append(tempint2)
        tempint += 1
    #tempint is the lists that exist
    #print(str(intlist))
    maxamount = 0
    maxLocation = -1
    for i in range(tempint-1):
        if (intlist[i] > maxamount):
            maxamount = intlist[i]
            maxLocation = i
    intlistcharsHavemax = []
    for i in range(len(listoflists[maxLocation])):
        if (listoflists[maxLocation][i].count("1") > 0):
            intlistcharsHavemax.append(i)
    f = open("output.txt", "w")
    f.write(str(listoftypes[maxLocation]) +"\n")
    templistnames = []
    templistnos = []
    for i in intlistcharsHavemax:
        templistnames.append(listofnames[i])
        templistnos.append(i+1)
    f.write(str(templistnames) + "\n")
    f.write(str(templistnos)+ "\n")
    f.close
    
f = open('Input.txt', 'r')
listofnames = []
strNames = f.readline()
listofnames =strNames.split("|")
listofnames.pop(0)
listoftypes = []
listoflists = []
listToRemove = ["|", "-", "\t", "\n"]
tempint = 0
try:
    while True:
        strTemp = f.readline()
        tempList = strTemp.split("|")
        listoftypes.append(tempList.pop(0))
        listoflists.append(tempList)
        tempint += 1
        if (tempint > 20):
            break
finally:
    trimlistofListStrCharList(listoflists, listToRemove)
    trimCharlist(listoftypes, listToRemove)
    trimCharlist(listofnames, listToRemove)
    f.close()
    #print("done with importing lists")
    #print("listoflists contains: "+ str(listoflists))
    #print("listoftypes contains: "+ str(listoftypes))
    #print(f"list of names contains {str(listofnames)}")
    postImport()
