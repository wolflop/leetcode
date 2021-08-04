list_a=[]                                                                                   
def rmDu(list_a):                                                                           
    # list_a = [0, 0, 1, 2, 3, 3, 3]                                                        
    for i in range(len(list_a)-1, 0, -1):                                                   
        if list_a[i] == list_a[i-1]:                                                        
            del list_a[i]                                                                   
    # print(list_a)                                                                         
    return list_a                                                                           
def rmDu1():                                                                                
    list_a = [0, 0, 1, 2, 3, 3, 3, 2]                                                       
    newList = []                                                                            
    for i in list_a:                                                                        
        if i not in newList:                                                                
            newList.append(i)                                                               
    for i in newList:                                                                       
        count = 0                                                                           
        for j in range(len(list_a)):                                                        
            if list_a[j] == i:                                                              
                count += 1                                                                  
        print(i, count)                                                                     
def rmDu2():                                                                                
    list_a = [2, 2, 2, 1, 3, 3]                                                             
    new_len = len(list_a)                                                                   
    i = 0                                                                                   
    while i < new_len:                                                                      
        j = i + 1                                                                           
        while j < new_len:                                                                  
            if list_a[j] == list_a[i]:                                                      
                list_a.pop(i)                                                               
                new_len = len(list_a)                                                       
            else:                                                                           
                j += 1                                                                      
        i += 1                                                                              
    return rmDu(list_a)                                                                     
                                                                                            
def findOut():                                                                              
    list_a = [2,2,1,3,4,5,4]                                                                
    newlist = []                                                                            
    for i in range(len(list_a)):                                                            
        if list_a[i] not in list_a[0:i]:                                                    
            if list_a[i] not in list_a[i+1::]:                                              
                newlist.append(list_a[i])                                                   
    return newlist                                                                          
                                                                                            
def inselect():                                                                             
    nums1 = [1, 2, 2, 1, 7]                                                                 
    nums2 = [2, 1, 1, 2, 5, 5]                                                              
    newNums=[]                                                                              
    if len(nums1) < len(nums2):                                                             
        for i in nums1:                                                                     
            if i in nums2:                                                                  
                newNums.append(i)                                                           
    else:                                                                                   
        for i in nums2:                                                                     
            if i in nums1:                                                                  
                newNums.append(i)                                                           
    return newNums                                                                          
                                                                                            
def pluOne():                                                                               
    nums = input("请输入：")                                                                    
    oldList = []                                                                            
    for i in range(len(nums)):                                                              
        oldList.append(int(nums[i]))                                                        
    newList = oldList[:-1]                                                                  
    newList.append(oldList[-1] + 1)                                                         
    return newList                                                                          
                                                                                            
                                                                                            
def moveZeroes():                                                                           
    nums = [0,1,0,3,12]                                                                     
    count = 0                                                                               
    newnum = []                                                                             
    for i in range(len(nums)):                                                              
        if nums[i] == 0:                                                                    
            count += 1                                                                      
        else:                                                                               
            newnum.append(nums[i])                                                          
    for i in range(count):                                                                  
        newnum.append(0)                                                                    
    return newnum                                                                           
                                                                                            
nums = []                                                                                   
def twoSum(target, nums):                                                                   
    result = []                                                                             
    for index, value in enumerate(nums):                                                    
        if target - value in nums[index+1:]:                                                
            result.append({value:index, target-value:nums[index+1:].index(target-value)+inde
    return result                                                                           
                                                                                            
def twoSum1(target, nums):                                                                  
    result = []                                                                             
    for i in range(len(nums)):                                                              
        for j in range(i, len(nums)):                                                       
            if target - nums[i] == nums[j]:                                                 
                result.append({i:nums[i], j:nums[j]})                                       
    return result                                                                           
def reseveStr():                                                                            
    s = ["h","e","l","l","o"]                                                               
    newS = []                                                                               
    for i in range(len(s)-1, -1, -1):                                                       
        newS.append(s[i])                                                                   
    return newS                                                                             
def reserStr1():                                                                            
    s = ["h","e","l","l","o"]                                                               
    countA = 0                                                                              
    countB = len(s)-1                                                                       
    while countA < len(s)/2 and countB >= len(s)/2:                                         
        s[countA], s[countB] = s[countB], s[countA]                                         
        countA +=1                                                                          
        countB -=1                                                                          
    return s                                                                                
                                                                                            
def reverseS(x):                                                                            
    temp = ""                                                                               
    if -2**31-1 <= x <= 2**31-1:                                                            
        newx = str(abs(x))                                                                  
        for i in range(len(newx)-1, -1, -1):                                                
            temp += newx[i]                                                                 
    else:                                                                                   
        return 0                                                                            
    if x >= 0:                                                                              
        return temp                                                                         
    else:                                                                                   
        return '-' + temp                                                                   
                                                                                            
def firstUniChar():                                                                         
    s = "llaeetcode"                                                                        
    num = []                                                                                
    for i in range(len(s)):                                                                 
         if s[i] not in s[0:i] and s[i] not in s[i+1:] :                                    
            num.append(i)                                                                   
            break                                                                           
         else:                                                                              
            continue                                                                        
    if len(num) == 1:                                                                       
        print(num[0])                                                                       
    else:                                                                                   
        print(-1)                                                                           
                                                                                            
def isAnagram():                                                                            
    s = "a"                                                                                 
    t = "ab"                                                                                
    list_s = []                                                                             
    list_t = []                                                                             
    if 1 < len(s) < 5 * 10**4 and 1 < len(t) < 5 * 10**4:                                   
        if len(s) == len(t):                                                                
            print(s)                                                                        
            print(t)                                                                        
            for i in range(len(s)):                                                         
                list_s.append(s[i])                                                         
                list_t.append(t[i])                                                         
        else:                                                                               
            return False                                                                    
    else:                                                                                   
        return False                                                                        
    list_s = sorted(list_s)                                                                 
    list_t = sorted(list_t)                                                                 
    print(list_s)                                                                           
    print(list_t)                                                                           
    if list_s == list_t:                                                                    
        return True                                                                         
    else:                                                                                   
        return False                                                                        
                                                                                            
def isPalindrome():                                                                         
    s = "a, db, bd,a"                                                                       
    temp = ""                                                                               
    if 1 <= len(s) <= 2 * 105:                                                              
        for i in s:                                                                         
            if i.isdigit():                                                                 
                temp += i                                                                   
            elif i.isalpha():                                                               
                temp += i.lower()                                                           
            else:                                                                           
                continue                                                                    
    print(temp[::-1])                                                                       
    if temp == temp[::-1]:                                                                  
        return True                                                                         
    else:                                                                                   
        return False                                                                        
if __name__=='__main__':                                                                    
    # print(rmDu1())                                                                        
    # print(findOut())                                                                      
    # print(moveZeroes())                                                                   
    # print(twoSum1(target, nums))                                                          
    print(reverseS(1534236469))                                                             
    # firstUniChar()                                                                        
    # a = isAnagram()                                                                       
    # print(a)                                                                              
    # print(isPalindrome())                                                                 
