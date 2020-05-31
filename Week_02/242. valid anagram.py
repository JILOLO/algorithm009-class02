class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount, tcount = [0] * 26, [0] * 26
        for item in s:
            scount[ord(item) - ord('a')] += 1
        for item in t:
            tcount[ord(item) - ord('a')] += 1
        return scount == tcount