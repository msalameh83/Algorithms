__author__ = 'Mohammad'
"""
Problem:
Given certain number of floor and certain number of eggs, how many attempts do we need to know
in the worst case from which floor the egg will break

Examples:
Given 1 egg adn 10 floors, we need 10 attemps in the worst case. I can start witht he frst floor,
then 2nd, 3rd, ... until the egg breaks

Given 2 eggs and 10 floors, I can start with floor 4.
If it breaks then I have 3 floors and 1 egg to work with: floors 1, 2, and 3
if it did not, then I have 6 floors and 2 eggs to work with: floors 6, 7, 8, 9, and 10

Given 2 eggs and 6 floors:

       f  l  o  o  o  r
egg 1 [1, 2, 3, 4, 5, 6]
egg 2 [1, 2, 2, 3, 3, 3]


T[2][4]=3  means I have 2 eggs and I start at floor 4
If I start from first floor and drop an egg and egg breaks, the I found the answer:  1+max (0 ,??? )
else: I have 3 floors and 2 eggs to work with ,   1+ max (0, T[2][3])  = 1+ max(0,2) = 3

If I drop from 2nd floor, and egg breaks, then I have 1 floor to work with and 1 egg: 1+max(T[1][1], ???)
else: I have 2 floors and 2 eggs to work with:  1+max(T[1][1], T[2,2]) = 1+ max (1, 2) =3

from 3rd floor:  1+max(T[1][2], T[2][1]) = 1+ max (2, 1) =3
from 4rd floor:  1+max(T[1][3], T[2][0]) = 1+ max (3, 0) =4


Minimum (3,3,3,4)=3 is minimum number of attempts in the worst case

"""
import sys
from pprint import pprint

def edp(eggs, floors):
    chart =[[0]* (floors+1) for i in range(eggs+1)]
    chart[1] = list(range(floors+1))

    for egg in range(2,eggs+1):
        for floor in range(1, floors+1):
            chart[egg][floor]=sys.maxsize
            for k in range(1,floor+1):
                c = 1 + max(chart[egg-1][k-1],chart[egg][floor-k ])
                if c < chart[egg][floor]:
                    chart[egg][floor] = c

    pprint (chart)
    print ('min number of attemspts is %i'%chart[eggs][ floors])


def edp_rec(eggs, floors):
    if eggs==1: return floors
    if floors==0: return 0

    minimum =1000
    for k in range(1,floors+1):
        c = 1 + max(edp_rec(eggs-1,k-1),edp_rec(eggs,floors-k ))
        if c < minimum: minimum=c
    return minimum



eggs=2
floors=6
edp(eggs, floors)
a=edp_rec(eggs, floors)
print(a)




