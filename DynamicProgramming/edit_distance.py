__author__ = 'Mohammad'


"""
Minimum Edit distance between two strings str1 and str2 is defined as the minimum
number of insert/delete/substitute operations required to transform str1 into str2.
For example if str1 = "ab", str2 = "abc" then making an insert operation of
character 'c' on str1 transforms str1 into str2. Therefore, edit distance between
str1 and str2 is 1. You can also calculate edit distance as number of operations
required to transform str2 into str1. For above example, if we perform a delete
operation of character 'c' on str2, it is transformed into str1 resulting in same edit distance of 1.

Looking at another example, if str1 = "INTENTION" and str2 = "EXECUTION", then the
minimum edit distance between str1 and str2 turns out to be 5 as shown below.
All operations are performed on str1.

      a  b  c  d  e  f
  [0, 1, 2, 3, 4, 5, 6]
a [1, 0, 1, 2, 3, 4, 5]
z [2, 1, 1, 2, 3, 4, 5]
c [3, 2, 2, 1, 2, 3, 4]
e [4, 3, 3, 2, 2, 2, 3]
d [5, 4, 4, 3, 2, 3, 3]
5 6
Edit f in string1 to d in string2
Keep e
Delete in string1 d
Keep c
Edit b in string1 to z in string2
Keep a


when printing, if current value is due to the one on the left + 1
then delete column character

Time Complexity is O(mn)
Space Complexity is O(mn)


"""


def min_edit_distance(str1, str2):
    chart = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    for i in range(len(str2)+1):chart[i][0] = i
    for i in range(len(str1)+1):chart[0][i] = i
    # for i in chart:print(i)

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                chart[i][j] = chart[i-1][j-1]
            else:
                chart[i][j]  = 1 + min(chart[i-1][j-1],  chart[i-1][j], chart[i][j-1])

    for i in chart: print (i)
    print_edits(chart, str1, str2)

def print_edits(chart, str1, str2):
    i = len(chart) - 1
    j = len(chart[0]) - 1
    print(i, j)
    while True:
        if i== 0 or j ==0:break

        if str2[i-1] == str1[j-1]:
            print("Keep %s"%str2[i-1])
            i -= 1
            j -= 1

        elif chart[i][j] == 1 + chart[i-1][j-1]:
            print("Edit " + str1[j-1] + " in string1 to " + str2[i-1] + " in string2")
            i -= 1
            j -= 1



        elif chart[i][j] == 1 + chart[i-1][j]:
            print("Delete in string2 %s" % str2[i-1])
            i -= 1
        elif chart[i][j] == 1 + chart[i][j-1]:
            print("Delete in string1 %s" % str1[j-1])
            j -= 1

        else:
            print("ERROR")




str1 = list('abcdef')
str2 = list('azced')
min_edit_distance(str1, str2)
