#-*- coding：utf-8 -*-
#filename:lengthOfLongestSubString.py

class Solution:
    def __init__(self, inputString):
		#初始化参数
		self.inputString = inputString
	def lengthOfLongestSubString(self):
		'''
		outstr为返回字符串
		counterA/counterB 为0
		'''
		outStr = []
		counterA = 0
		counterB = 0
		#设置循环，counterA和counterB在输入的字符串内循环
		while(counterA < len(self.inputString) and counterB < len(self.inpuString)):
			'''	
			如果字符串中self.inputString[counterA]不在inputString[counterB:counterA]中
			ze进行判断，先判断outStr是否为空，如果非空，取出列表的内容与不重复的字符子串比较，如果已存在的
			str的长度比添加的小，则替换,否则继续保存；如果是空，则直接添加该字符子串
			'''		
			if self.inputString[counterA] not in inputString[counterB:counterA]:
				if outStr:
					temp = outStr.pop()
					if temp < len(self.inputString[conterB：counterA])：
						outStr.append(self.inputString[conterB:counterA])
					else:
						outStr.append(temp)
				else:
					outStr.append(self.inputString[conterB:counterA])
				counterA += 1
			#判断字符串中self.inputString[counterA]在inputString[counterB:counterA]中，计数加1，并将counterB位置移至counterA
			elif inputString[counterA] in self.inputString[counterB:counterA]:
				counterB = counterA
				counterA +=1
			#其它条件退出循环
			else:
				break
		#返回最长的无重复的字符子串
		return outStr[0]
	
	
if __name__ == '__main__':
	inputString = 'abcabcdbb'
	str_num = Solution(inputString)
	print("The longest no deplicate sub string is %s" % str_num.lengthOfLongestSubString())
	
