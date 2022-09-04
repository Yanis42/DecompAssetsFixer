from os import walk

try:
    from data import dataToFix, entrDictSpecial
except:
    print("ERROR: ``data.py`` not found! Make sure everything is in the same folder.")
    quit()

# -------------------------------------------------------

### [GENERAL FUNCTIONS] ###

def getFiles(path:str, fileType:str):
    '''Returns a list of data paths with the specified extension'''
    filesList = []
    for path, dirs, files in walk(path):
        for file in files:
            if file.endswith(fileType):
                filesList.append(f"{path}/{file}")
    filesList.sort()
    return filesList

def getFilesFromDict(dataDict:dict, files:list):
    '''Filters the list returned by ``getFiles`` to keep relevant data'''
    filesList = []
    for file in files:
        with open(file, 'r') as curFile:
            for key in dataDict.keys():
                for line in curFile.readlines():
                    if line.find(key) != -1:
                        filesList.append(curFile.name)
    filesList.sort()
    return filesList

# -------------------------------------------------------

### [FIX TYPES MODE] ###

def replaceOldData(path:str, extension:str):
    '''Replaces older names by newer ones'''
    for data in dataToFix:
        files = getFilesFromDict(data, getFiles(path, extension))
        for file in files:
            with open(file, 'r') as curFile:
                fileData = curFile.read()
            for key in data.keys():
                fileData = fileData.replace(f"{key} ", f"{data[key]} ")
            with open(file, 'w') as curFile:
                curFile.write(fileData)

# -------------------------------------------------------

### [NAME ENTRANCES] ###

def getEntranceDict(path:str):
    """Returns a list containing every entrances"""
    entranceList = []

    # read the entrance table
    try:
        with open(f"{path}/include/tables/entrance_table.h", 'r') as fileData:
            # keep the relevant data
            for line in fileData.readlines():
                if line.startswith("/* 0x"):
                    startIndex = line.find("ENTR_")
                    entranceList.append(line[startIndex : line.find(",", startIndex)])
    except FileNotFoundError:
        raise print("ERROR: Can't find scene_table.h!")

    # return a dictionnary from the entrance list
    return ({f"0x{i:04X}": entrance for i, entrance in enumerate(entranceList)} | entrDictSpecial)

def getArrayInfos(data:list, arrayName:str):
    '''Returns arrays containing line numbers for the start and the end of relevant C data'''
    arrayStartIndices = []
    arrayEndIndices = []
    hasListStarted = False

    for lineNb, line in enumerate(data):
        if line.find(arrayName) != -1 and line.endswith("] = {\n"):
            arrayStartIndices.append(lineNb + 1)
            hasListStarted = True

        if hasListStarted and line.startswith("};\n"):
            arrayEndIndices.append(lineNb)
            hasListStarted = False
    try:
        if len(arrayStartIndices) != len(arrayEndIndices):
            raise IndexError
    except IndexError:
        print("ERROR: Start Length != End Length")

    return arrayStartIndices, arrayEndIndices

def getNewFileData(data:list, dataDict:dict, arrayName:str):
    '''Returns the current data with the updated values'''
    startList, endList = getArrayInfos(data, arrayName)
    if len(startList) == len(endList):
        for curStart, curEnd in zip(startList, endList):
            for i in range(curEnd - curStart):
                curLine = curStart + i
                try:
                    data[curLine] = f"    {dataDict[data[curLine][:-2].lstrip()]},\n"
                except KeyError:
                    # why???
                    pass
    return data

def replaceEntranceHex(decompRoot:str):
    '''Updates the entrances from OoT scenes'''
    entrDict = getEntranceDict(decompRoot)
    scenePaths = getFiles(f"{decompRoot}/assets/scenes/", ".c")

    for path in scenePaths:
        data = []
        sceneName = None
        with open(path, 'r') as file:
            if file.name.find("room") == -1:
                data = file.readlines()
                sceneName = file.name.split('/')[6][:-2]
        if sceneName is not None:
            newData = getNewFileData(data, entrDict, f"{sceneName}ExitList")
            with open(path, 'w') as file:
                for line in newData:
                    file.write(line)
