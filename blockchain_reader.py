#runs in python2
from ethjsonrpc import EthJsonRpc
import ast
import os


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def callBCFunc(functionName, params, returnType):
    c = EthJsonRpc('10.33.1.244',8545)
    f = open('readto3.csv', 'a')
    contractAddr = u'0x26d6699a180bd6654ca030965396d7c132bd7cc6'
    results = c.call(contractAddr, functionName, params, [returnType])
    f.write(str(results[0])+'\n')
    f.close()

while True:
    with open("readto2.csv") as f:
      lines = len(f.readlines())
    #print(lines)
    if lines >= 3:
        fromfile = open('readto2.csv','r+')
        fromfile_contents = fromfile.readlines()
        functionName = fromfile_contents[0].strip()
        params = ast.literal_eval(fromfile_contents[1].strip())
        print(type(params))
        returnType = fromfile_contents[2].strip()
        print functionName
        print params
        print returnType
        fromfile.truncate(0)


        callBCFunc(functionName, params, returnType)






#callBCFunc('getOwner()', [], 'address')
#callBCFunc('getEnglishProblemTotal()', [], 'uint8')
