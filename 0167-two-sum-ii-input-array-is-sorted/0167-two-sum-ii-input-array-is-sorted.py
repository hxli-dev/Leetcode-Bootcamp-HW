class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0                       #start
        r = len(numbers)-1          #end
        sum = 0

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                return[l+1, r+1]

            if sum < target:
                l += 1 
            else: r -= 1
        
        
