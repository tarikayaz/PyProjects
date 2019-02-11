from sys import argv


script,firstFile,secondFile = argv;

def print_some_text():
    print("Are you sure to copy %s over %s ? \n " %(firstFile,secondFile))
    check = input("y for yes or n for no ?")
    if( check == "y"):
        func_copy()
    elif(check == "n"):
        quit()

def func_copy():
    inputFile = open(firstFile,"r+")
    outFile = open(secondFile,"r+")

    content = inputFile.read()
    print (firstFile + " is " + str(len(content)))
    outFile.write(content)
    print("SUCCESSFULL!!")
    inputFile.close()
    outFile.close()

print_some_text()
