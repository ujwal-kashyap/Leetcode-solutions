class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if k==0:
            return
        left=nums[:-k]
        right=nums[-k:]
        nums[:]=right+left 
# reduce k
# find left part
# find right part
# put them back into nums