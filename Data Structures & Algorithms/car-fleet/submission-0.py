from operator import itemgetter
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        i = len(position)-1
        lst = list(zip(position,speed))
        lst.sort(key=itemgetter(0))
        stk = []
        while i >= 0:
            pos, speed = lst[i]
            time = (target - pos)/speed
            if not(stk and time <= stk[-1][1] and pos <= stk[-1][0]):
                stk.append((pos,time))
            i-=1
        return len(stk)