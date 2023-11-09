#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        checkList = []

        maxLen = 0
        for i, char in enumerate(s):
            if char in checkList:
              currentLen = len(checkList)
              checkList = []
              if currentLen > maxLen:
                maxLen = currentLen
            checkList.append(char)
        return maxLen

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
