#! /usr/bin/python
'''
Script to copy chosen directories to the Google Drive folder
to use as a backup - Patrick Withams, 2015
'''
import time
import os
import shutil

# backup directory
DESTDIR = "C:\\Path\\To\\Google\\Drive\\Folder\\backup_container"

# reads the list of directories desired to be copied from text file
def readDirList():
    fileList = []
    f = open("C:\\Path\\To\\Location\\Of\\Text\\File\\foldersToBackup.txt", "r")
    for aline in f:
        aline = aline.rstrip('\n')
        splitLine = aline.split("   ")        
        fileList.append(splitLine)
    return fileList

# deletes the dest folder and its contents, then recreate items
# for each folder specified, copy all its data to the dest
def copFiles():
    dirlist = readDirList()
    shutil.rmtree(DESTDIR,  ignore_errors=False)
    # allow delete process to complete, and to avoid permissions error
    time.sleep(10)
    os.mkdir(DESTDIR)
    for dir in dirlist:	
        shutil.copytree(dir[0], DESTDIR+"\\"+dir[1])
		
def main():
    copFiles()

main()
