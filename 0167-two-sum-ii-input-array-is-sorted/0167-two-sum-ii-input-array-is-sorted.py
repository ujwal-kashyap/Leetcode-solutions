class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=(len(numbers))-1
        
        for i in range(len(numbers)):
            current_sum=numbers[left]+numbers[right]
            if current_sum==target:
                current_sum=[left+1,right+1]
                return current_sum
            elif current_sum<target :
               left+=1
            elif current_sum>target:
                right-=1   
               
        return []