class Ram:
    def __init__(self, T):
        self.T = T
    def read(self):
        self.file = open(self.T, 'r')
        self.pro_order = self.file.readlines()
        print("프로그램 전체 RAM에 적재:", self.pro_order, "\n")
            
    def check(self):
        if self.pro_order != "":
            self.pc = 0
            self.protocal = 1
        else:
            self.protocal = 0
        return self.protocal

    def sendorder(self, addr):
        self.order = self.pro_order[addr].rstrip()
        
    def datasender(self, addre):
        self.data = self.pro_order[addre].split("\t")
        self.data_send = self.data[2]

    def update(self, movingdata, addr):
        self.pro_order[addr] = '\t'+str(addr)+'\t'+str(movingdata)+'\t\t\n'
        print("업데이트된 주소", addr,"의 데이터", self.pro_order[addr])
    
