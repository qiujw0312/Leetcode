# -*- coding: utf-8 -*-  
'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。


链接：https://leetcode-cn.com/problems/longest-common-prefix
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        substring = ""
        for i in xrange(len(strs[0])):
            substring1 = substring + strs[0][i]
            for string in strs:
                if not string.startswith(substring1):
                    return substring
            substring = substring1
        return substring