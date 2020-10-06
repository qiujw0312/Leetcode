# -*- coding: utf-8 -*-  
'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = []
        def func(l,n):
            if n == 0:
                return 1
            q = 1
            p = 1
            for i in xrange(n):
                q = q * (i + 1)
                p = p * (l - i)
            return p / q
        
        for i in xrange(numRows):
            l1 = []
            for j in xrange(i+1):
                l1.append(func(i,j))
            l.append(l1)
        return l