def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    
def userInputCasting():
    while True:
        string = input("Name: ")
        if(string.startswith("hello")):
            pass
        elif(string=="exit"):
            break;
        else:
            if(is_int(string)):
                print(int(string))
            else:
                print(string)
