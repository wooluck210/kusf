from cpu import Cpu
from ram import Ram

R = Ram('T.txt')
R.read()
prot = R.check()
C = Cpu(prot, R)

while True:
    C.controler1(R)
    C.comreg(R)
    C.controler2(R)

    if C.a == 'false' or C.pc == "":
        break
