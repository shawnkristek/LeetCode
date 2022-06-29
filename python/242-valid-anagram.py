from collections import Counter

class Solution:
    def isAnagram(s: str, t: str) -> bool:
        # strings must be same length
        if len(s) != len(t):
            return False
        
        # dictionaries for counting characters
        countS, countT = {}, {}
        
        # loop through strings and count characters
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False
        return countS == countT

class Solution1:
    def isAnagram(s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


#test
s = "anagram"
t = "nagaram"

print(Solution.isAnagram(s, t))