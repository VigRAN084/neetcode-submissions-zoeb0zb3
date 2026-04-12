class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def computeTime(k):
            return sum(math.ceil(piles[i] / k) for i in range(len(piles)))
        '''
        Brute Force

        let k = piles[0]
        s = sum(piles[i] / k + 1) for 0 <= i < n

        if s < hours:
            k -= 1
        elif s > hours:
            k += 1
        else:
            return k
        '''
        l = 1
        r = max(piles)
        res = (l + r) // 2
        while l <= r:
            k = (l + r) // 2
            timeToFinishBananas = computeTime(k) 
            # print(k, timeToFinishBananas)
            # very fast! try to find a smaller k value
            if timeToFinishBananas <= h:
                res = k
                r = k - 1
            # too slow, find a larger k value
            elif timeToFinishBananas > h:
                l = k + 1
        return res
                
