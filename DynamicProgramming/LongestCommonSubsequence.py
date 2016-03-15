__author__ = 'Mohammad'

import pprint

def lcs(str1,str2):
    len_str1=len(str1)
    len_str2=len(str2)
    chart=[ [0]*(len_str1+1) for i in range(len_str2+1)]

    for i in range (1,len(chart)):
        for j in range (1, len(chart[i])):
            if str2[i-1]==str1[j-1]:
                chart[i][j]=1+chart[i-1][j-1]
            else:
                chart[i][j]=max(chart[i-1][j], chart[i][j-1])
        # print (chart[i])
    pprint.pprint (chart)

    print ('Longest Commons Subsequence is %i'%chart[-1][-1])

    i=len_str2
    j=len_str1
    lcs_str=[]
    while i > 0  and j > 0 :
        if str1[j-1]==str2[i-1]:
            i-=1
            j-=1
            lcs_str.insert (0,str1[j])
        elif chart[i][j]==chart[i-1][j]:
            i-=1
        else:
            j-=1

    print ('Longest Commons Subsequence String is %s' % lcs_str)

str1='abcdaf'
str2='acbcf'

lcs(str1,str2)


# OUTPUT:
#
# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 1, 1, 1],
#  [0, 1, 1, 2, 2, 2, 2],
#  [0, 1, 2, 2, 2, 2, 2],
#  [0, 1, 2, 3, 3, 3, 3],
#  [0, 1, 2, 3, 3, 3, 4]]
# Longest Commons Subsequence is 4
# Longest Commons Subsequence String is ['a', 'b', 'c', 'f']