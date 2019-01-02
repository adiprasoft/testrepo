import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
parent = os.getcwd()

# print(parent)
# def path(spath):
#     dirs = os.listdir(spath)
#     allfiles = list()
#     for dir in dirs:
#         newpath = os.path.join(spath, dir)
#         if os.path.isdir(newpath):
#                 path(newpath)
#         else:
#             allfiles.append(newpath)
#             #print(os.path.join(spath, dir))
#     return allfiles
# all_list = path(parent)

# for items in all_list:
#     print(items)


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)             
    return allFiles

flist = getListOfFiles(parent)

for items in flist:
    print(items)