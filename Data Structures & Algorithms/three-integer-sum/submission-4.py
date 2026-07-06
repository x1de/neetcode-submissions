class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        srted = sorted(nums)
        output=[]
        for i, val in enumerate(srted):
            if i>0 and val == srted[i-1]:
                continue
            target = srted[i]*-1
            left = i+1
            right = len(nums)-1
            while left<right:
                if srted[left]+srted[right] == target:
                    output.append([srted[i],srted[left],srted[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and srted[left] == srted[left - 1]:
                        left += 1
                    while left < right and srted[right] == srted[right + 1]:
                        right -= 1
                elif srted[left]+srted[right] < target:
                    left+=1
                elif srted[left]+srted[right] > target:
                    right-=1
        return output