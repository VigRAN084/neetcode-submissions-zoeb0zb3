class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        positionTimes = [(position[i], (target - position[i])/speed[i]) for i in range(N)]
        positionTimes.sort(reverse=True)

        # positionTimes guaranteed to be sorted by position AND time 
        # you will arrive there
        stack = []
        fleets = N
        print(positionTimes)
        for pos, time in positionTimes:
            if stack and stack[-1][1] >= time:
                fleets -= 1
            else:
                stack.append((pos, time))
        return fleets
            

