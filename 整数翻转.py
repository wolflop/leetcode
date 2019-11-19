# -*- coding:utf-8 -*-
#reverInt.py
class ReverInt:
	def __init__(self, inputInt):
		#初始化参数
		self.inputInt = inputInt
	def reversInt(self):
		#设置返回的字符串，初始化为0
		outStr = 0
		#判断输入的值是否为int类型的，并且在[0,2^31-1]之中，如果在就将数字转成字符串进行反序操作，再转成int类型返回
		if isinstance(self.inputInt, int) and self.inputInt < 2**31-1 and self.inputInt >= 0:
			outStr = int(str(self.inputInt)[::-1])
			return outStr
		#判断输入的值是否为int类型的，并且在[-2^31-1, 0]之中，如果在就将数字取绝对值再转成字符串进行反序操作，再转成int类型后取负数返回
		elif is instance(self.inputInt, int) and self.inputInt > 2**31-1 and self.inputInt < 0:
			outstr = -int(str(abs(self.inputint))[::-1])
			return outStr
		else:
			print("the inputInt is error!")

if __name=='__main__':
	inputint = 12345
	reverint = ReverInt(inputint)
	print(reverint.reversInt())
		
