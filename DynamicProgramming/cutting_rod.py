__author__ = 'Mohammad'

"""
Given a rod of length n inches and an array of prices that contains prices of all
pieces of size smaller than n. Determine the maximum value obtainable by cutting
up the rod and selling the pieces. For example, if length of the rod is 8 and the
values of different pieces are given as following, then the maximum obtainable
value is 22 (by cutting in two pieces of lengths 2 and 6)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
And if the prices are as following, then the maximum obtainable value is 24
(by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20

The naive solution for this problem is to generate all configurations of
different pieces and find the highest priced configuration. This solution
is exponential in term of time complexity. Let us see how this problem
possesses both important properties of a Dynamic Programming (DP)
Problem and can efficiently solved using Dynamic Programming.

1) Optimal Substructure:
We can get the best price by making a cut at different positions
and comparing the values obtained after a cut. We can recursively
call the same function for a piece obtained after a cut.

Let cutRoad(n) be the required (best possible price) value for a
rod of lenght n. cutRod(n) can be written as following.

cutRod(n) = max(price[i] + cutRod(n-i-1)) for all i in {0, 1 .. n-1}

2) Overlapping Subproblems
Following is simple recursive implementation of the Rod Cutting problem.
The implementation simply follows the recursive structure mentioned above.


GIVEN
rod_sz = 5
cuts_profit = [2, 5, 7, 8] for 1, 2, 3, 4 dimension

      1  2  3  4   5
  [0, 0, 0, 0, 0,  0 ]
2 [0, 2, 4, 6, 8,  10]
5 [0, 2, 5, 7, 10, 12]
7 [0, 2, 5, 7, 10, 12]
8 [0, 2, 5, 7, 10, 12]

"""
def cutting_rod_max_profit(rod_sz, cuts):
    chart = [ [0]*(rod_sz+1) for i in range(len(cuts)+1)]

    # for i in chart:print(i)

    for cut_sz in range(1,  len(chart)):
        for i in range(1, rod_sz+1):
            if i - cut_sz >= 0:
                chart[cut_sz][i] = max( chart[cut_sz-1][i] , cuts[cut_sz-1] + chart[cut_sz][i - cut_sz ])
            else:
                chart[cut_sz][i] = chart[cut_sz-1][i]

    for i in chart:print(i)






rod_sz = 5
cuts = [2, 5, 7, 8]
cutting_rod_max_profit(rod_sz, cuts)
