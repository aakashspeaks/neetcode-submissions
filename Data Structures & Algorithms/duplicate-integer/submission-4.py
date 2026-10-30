class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        charset = set()
        for i in range(len(nums)):
            if nums[i] in charset:
                return True
            charset.add(nums[i])
        return False
        
        