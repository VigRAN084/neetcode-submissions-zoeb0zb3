class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Decision tree
        1. Which side is sorted (left subarray or right subarray) 
        2. Could the element be in the sorted side?
            --> if not, it MUST be in the other side
            nums[l] < target < nums[m]  OR
            nums[m] < target < nums[r]
        '''

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2 
            if nums[m] == target: 
                return m
            # left search space is sorted
            elif nums[m] <= nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            # right search space is sorted
            else:
            
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1