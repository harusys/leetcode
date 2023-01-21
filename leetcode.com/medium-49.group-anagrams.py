#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i, s in enumerate(strs):
            counter = Counter(s)
            # 辞書型を並び替え
            counter = sorted(counter.items())
            counter = dict((k, v) for k, v in counter)
            # キーにするため辞書型 -> 文字列に変換
            key = json.dumps(counter)
            if key in dic:
                dic[key] = dic[key] + [s]
            else:
                dic[key] = [s]
        return dic.values()
# @lc code=end
