class Solution:
    def productExceptSelf(nums: list[int]) -> list[int]:
        product = 1
        output = [1] * len(nums)
        zeros = 0
        
        # find product of all nums
        for num in nums:
            # skip any zeros
            if num != 0:
                product *= num
            else:
                zeros += 1
            # if two or more zeros, all values are zero
            if zeros > 1:
                return [0] * len(nums)
            
        # output[i] = product / nums[i]
        for i in range(len(nums)):
            if nums[i] != 0:
                output[i] = int(product / nums[i])
            # except when a zero is present
            else:
                # all values are zero except for the zero's index which is product
                output[i] = product
                for j in range(len(nums)):
                    if i != j:
                        output[j] = 0
                return output
            
        return output
class Solution1:
    def productExceptSelf(nums: list[int]) -> list[int]:
        output = [1] * len(nums)
        
        # calculate pre-products
        preproduct = 1
        for i in range(len(nums)):
            output[i] = preproduct
            preproduct *= nums[i]

        # calculate post-products and combine with pre-products
        postproduct = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] *= postproduct
            postproduct *= nums[j]

        return output

# test
inputs = [
        [1,2,3,4],
        [-1,1,0,-3,3],
        [0,0]
]

for nums in inputs:
    print(Solution1.productExceptSelf(nums))