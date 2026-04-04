class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        positionTimes = [(position[i], (target - position[i])/speed[i]) for i in range(N)]
        positionTimes.sort(reverse = True)

        timeBound = 0.0
        fleets = 0
        for pos, time in positionTimes:
            if time > timeBound:
                fleets += 1
                timeBound = time
        return fleets