from collections import defaultdict, Counter

class Solution:
  def checkInclusion(s1: str, s2: str) -> bool:
    # window length
    k = len(s1)
    window = defaultdict(int)
    s1hash = Counter(s1)

    left = 0
    for right in range(len(s2)):

      # add new letter to hash
      window[s2[right]] += 1

      # shrink window if longer than s1
      if right - left  + 1 > k:
        if window[s2[left]] == 1:
          window.pop(s2[left])
        else:
          window[s2[left]] -= 1

        left += 1
      
      # check for permutation
      if window == s1hash:
        return True

    return False

# test
tests = [
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False)
]

for s1,s2,solution in tests:
  print(Solution.checkInclusion(s1,s2) == solution)