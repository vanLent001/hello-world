def Transcriptor(filename):
    f= open(filename,"r")
    for line in f:
        RNA= line.replace("T","U")
    return RNA



        
