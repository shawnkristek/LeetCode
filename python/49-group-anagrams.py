from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        """
        use dictionaries and compare
        create a list of dictionaries element by element and ouput list of lists. 
        """
        # func to convert strings to keys
        def key_func(s: str) -> str:
            key = list(s)
            key.sort()
            return "".join(key)

        #init dictionary
        lists = dict()

        # loop thru strs
        for s in strs:
        # check if current string is an anagram for previous
            key = key_func(s)
            if key in lists:
                # add to existing anagram list
                lists[key].append(s)
            else:
                # add new anagram list
                lists[key] = [s]

        # reformat for output
        output = list(lists.values())

        return output 

class Solution1:
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list) # charCount -> list[anagrams]

        for s in strs:
            charCount = [0] * 26

            # count chars and map to index
            for c in s:
                charCount[ord(c)-ord("a")] += 1
            
            ans[tuple(charCount)].append(s)

        # format from dict_values -> list
        return list(ans.values())


#test
strs = ["eat",
        "tea",
        "tan",
        "ate",
        "nat",
        "bat",
        ]

print(Solution1.groupAnagrams(strs))