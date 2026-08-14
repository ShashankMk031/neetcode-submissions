class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {} 
        for i in range(len(nums)): 
            left = target - nums[i]
            if left in freq: 
                return [freq[left],i] 
            freq[nums[i]] = i 
        return [] 