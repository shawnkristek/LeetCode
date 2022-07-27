class Solution:
    def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2 

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft  = A[i]     if i >= 0           else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft  = B[j]     if j >= 0           else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # pass condition
            if Aleft <= Bright and Bleft <= Aright:
                # calc median if an odd total length
                if total % 2:
                    return min(Aright, Bright) / 1
                # if even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else: 
                l = i + 1

# test

tests = [ 
    ([1,3], [2], 2.0),
    ([1,2], [3,4], 2.50),
    ([1,3,8,9,15], [7,11,18,19,21,25], 11.0)
]

for nums1, nums2, solution in tests:
    print(Solution.findMedianSortedArrays(nums1, nums2) )