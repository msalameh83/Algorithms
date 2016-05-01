__author__ = 'Mohammad'

"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence
present in both of them. A subsequence is a sequence that appears in the same relative
order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”
, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different possible subsequences.

It is a classic computer science problem, the basis of diff (a file comparison program
that outputs the differences between two files), and has applications in bioinformatics.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.


https://www.youtube.com/watch?v=NnD96abizww&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=2

OUTPUT:
      a, b, c, d, e, f
  [0, 0, 0, 0, 0, 0, 0],
a [0, 1, 1, 1, 1, 1, 1],
c [0, 1, 1, 2, 2, 2, 2],
b [0, 1, 2, 2, 2, 2, 2],
c [0, 1, 2, 3, 3, 3, 3],
f [0, 1, 2, 3, 3, 3, 4]
Longest Commons Subsequence is 4
Longest Commons Subsequence String is ['a', 'b', 'c', 'f']

if char are equal then diagonal + 1
else, max (up , left)

Time Complexity of the above implementation is O(mn)

"""

import pprint


def lcs(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    chart = [[0] * (len_str1 + 1) for i in range(len_str2 + 1)]

    for i in range(1, len(chart)):
        for j in range(1, len(chart[i])):
            if str2[i - 1] == str1[j - 1]:
                chart[i][j] = 1 + chart[i - 1][j - 1]
            else:
                chart[i][j] = max(chart[i - 1][j], chart[i][j - 1])
                # print (chart[i])
    pprint.pprint(chart)

    print('Longest Commons Subsequence is %i' % chart[-1][-1])

    i = len_str2
    j = len_str1
    lcs_str = []
    while i > 0 and j > 0:
        if str1[j - 1] == str2[i - 1]:
            i -= 1
            j -= 1
            lcs_str.insert(0, str1[j])
        elif chart[i][j] == chart[i - 1][j]:
            i -= 1
        else:
            j -= 1

    print('Longest Commons Subsequence String is %s' % lcs_str)


def lcs_rec(str1, str2, len1, len2):
    if len1 == len(str1) or len2 == len(str2):
        return 0
    if str1[len1] == str2[len2]:
        return 1 + lcs_rec(str1, str2, len1 + 1, len2 + 1)
    else:
        return max(lcs_rec(str1, str2, len1 + 1, len2), lcs_rec(str1, str2, len1, len2 + 1))


str1 = 'abcdaf'
str2 = 'acbcf'

s = lcs(str1, str2)
s = lcs_rec(str1, str2, 0, 0)
print(s)
