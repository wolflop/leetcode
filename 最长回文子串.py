class solution:
    def __init__(self, inputStr):
        self.inputStr = inputStr
    def longestPalindrome(self):
        countA = 0                  #设置计数countA
        output = []                  #设置输出字符串
        while countA< len(self.inputStr):         #countA在输入端字符串中迭代
            for countB in range (countA, len(self.inputStr), 1):     #countB在以countA为起点的迭代
                '''
                如果发现两个字符相同，就截取这两个字符中间所有的字符串
                再逐个比较这些子串是否相同，是否符合回文串的标标准
                回文串标准：列表中正序跟倒序相同即为回文串
                如果符合回文串标准，还要跟已经获取的回文子串儿比较长度
                如果比已经添加的回文子串的大，则添加到output列表里，
                '''
                if self.inputStr[countA] == self.inputStr[countB]:
                    output1 = self.inputStr[countA:countB+1]
                    if output1 == output1[::-1]:
                        if output:
                            temp = output.pop()
                            if len(temp) < len(self.inputStr[countA:countB+1]):
                                output.append(self.inputStr[countA:countB+1])
                            else:
                                output.append(temp)
                        else:
                            output.append(self.inputStr[countA:countB+1])
            countA += 1
        if len(output[0]) > 1:
            return output[0]
        else:
            print("There is no Pllindrome.")


if __name__=='__main__':
    inputstr = 'abad12343211'
    solution = solution(inputstr)
    c = solution.longestPalindrome()
    print(c)
