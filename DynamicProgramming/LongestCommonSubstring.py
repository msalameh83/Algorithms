__author__ = 'Mohammad'


def LongestCommonSubstring(str1,str2):
    len_str1=len(str1)
    len_str2=len(str2)

    chart=[[0]*(len_str1+1) for i in range(len_str2+1)]
    # for i in chart: print (i)
    max=0; i_max=0; j_max=0
    for i in range(1,len(chart)):
        for j in range(1,len(chart[i])):
            if str2[i-1]==str1[j-1]:
                chart[i][j]=chart[i-1][j-1]+1
                if chart[i][j] > max:
                    max= chart[i][j]; i_max=i; j_max=j;

    for i in chart: print (i)
    print (max,i_max, j_max)

    lcs=str2[i_max-max:i_max]
    print (lcs)







str1='abcdaf'
str2='zbcdf'



str1='abcdafnpqrste'
str2='zbcdfmpqrstw'

LongestCommonSubstring(str1,str2)