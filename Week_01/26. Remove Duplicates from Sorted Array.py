class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        
        store = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                store += 1
                nums[store] = nums[i]
        return store + 1