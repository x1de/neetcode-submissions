class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            j = len(heights)-1
            while i<j:
                max_area = max(max_area,min(heights[i],heights[j])*(j-i))
                j-=1
        return max_area