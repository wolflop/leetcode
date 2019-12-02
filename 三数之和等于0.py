# -*- coding:utf-8 -*-

class solution:
    def __init__(self, nums):
        self.nums = nums
    def threeSum(self):
        output=[]
        '''
        算法复杂度最高，益理解。
        依次循环，从而选出不同的值，但是相加等于0的。
        '''
        for countA in range(len(self.nums)):
            # print(countA)
            for countB in range(countA, len(self.nums)):
                for countC in range(countB, len(self.nums)):
                    if countA != countB and countA != countC and countB != countC:
                        if self.nums[countC] + self.nums[countA] + self.nums[countB] == 0:
                            output.append([self.nums[countA], self.nums[countB], self.nums[countC]])
        print(output)
        return output
    
