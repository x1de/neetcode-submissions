class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(heights)-1
        while i<j:
            max_area = max(max_area,min(heights[i],heights[j])*(j-i))
            if heights[i]<heights[j]:
                i+=1
            elif heights[i]>heights[j]:
                j-=1
            else:
                i+=1
                j-=1
        return max_area