class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Find inflection point
        # --> nums[i] < nums[i-1]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[m-1]: 
                return nums[m]
            # inflection is in right half
            elif nums[m] > nums[r]:
                l = m + 1
            # .. left ..
            else:
                r = m - 1
        return nums[l]