class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 0
        while l <= r:
            m = (l+r)//2
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile/m)
            if time_taken > h:
                l = m+1
            else:
                k = m
                r = m-1
        return k