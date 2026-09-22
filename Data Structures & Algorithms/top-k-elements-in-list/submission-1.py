class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} 
        for ch in nums: 
            freq[ch] = freq.get(ch,0) + 1 
        ans = [] 
        sorted_freq = sorted(freq.items(), key = lambda x : x[1], reverse = True) 
        for i in range(k): 
            ans.append(sorted_freq[i][0])
        return ans 