class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashh = set()

        for num in nums: 
            if num in hashh:
                return True
            hashh.add(num)
        return False       
        
        
        