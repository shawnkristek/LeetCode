from collections import defaultdict

class Solution:
    def characterReplacement(s: str, k: int) -> int:
        charCounts = defaultdict(int)
        charCounts["A"] = 0
        maxLength = 0

        left = 0
        for right in range(len(s)):
            charCounts[s[right]] += 1

            # window length - most freq char <= k
            if (right - left + 1) - max(charCounts.values()) > k:
                charCounts[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)
        return maxLength

class Solution1:
    def characterReplacement(s: int, k: int) -> int:
        charCounts = defaultdict(int)
        charCounts["A"] = 0
        maxLength = 0

        left = 0
        maxFreq = 0
        for right in range(len(s)):
            charCounts[s[right]] += 1
            maxFreq = max(maxFreq, charCounts[s[right]])

            # window length - most freq char <= k
            if (right - left + 1) - maxFreq > k:
                charCounts[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)
        return maxLength


# test
tests = [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
    ("", 0, 0)
]

for s,k,solution in tests:
    print(Solution.characterReplacement(s,k) == solution)