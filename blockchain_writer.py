#must use python2
from ethjsonrpc import EthJsonRpc


def writeBCFunc(functionName, stuaddr, num, den):
    c = EthJsonRpc('10.33.1.244',8545)
    contractAddr= u'0x26d6699a180bd6654ca030965396d7c132bd7cc6'
    tx = c.call_with_transaction(c.eth_coinbase(), contractAddr, functionName+'(address,uint256,uint256)', [stuaddr,num,den])
    print tx

while True:
    with open("writeto2.csv") as f:
      lines = len(f.readlines())
    #print(lines)
    if lines >= 4:
        fromfile = open('writeto2.csv','r+')
        fromfile_contents = fromfile.readlines()
        functionName = fromfile_contents[0].strip()
        stuaddr = int(fromfile_contents[1].strip(),16)
        num = int(fromfile_contents[2].strip())
        den = int(fromfile_contents[3].strip())
        print functionName
        print stuaddr
        print num
        print den
        fromfile.truncate(0)

        writeBCFunc(functionName,stuaddr,num,den)

#writeBCFunc('addEnglishScore',0x5e8d910869c97eb5d23e03a7c4f95548c676f776,3,4)
