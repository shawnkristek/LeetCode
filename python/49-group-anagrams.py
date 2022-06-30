from collections import Counter

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

#test
strs = ["eat",
        "tea",
        "tan",
        "ate",
        "nat",
        "bat",
        ]

print(Solution.groupAnagrams(strs))