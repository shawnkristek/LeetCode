DELIMITER = "+"

class Solution:
    def encode(strs: list[str]) -> str:
        # write your code here
        en = ""
        for s in strs:
            en += str(len(s)) + DELIMITER + s
        return en

    def decode(s: str) -> list[str]:
        # write your code here
        strs = []
        # length = 0

        # loop through all char in str looking for (int)(DELIMITER)(string)
        i = 0
        while i < len(s):
          # grab and parse word length
          j = i
          while s[j] != DELIMITER:
            j += 1
          length = int(s[i:j])
          # skip over DELIMITER
          j += 1
          # bump i to end of word
          i = j + length
          # grab word
          strs.append(s[j:i])

        return strs

# test
cases = [
  ["good", "word", "hello", "+45thousand", "kendra", "acorn"],
  ["34try+42", "test", "123", "try"]
]

for case in cases:
  print(Solution.decode(Solution.encode(case)) == case)