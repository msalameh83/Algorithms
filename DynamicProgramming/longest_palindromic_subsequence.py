__author__ = 'Mohammad'
"""
find the longest palndromic subsequence in a string:

string= a g b d b a
Soluton:  a b d b a

https://www.youtube.com/watch?v=_nCsPn7_OgI&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=9


first loop:
what is the lps if I consider 1 character:
 it is all 1

for length = 2
what is the lsp for ag, gb, bd, db, ba ?

for length = 3
what is the lsp for agb, gbd, bdb, dba?
for agb, since a != b , then it's the lsp is the max of ag and gb

for bdb, since b = b ,  then it's the lsp is 2 + lsp(d)




"""


def lps(string):
    str_len=len(string)

    chart=[[0]*(str_len) for i in range(str_len)]

    # what is the lps if i consider 1 character
    for i in range(str_len):
        chart[i][i] = 1


    for span in range(2, str_len + 1):
        for i in range(str_len - span + 1):
            j = i + span -1
            if string[i] == string[j] and span == 2:
                chart[i][j] = 2
            elif string[i] == string[j]:
                chart[i][j] = chart[i+1][j-1] + 2
            else:
                chart[i][j] = max(chart[i + 1][j], chart[i][j - 1])


    for i in chart: print(i)

def lps_rec(string, start, length):
    if length == 1:
        return 1
    if length == 0:
        return 0
    if string[start] == string[start + length -1]:
        return 2 + lps_rec(string, start + 1, length - 2)
    else:
        return max(lps_rec(string, start + 1, length - 1) , lps_rec(string, start , length - 1))



string='agbdba'
lps(string)
print(lps_rec(string, 0, len(string)))

