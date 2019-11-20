# -*- coding:utf-8 -*-
#filename:atoi.py

class Atoi:
    def __init__(self, inputStr):
        #初始化输入变量
        self.inputStr = inputStr
    def atoi(self):
        #创建digitList用来存储数字
        diglitList = []
        #判断输入的是否为字符串
        if isinstance(self.inputStr, str):
            counter = 0
            #在字符串里循环，判断第一个非空是否是‘-’和数字，如果是，就添加到diglitList里面，如果不是就退出
            while counter < len(self.inputStr):
                if self.inputStr[counter] == '-':
                    digitList.append(self.inputStr[counter])
                    counter += 1
                elif self.inputStr[counter].isdigit():
                    digitList.append(self.inptuStr[counter])
                    counter += 1
                    if not self.inputStr[counter].isdigit():
                        break
                else:
                    counter += 1
        else:
            print("the input str is not correct!")
        #将diglist的数字相连节后，返回int类型的数字
        outStr = "".join(digitList)
        return int(outStr)

if __name__=='__main__':
    inputStr = '   -211 22alkjla  daf'
    atoi = Atoi(inputstr)
    outstr = atoi.atoi()
    print(outstr)
