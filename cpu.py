class Cpu:
    def __init__(self,protocal, R):
        self.protocal = protocal
        self.pc = R.pc
        self.totalreg = {"AX":"", "BX":"", "CX":"", "DX":""}
        self.stackpointer = []
        self.stack = []
        self.a = 'true'
        print("범용 레지스터:", self.totalreg, "\n")
        print("프로그램 카운터:", self.pc, "\n")
        
    def PC(self):
        self.pc = self.pc+1
        

    def controler1(self, R):
        if self.protocal == 1 and self.pc != "":
            addr = self.pc
            R.sendorder(addr)
            print("실행할 주소의 명령어 CPU에 적재:", R.order)

    def controler2(self, R):
        comdiv = self.comline.split("\t")
        com = comdiv[2]
        if com == "MOV" or "PUSH" or "POP" or "PRINT":
            if com == "MOV" :
                if 'X' in comdiv[3]:
                    self.addre = int(comdiv[4])
                    self.key = comdiv[3] 
                    R.datasender(self.addre)
                    self.totalreg[self.key] = R.data_send
                    print("범용 레지스터:", self.totalreg, "\n")
                else:
                    self.addre = int(comdiv[3])
                    self.key = comdiv[4]
                    self.movingdata = self.totalreg[self.key]
                    R.update(self.movingdata, self.addre)
                    print("범용 레지스터:", self.totalreg, "\n")
            elif com == "PUSH":
                self.key = comdiv[3]
                self.value = self.totalreg[self.key]
                self.stack.append(self.value)
                print("현재 스택:", self.stack, "\n")
            elif com == "POP":
                self.value = self.stack[len(self.stack)-1]
                self.key = comdiv[3]
                self.totalreg[self.key] = self.value
                del self.stack[len(self.stack)-1]
                print("현재 스택:", self.stack)
                print("범용 레지스터:", self.totalreg, "\n")
            elif com == "PRINT":
                self.addre = int(comdiv[3])
                R.datasender(self.addre)
                print("출력값:", R.data_send, "\n")
            
        if com == "ADD":
            self.key1 = comdiv[3]
            self.key2 = comdiv[4]
            A = int(self.totalreg[self.key1])
            B = int(self.totalreg[self.key2])
            value = self.calculater(com, A, B)
            self.totalreg[self.key1] = value
            self.totalreg[self.key2] = ''
            print("범용 레지스터:", self.totalreg, "\n")
        if com == "MUL":
            self.key1 = comdiv[3]
            self.key2 = comdiv[4]
            A = int(self.totalreg[self.key1])
            B = int(self.totalreg[self.key2])
            value = self.calculater(com, A, B)
            self.totalreg[self.key1] = value
            self.totalreg[self.key2] = ''
            print("범용 레지스터:", self.totalreg, "\n")
        if com == "CALL":
            self.stackpointer.append(self.pc)
            self.pc = int(comdiv[3])
            print("실행할 주소(pc):", self.pc)
            print("스택포인터:", self.stackpointer, '\n')
        if com == "RETURN":
            self.pc = self.stackpointer[len(self.stackpointer)-1]
            del self.stackpointer[len(self.stackpointer)-1]
            print("돌아갈 주소(pc):", self.pc, "\n")
        if com == "HALT":
            self.a = 'false'
            
            
    def comreg(self, R):
        self.comline = R.order
        if self.comline != []:
            self.PC()
            print("다음 주소:", self.pc)

    def calculater(self, OP, A, B):
        if OP == "ADD":
            return A+B
        if OP == "MUL":
            return A*B
        
