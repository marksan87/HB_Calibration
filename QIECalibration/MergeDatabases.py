# Merge a list of databases into one database
# Returns name of merged database
# Zach Eckert
# 6/25/2018

import sqlite3
from shutil import copyfile
import sys

def MergeDatabases(files,dirName="",outName="mergedDatabase.db"):
    if not files:
        print "No database files found in SummaryPlot."
        sys.exit()
    copyfile(files[0],"".join([dirName,outName]))
    #copyfile(files[0],outName)
    outDatabase = sqlite3.connect("".join([dirName,outName]))
    outCursor = outDatabase.cursor()
    for i,f in enumerate(files[1:]):
        print f
        outCursor.execute("""ATTACH "%s" AS db%i"""%(f,i))
        outCursor.execute("""INSERT INTO qieshuntparams SELECT * FROM db%i.qieshuntparams"""%i)


    outCursor.close()
    outDatabase.commit()
    


