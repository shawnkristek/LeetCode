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



#test
ss = ["abcabcbb",
    "bbbbb",
    "pwwkew",
    "aab",
    "",
    "dvdf"]

for s in ss:
    print(Solution.lengthOfLongestSubstring(s))
