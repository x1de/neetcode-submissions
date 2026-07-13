from operator import itemgetter
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = list(zip(position,speed))
        lst.sort(reverse=True)
        stk = []
        for pos, speed in lst:
            time = (target - pos)/speed
            if not(stk and time <= stk[-1][1] and pos <= stk[-1][0]):
                stk.append((pos,time))
        return len(stk)