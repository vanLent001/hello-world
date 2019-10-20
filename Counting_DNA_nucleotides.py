def count_function(filename):
    f= open(filename, "r")
    Total=0
    for line in f:
        line= line.rstrip()
        Acount= line.count("A")
        Ccount= line.count("C")
        Tcount= line.count("T")
        Gcount= line.count("G")
        Ncount= line.count("N")
        Total+=len(line)
    Content="Total: %d\nA: %d\nC: %d\nT: %d\nG: %d\nN: %d"%(Total, Acount,Ccount,Tcount,Gcount,Ncount)
    return Content
        
          



