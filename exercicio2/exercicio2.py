class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        def backtrack(start, path):
            if start == len(s): # todas as palavras foram encontradas
                result.append(" ".join(path))
                return

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    backtrack(end, path + [word])

        result = []
        backtrack(0, [])
        return result

solution = Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
output = solution.wordBreak(s, wordDict)
print(output)