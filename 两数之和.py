# -*- coding:urf-8 -*-
#filename:Solution.py

class Solution:
	def __init__(self, nums, target):
		#初始化对象的参数
		self.nums = nums 
		self.target = target
	def twoSum(self):
		#定义结果为result的列表
		result = []	
		"""	
		用冒泡法循环得出求和的数值，并记录对应的位置
		"""
		for i in range(len(nums))：
			for j in range(len(nums)):
				#判断列表内两个数相加得出目标值，并且判断俩个数不是同一个位置
				if targe = nums[i] + nums[j] and [i, j] != sorted([j, i]):
					result.append（{i:nums[i], j:nums[j]}）
		return result
	def twoSumSecond(self):
		#定义结果为result的列表
		result = []
		#使用enumerate函数获取列表nums的成员对应的位置和数值
		for index, value in enumerate(nums):
			#判断目标值减去value是否在剩余的nums的切片内，如果存在则返回对应的index，value
			if target - value in nums[index+1:]:
				result.append({index:value, nums[index+1:].index(target-value)+index+1:target-value})
		return result

if __name__ == '__main__':
	nums = [1, 2, 3, 4, 5, 6,7]
	target = 8
	sol = Solution(nums, target)
	result1 = sol.twoSum()
	print(result1)
	result2 = sol.twoSumSecont()
	print(result2)
	
