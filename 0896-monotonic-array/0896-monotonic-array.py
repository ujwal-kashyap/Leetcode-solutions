class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        nums1=sorted(nums) 
        nums2=sorted(nums,reverse=True)
        if nums == nums1: 
            return True
        elif nums==nums2:
            return True
        return False
        