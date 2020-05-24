class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#        为什么这么写不行？
#        store = 0
#        for num in nums:
#            if num != 0:
#                num, nums[store] = nums[store], num
#                store += 1

        if not nums: return
        store = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[store] = nums[store], nums[i]
                store += 1
        