#https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix=''
        arr=sorted(strs)
        first=arr[0]
        last=arr[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return prefix
            prefix+=first[i]
        return prefix
