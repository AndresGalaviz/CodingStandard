import re
import sys
import subprocess
from tools import *
# TheLongAndWindingRoad2.cpp
fileName = input("Please enter filename: ")

print(fileName)
if bool(re.search(r'^([A-Z][a-z]*[0-9]*)+\.cpp$', fileName)):
    print('Filename is okay')
else:
    print('Filename is incorrect')




with open(fileName) as file:
    bashCommand = "g++ " + fileName

    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = process.communicate()[1]
    
    if ("error" in str(output)):
        print("Code does not compile")
        print(output)
        sys.exit()
        
    lineNumber = 0;
    for line in file:
        tokens = line.split()
        lineNumber += 1
        if(len(tokens) == 0):
            continue
        print("Line number " + str(lineNumber), end = ": \n")
        
        i = 0
        print(tokens)
        if(tokens[i] in reservedWords):
            if(tokens[i] == 'const'):
                i += 1
            
            if(tokens[i] in variableDefinitions):
                variableRegex = re.escape(tokens[i][0]) + r"([A-Z][a-z]*[0-9]*)+$"
                lineIsCorrect = False
                if(bool(re.search(variableRegex, tokens[i + 1]))):
                    lineIsCorrect = True
                    wordsPerLine = re.findall(r'[A-Z][a-z]*', tokens[i + 1])
                    for word in wordsPerLine:
                        if(word.lower() in reservedWords):
                            print("\tReserved word detected in variable name: " + word)
                            lineIsCorrect = False
                
                if(lineIsCorrect):
                    print('\t' + tokens[i] + " variable: \'" + tokens[1] + "\' is correct")
                else:
                    print('\t' + tokens[i] + "  variable: \'" + tokens[1] + "\' is incorrect")
        
