class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for a in s:
                count[ord(a) - ord('a')] += 1
            ans[tuple(count)] += [s] # ans[tuple(count)].append(s)
        return ans.values()