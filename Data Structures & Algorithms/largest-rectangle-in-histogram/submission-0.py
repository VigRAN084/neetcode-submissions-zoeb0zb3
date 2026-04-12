class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def maxRightImpl(heights, arr):
            stack = []
            for i, height in enumerate(heights):
                # Invariant: stack will be nondecreasing
                while stack and height < heights[stack[-1]]:
                    updateMaxDistanceIdx = stack.pop()
                    arr[updateMaxDistanceIdx] = i
                stack.append(i)
            return arr

        def maxLeftImpl(heights, arr): 
            stack = []
            for i in range(len(heights) - 1, -1, -1):
                height = heights[i]
                # Invariant: stack will be nondecreasing
                while stack and height < heights[stack[-1]]:
                    updateMaxDistanceIdx = stack.pop()
                    arr[updateMaxDistanceIdx] = i
                stack.append(i)
            return arr

        N = len(heights)
        maxLeft = maxLeftImpl(heights, [-1] * N) # leftmost bar that can use this height
        maxRight = maxRightImpl(heights, [N] * N) # rightmost bar that can use this height

        maxArea = float('-inf')
        for i in range(len(maxLeft)):
            l = maxLeft[i] + 1
            r = maxRight[i] - 1
            width = r-l+1
            height = heights[i]
            maxArea = max(width*height, maxArea) 
        return maxArea
