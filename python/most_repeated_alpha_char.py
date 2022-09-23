"""
Given a string s, return the most frequent character (an alphabet letter) in the string s.

- Input string of ascii characters.
- Only care about the alphabet letters.
- 'A' does not equal 'a'
"""
class Solution:
    def most(s: str) -> str:
        SHIFT = ord('A') #used to shift indicies for list
        mx = -1 #max_count
        ret = ''
        counts = [-1] * (ord('z') - ord('A'))

        for l in s:
            if l.isalpha():
                index = ord(l) - SHIFT
                counts[index] +=1
                if counts[index] > mx:
                    mx = counts[index]
                    ret = l
        return ret


tests = [ 
    ('abcddefda1111133333333',              'd'),
    ('AA0AB0BB0ccc0aa0aw00woOBBBw123123',   'B'),
]

for s,solution in tests:
    sol = Solution.most(s)
    print( sol == solution )