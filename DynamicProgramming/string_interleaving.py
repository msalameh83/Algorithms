__author__ = 'Mohammad'

"""
Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B.
C is said to be interleaving A and B, if it contains all characters of A and B and order of all
characters in individual strings is preserved.

We have discussed a simple solution of this problem here. The simple solution doesn't work if strings
A and B have some common characters. For example A = "XXY", string B = "XXZ" and string C = "XXZXXXY".
To handle all cases, two possibilities need to be considered.

a) If first character of C matches with first character of A, we move one character ahead in A and C
and recursively check.

b) If first character of C matches with first character of B, we move one character ahead in
B and C and recursively check.

If any of the above two cases is true, we return true, else false. Following is simple recursive
implementation of this approach

http://www.geeksforgeeks.org/check-whether-a-given-string-is-an-interleaving-of-two-other-given-strings-set-2/
https://www.youtube.com/watch?v=ih2OZ9-M3OM&index=29&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

          a      a      b
   [True, True, True, False]
a  [True, True, False, False]
x  [False, True, True, True]
y  [False, True, False, True]

if my pointer at aaxaby is at b and I am checking [2, 3],
then I check if b is equel to points at 2, 2 (i.e b or x)
Since it is equal to b, then aaax is an interleaving to aaxa( prefix of aaxab), so I look at its left[2, 2]

CHECK IF CORRECT
"""

def string_interleaving(str1, str2, str3):
    chart = [[False]* (len(str1)+1) for i in range(len(str2)+1)]


    if len(str1) + len(str2) != len(str3):
        return False

    for i in range(len(chart)):
        for j in range(len(chart[i])):
            l = i + j -1
            if i == 0 and j == 0:
                chart[i][j] = True
            elif i == 0:
                if str3[l] == str1[j-1]:
                    chart[i][j]  = chart[i][j - 1]
            elif j == 0:
                if str3[l] == str2[i-1]:
                    chart[i][j] = chart[i - 1][j]
            else:
                if str2[i-1] == str3[l] or str1[j-1] == str3[l]:
                    chart[i][j] = (chart[i - 1][j] or chart[i][j - 1])

    for i in chart: print(i)



str1='aab'
str2='axy'
str3= 'aaxaby'

string_interleaving(str1, str2, str3)