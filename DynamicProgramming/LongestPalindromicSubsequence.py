__author__ = 'Mohammad'
"""
find the longest palndromic subsequence in a string:

string= a g b d b a
Soluton:  a b d b a
"""


def lps(string):
    str_len=len(string)

    chart=[[0]*(str_len + 1) for i in range(str_len+1)]
    for i in range(str_len+1):
        chart[1][i]=1

    for c in range(2, str_len):
        for i in range(1, str_len):
            if(string[i-1] == string[i-1 + c-1] and c == 2):
                chart[c][i] = 2;
            elif(string[i-1] == string[i+c-2]):
                chart[c][i] = chart[c-2][i+1] + 2
            else:
                chart[c][i] = max(chart[c-1][i+1], chart[c-1][i])


    print(chart)


string='agbdba'
lps(string)



