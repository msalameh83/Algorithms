__author__ = 'Mohammad'

"""
You are given a set of n types of rectangular 3-D boxes, where the i^th box has height h(i),
width w(i) and depth d(i) (all real numbers). You want to create a stack of boxes which is
as tall as possible, but you can only stack a box on top of another box if the dimensions of
the 2-D base of the lower box are each strictly larger than those of the 2-D base of the
higher box. Of course, you can rotate a box so that any side functions as its base.
It is also allowable to use multiple instances of the same type of box.

The Box Stacking problem is a variation of LIS problem. We need to build a maximum height stack.

Following are the key points to note in the problem statement:
1) A box can be placed on top of another box only if both width and depth of the upper placed
box are smaller than width and depth of the lower box respectively.
2) We can rotate boxes. For example, if there is a box with dimensions {1x2x3} where 1 is
height, 2x3 is base, then there can be three possibilities, {1x2x3}, {2x1x3} and {3x1x2}.
3) We can use multiple instances of boxes. What it means is, we can have two different rotations
of a box as part of our maximum height stack.

Following is the solution based on DP solution of LIS problem.

1) Generate all 3 rotations of all boxes. The size of rotation array becomes 3 times the
size of original array. For simplicity, we consider depth as always smaller than or equal
to width.

2) Sort the above generated 3n boxes in decreasing order of base area.

3) After sorting the boxes, the problem is same as LIS with following optimal substructure property.
MSH(i) = Maximum possible Stack Height with box i at top of stack
MSH(i) = { Max ( MSH(j) ) + height(i) } where j < i and width(j) > width(i) and depth(j) > depth(i).
If there is no such j then MSH(i) = height(i)

4) To get overall maximum height, we return max(MSH(i)) where 0 < i < n

http://www.geeksforgeeks.org/dynamic-programming-set-21-box-stacking-problem/


boxes = [(1, 2, 4), (3, 2, 5)]
permutations = [[(1, 2, 4), (1, 4, 2), (2, 1, 4), (2, 4, 1), (4, 1, 2), (4, 2, 1)],
                [(3, 2, 5), (3, 5, 2), (2, 3, 5), (2, 5, 3), (5, 3, 2), (5, 2, 3)]]

filter l > w :
                [(2, 1, 4), (4, 1, 2), (4, 2, 1), (3, 2, 5), (5, 3, 2), (5, 2, 3)]

sort permutations on l x w :
                [(5, 3, 2), (5, 2, 3), (4, 2, 1), (3, 2, 5), (4, 1, 2), (2, 1, 4)]

LIS problem based on height
max_height = [2, 3, 1, 5, 2, 4]
result =     [0, 1, 2, 3, 4, 5]

i j  max_height         result
    [2, 3, 1, 5, 2, 4] [0, 1, 2, 3, 4, 5]
1 0 [2, 3, 1, 5, 2, 4] [0, 1, 2, 3, 4, 5]
2 0 [2, 3, 3, 5, 2, 4] [0, 1, 0, 3, 4, 5]
2 1 [2, 3, 3, 5, 2, 4] [0, 1, 0, 3, 4, 5]
3 0 [2, 3, 3, 7, 2, 4] [0, 1, 0, 0, 4, 5]
3 1 [2, 3, 3, 7, 2, 4] [0, 1, 0, 0, 4, 5]
3 2 [2, 3, 3, 7, 2, 4] [0, 1, 0, 0, 4, 5]
4 0 [2, 3, 3, 7, 4, 4] [0, 1, 0, 0, 0, 5]
4 1 [2, 3, 3, 7, 5, 4] [0, 1, 0, 0, 1, 5]
4 2 [2, 3, 3, 7, 5, 4] [0, 1, 0, 0, 1, 5]
4 3 [2, 3, 3, 7, 5, 4] [0, 1, 0, 0, 1, 5]
5 0 [2, 3, 3, 7, 5, 6] [0, 1, 0, 0, 1, 0]
5 1 [2, 3, 3, 7, 5, 7] [0, 1, 0, 0, 1, 1]
5 2 [2, 3, 3, 7, 5, 7] [0, 1, 0, 0, 1, 2]
5 3 [2, 3, 3, 7, 5, 11] [0, 1, 0, 0, 1, 3]
5 4 [2, 3, 3, 7, 5, 11] [0, 1, 0, 0, 1, 3]

"""

from itertools import permutations



def box_stacking(boxes):
    # get permutations of all boxes
    boxes = [list(permutations(box)) for box in boxes]
    # keep only ones where length > width
    boxes =[i for lst in boxes for i in lst if i[0]> i[1]]
    # sort based on area: length x width
    boxes.sort(key = lambda x:x[0]*x[1], reverse =True)

    # Longest increasing subsequence, max height is array initialized to heights
    # and result is initialized to indexes

    max_height = [box[2] for box in boxes]
    result = list(range(len(boxes)))
    for i in range(1, len(max_height)):
        for j in range(i):
            # can box[i] go on the top of box[j] such that length[i] < length[j] and width[i] < width[j]
            if boxes[i][0] <  boxes[j][0] and boxes[i][1] <  boxes[j][1]:
                max_height[i] = boxes[i][2] + max_height[j]
                result[i] = j
    print (max_height)
    print (result)



boxes = [(1, 2, 4), (3, 2, 5)]
box_stacking(boxes)
