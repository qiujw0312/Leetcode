# -*- coding: utf-8 -*-  
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

 示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

链接：https://leetcode-cn.com/problems/reverse-integer
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        if x >2147483647 or x < -2147483648:
            return 0
        try:
            while (x > 0):
                r *= 10
                r += x % 10
                x /= 10
            r = r*flag
            if r > 2147483647 or r < -2147483648:
                return 0 
            return r
        except:
            return 0