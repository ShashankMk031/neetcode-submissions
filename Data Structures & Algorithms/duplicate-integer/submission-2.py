class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        seen = set() 
        for char in nums: 
            if char in seen: 
                return True 
            seen.add(char) 
        return False