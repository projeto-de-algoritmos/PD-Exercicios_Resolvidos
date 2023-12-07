class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        sum = current_sum = nums[0]
    
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            sum = max(sum, current_sum)
            
        return sum

solution = Solution()
array = [-2,1,-3,4,-1,2,1,-5,4]
resultado = solution.maxSubArray(array)
print(f"resultado: {resultado}")

