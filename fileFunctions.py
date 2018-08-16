def filefunctionsinpython(mode):
    print("Use f.readline() to read line by line"+
          "\n use f.readline().rstrip() trailing new line characters"
          +"\n you can read all lines at once using f.readlines() this will return a"+
          "comma seperated list of lines"
          )
    if(mode=="r"):
        f = open("sampleDoc.txt","r")
        quote=f.read()
        f.close()
        return quote
    elif(mode=="u"):
        f = open("sampleDoc.txt","a")
        f.write("\nam new line")
        f.close()
        return "added fine"
    elif(mode=="rr"):
        f = open("sampleDoc.txt","r")
        quote=f.read()
        f.seek(0)
        quote+=f.read()
        f.close()
        return quote
    elif(mode=="w"):
        f = open("sampleDocForWrite.txt","w")
        f.write("am a new file created for writing")
        f.close


string=filefunctionsinpython("r")
print(string)
status=filefunctionsinpython("u")
print(status)
print(filefunctionsinpython("r"))
print("\n\n")
print(filefunctionsinpython("rr"))
print(filefunctionsinpython("w"))
