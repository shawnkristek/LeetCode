class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        maxlength = 0
        window = ""
        
        for l in s:
            # shrink window if letter already in
            while l in window and window != l:
                window = window[1:]

            # add l if not in window
            if l not in window:
                window += l

            # update max length if greater
            maxlength = max(maxlength, len(window))
            
        return maxlength

class Solution1:
    def lengthOfLongestSubstring(s: str) -> int:
        maxLength = 0
        charSet = set()
        left = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength


#test
tests = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("aab", 2),
    ("", 0),
    ("dvdf", 3)]

for s, solution in tests:
    print(Solution1.lengthOfLongestSubstring(s) == solution)
