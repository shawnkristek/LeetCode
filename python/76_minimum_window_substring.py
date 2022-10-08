from collections import defaultdict, Counter

class Solution:
    def minWindow(s: str, t: str) -> str:
        # init hash maps for t and the window
        thash = Counter(t)
        window = defaultdict(int)
        output = ""

        left = 0
        for right in range(len(s)):
            # add next letter to window
            window[s[right]] += 1

            # save and shrink window if contains t
            for k,v in thash.items():
                if v > window[k]:
                    break
            else: # executes only if s contains t
                # shrink window if it will still contain t
                while window[s[left]] - 1 >= thash[s[left]] and left < right:
                    window[s[left]] -= 1
                    left += 1

                # update output
                if (right - left + 1) <= len(output if len(output) > 0 else s):
                    output = s[left:right + 1]

        return output

# test
tests = [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", "")
]

for s,t,solution in tests:
    print(Solution.minWindow(s,t) == solution)