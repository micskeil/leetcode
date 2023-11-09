# https://leetcode.com/problems/two-sum/description/
# This solution has only O(n2) time complexity.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index, num in enumerate(nums):
            ## copy the list and remove the current element
            nums_copy = nums[:]
            nums_copy.remove(num)

            for index2, num2 in enumerate(nums):
                ## skip the same element
                if index == index2:
                    continue
                if num + num2 == target:
                    return [index, index2]


# This solution has only O(n) time complexity.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indicates = {}
        for index, num in enumerate(nums):
            if num in indicates:
                indicates[num].append(index)
                return indicates[num]
            indicates[target-num] = [index]

nums = [2,7,11,15]
target = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6

s = Solution()
print(s.twoSum(nums, target))
print(s.twoSum(nums2, target2))
print(s.twoSum(nums3, target3))