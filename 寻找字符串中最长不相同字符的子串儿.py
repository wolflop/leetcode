#-*- coding：utf-8 -*-
#filename:lengthOfLongestSubString.py

class Solution:
    def __init__(self, inputString):
		self.inputString = inputString
	def lengthOfLongestSubString(self):
		outStr = []
		counterA = 0
		counterB = 0
		while(counterA < len(inputString) and counterB < len(inpuString)):
			if inputString[counterA+1] not in inputString[counterA:]:
				outStr.append(inputString[counterA+1:]）
				counterA +=1
			elif inputString[counterA+1] in inputString[counterA:]:
				counterA +=1
				counterB +=1
				Solution(inputString[counterB:]).lengthOfLongestSubString()
			else:
				break
		return outStr
	
	
if __name__ == '__main__':
	inputString = 'abcabcdbb'
	str_num = Solution(inputString)
	
