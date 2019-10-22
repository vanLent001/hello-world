def complement(filename):
    f= open(filename, "r")
    comseq=""
    for line in f:
        for i in line:
            if i=="A":
                comseq+="T"
            elif i=="C":
                comseq+="G"
            elif i=="T":
                comseq+="A"
            elif i=="G":
                comseq+="C"
    return comseq



