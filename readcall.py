#runs in python3
def readBC(functionName, params, returnType):
    f = open('readto2.csv','a')
    f.write(str(functionName)+'\n')
    f.write(str(params)+'\n')
    f.write(str(returnType)+'\n')
    f.close()

    while True:
        with open("readto3.csv") as g:
            lines = len(g.readlines())

        if lines >= 1:
             fromfile = open('readto3.csv','r+')
             fromfile_contents = fromfile.readlines()
             response = fromfile_contents[0].strip()

             fromfile.truncate(0)
             return response


#print(readBC("getStudentName(address)", [0x5e8d910869c97eb5d23e03a7c4f95548c676f776], 'string'))
