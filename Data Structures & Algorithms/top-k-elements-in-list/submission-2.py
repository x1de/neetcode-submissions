class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            hmap[i]=1+hmap.get(i,0)
        for ke,v in hmap.items():
            freq[v].append(ke)
        ans = []
        for j in range(len(freq)-1,0,-1):
            for n in freq[j]:
                ans.append(n)
                if len(ans)==k:
                    return ans
        