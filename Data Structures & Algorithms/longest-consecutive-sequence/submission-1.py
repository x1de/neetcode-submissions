class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = set(nums)
        len = 0
        for i in nums:
            if i-1 not in map:
                current_len =1
                while i+current_len in map:
                    current_len +=1
                len = max(current_len, len)
        return len