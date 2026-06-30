from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        post = [1]*len(nums)
        res = [1]*len(nums)
        for i in range(1,len(nums)):
            pre[i]=nums[i-1]*pre[i-1]
        for j in range(len(nums)-2,-1,-1):
            post[j]*=(nums[j+1]*post[j+1])
        for k in range(len(nums)):
            res[k]=pre[k]*post[k]
        return res