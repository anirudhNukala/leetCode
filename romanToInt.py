class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        sum = 0
        for i in range(len(s) - 1):
            if hashMap[s[i]] < hashMap[s[i + 1]]:
                sum -= hashMap[s[i]]
            elif s[i] in hashMap:
                sum += hashMap[s[i]]

        sum += hashMap[s[-1]]
        return sum
            