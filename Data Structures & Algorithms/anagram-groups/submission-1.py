class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap={}

        for s in strs:
            if ''.join(sorted(s)) in hmap:
                hmap[''.join(sorted(s))].append(s)
            else:
                hmap[''.join(sorted(s))]=[s]
        return list(hmap.values())
