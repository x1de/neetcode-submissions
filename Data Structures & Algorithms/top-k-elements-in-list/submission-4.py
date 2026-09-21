class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for num in nums:
            hmap[num]+=1
        return sorted(hmap.keys(), key=hmap.get, reverse=True)[:k]