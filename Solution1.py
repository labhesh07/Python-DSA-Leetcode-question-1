from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        
        for i in range(len(nums)):
            sum = target - nums[i]
            
            
            if sum in dict1:
              
                return [dict1[sum], i]
            

            dict1[nums[i]] = i
        
nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target)) 