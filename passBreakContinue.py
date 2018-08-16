def passbreakcontinue(n):
    while True:
        if(n%2==0):
            print(n)
        elif(n%6==0):
            continue
        else:
            pass
        n-=1
        if(n==0):
            break;
