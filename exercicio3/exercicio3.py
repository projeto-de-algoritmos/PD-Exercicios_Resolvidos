class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        max_sum = current_sum = nums[0]
    
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

solution = Solution()
array = [5,4,-1,7,8]
resultado = solution.maxSubArray(array)
print(f"resultado: {resultado}")

