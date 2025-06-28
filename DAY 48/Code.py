class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     from collections import defaultdict
     angrm = defaultdict(list)

     for word in strs:
        angrm[''.join(sorted(word))].append(word)
     return list(angrm.values())
