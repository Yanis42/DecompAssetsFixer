from os import walk

try:
    from data import dataToFix, decompPath
except:
    print("ERROR: ``data.py`` not found! Make sure everything is in the same folder.")
    quit()

def getFiles(path:str, fileType:str):
    '''Returns a list of the filenames with the specified extension'''
    filesList = []
    for path, dirs, files in walk(path):
        for file in files:
            if file.endswith(fileType):
                filesList.append(f"{path}/{file}")
    filesList.sort()
    return filesList

def getFilesFromDict(dataDict:dict, files:list):
    '''Returns a list of files which contains the specified data'''
    filesList = []
    for file in files:
        with open(file, 'r') as curFile:
            for key in dataDict.keys():
                for line in curFile.readlines():
                    if line.find(key) != -1:
                        filesList.append(curFile.name)
    filesList.sort()
    return filesList

def replaceOldData(path:str, extension:str):
    '''Returns list of the new files to write'''
    for data in dataToFix:
        files = getFilesFromDict(data, getFiles(path, extension))
        for file in files:
            with open(file, 'r') as curFile:
                fileData = curFile.read()
            for key in data.keys():
                fileData = fileData.replace(f"{key} ", f"{data[key]} ")
            with open(file, 'w') as curFile:
                curFile.write(fileData)

replaceOldData(decompPath, ".h")
replaceOldData(decompPath, ".c")
