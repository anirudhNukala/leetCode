class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) == 1:
            return 1
        lenLast = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                break
            lenLast += 1
        
        return lenLast
        
solution = Solution()
print(solution.lengthOfLastWord("    day"))