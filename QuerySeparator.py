import re
from openpyxl.compat.strings import file
from asyncore import write
from _ast import keyword
 

class QuerySeparator():
    def __init__(self):
        ROBOT_LIBRARY_SCOPE = 'GLOBAL'
        
        
    #@keyword("Get Queries From Log File")

    def GetQueriesFromLogFile(self,filePath):
        #this module takes one argument, 
        #which is the exact path of the file in your local machine 
        inFile = open(filePath,  errors='ignore')
        outFile = open(filePath+".sql", "w")
    
        strData = inFile.read()      
        buffer = re.findall("SELECT (.*)LIMIT", strData)
        for line in buffer:
            outFile.write("SELECT "+line+"LIMIT 0, 10;\n")
            #print("SELECT "+line+"LIMIT 0, 10;\n")
    
        inFile.close()
        outFile.close()
        
    #Get_Queries_From_Log_File("log_folder/NAS.log4.txt")    