def writeBC(functionName, stuaddr, num, den):
    f = open('writeto2.csv','a')
    f.write(str(functionName)+'\n')
    f.write(stuaddr+'\n')
    f.write(str(num)+'\n')
    f.write(str(den)+'\n')
    f.close()

#writeBC('addMathScore',"0x5e8d910869c97eb5d23e03a7c4f95548c676f776",3,4)
