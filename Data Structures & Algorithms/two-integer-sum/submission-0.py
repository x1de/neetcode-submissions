class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr1 = {}
        for i in range(len(nums)):
            if (target-nums[i]) not in arr1:
                arr1[nums[i]]=i
            else:
                return [arr1[target-nums[i]],i]