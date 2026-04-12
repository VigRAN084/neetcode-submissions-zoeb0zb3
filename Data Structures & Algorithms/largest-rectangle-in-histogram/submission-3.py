class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        One Pass Solution:
        - Iterate from left to right
        - Maintain a 'start' index for each height as u pop
        - it will give u the leftmost index while the nondecreasing 
             invariant of the stack gives u the rightmost index 

        Stack = [(start, height)]
        '''

        n = len(heights)
        heights = heights + [0]
        stack = [] 
        maxArea = heights[0] * 1
        for i, height in enumerate(heights):
            # naively assume u can start the rectangle at height i
            # it might be updated during popping to shift left
            start = i
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()      #idx == start for that height
                start = idx
                maxArea = max(maxArea, (i - idx) * h)
            # atp, u know the leftmost index for the current height
            stack.append((start, height))
        
        # need to postprocess the leftover elements....
        # these ones can stretch indefinitely towards the right b/c of 
        # nondecreasing stack
        # for idx, height in stack:
        #     maxArea = max(maxArea, (n - idx) * height)

        return maxArea  




