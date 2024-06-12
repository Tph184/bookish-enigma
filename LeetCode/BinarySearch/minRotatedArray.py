'''
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
'''

def findMin(nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]
        
        while left <= right:

            mid = (left + right) // 2
            res = min(nums[mid], res)

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return res
