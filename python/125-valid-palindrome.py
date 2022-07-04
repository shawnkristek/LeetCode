class Solution:
    def isPalindrome(s: str) -> bool:
        # init pointers
        i = 0
        j = len(s)-1
        
        # loop until pointers meet
        while i < j:
            # skip all non alphanumeric chars
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            # check chars are equal
            if s[i].lower() != s[j].lower():
                return False
            # next
            i += 1
            j -= 1

        return True

class Solution1:
    def isPalindrome(s: str) -> bool:
        filtered = ''.join(filter(str.isalnum, s.lower()))
        i, j = 0, len(filtered)-1

        while i < j:
            if filtered[i] != filtered[j]:
                return False
            i += 1
            j -= 1

        return True

# test
cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("", True),
    (",.", True)
]

for s, solution in cases:
    print(Solution1.isPalindrome(s) == solution)