__author__ = 'Mohammad'


# Convert a number or string x to an integer, or return 0 if no arguments are given.
int('00100001', 2)  #33

int('0xff',16) #255

int('ff', 16) # 255

# convert to hex string:
"0x%x" % (int('00100001', 2))  # '0x21'


# character
chr(int('01011110',2)) # '^'
int('01000000',2) # 64
chr(int('01000000',2)) # '@'

int('01110100', 2) # 116
chr(int('01110100', 2)) # 't'
ord('t') # 116


print ('binary of     5       is %s' % bin(5))
print ('Right Shift   5 >> 1  is %s' % bin(5 >> 1))  # Right Shift
print ('Left Shift    5 << 1  is %s' % bin(5 << 1))  # Left Shift
print ('Bitwise AND   8 & 5   is %s' % bin(8 & 5) )  # Bitwise AND
print ('Bitwise OR    9 | 4   is %s' % bin(9 | 4))   # Bitwise OR
print ('Bitwise XOR   12 ^ 42 is %s' % bin(12 ^ 42) )# Bitwise XOR
print ('Bitwise NOT   ~8      is %s '% bin(~8))      # Bitwise NOT


def clearBit( x, kth ):
    """
    Given a bit sequence x, clear the kth bit; where the zeroth
    (0th) bit is the least significant (rightmost) bit.

    Sample Input:  0010010010  (integer representation of bit sequence)
    Sample Output: 0010010000 after clearing the 1st bit
    Technical Details:
    Let x = 0010010010. Then only the 1st, 4th, and 7th bits are set.
    Therefore, clearBit(x,1) would return 0010010000; whereas
    clearBit(x,3) would have no effect and so would return 0010010010.

    clearBit is a three steps operation:

    0] Using the shift-left operator <<, create a bit sequence
      where only the kth bit is set.
      00000001 << kth = 00000010

    1] Take the negation of the sequence in step_0. This effectively
      creates a sequence where all bits are set except the kth bit.
      negation 11111101

    2] Take the bitwise AND of x and the sequence in step_1. In digital
      logic a&1 is equal to 1 whereas a&0 is equal to 0. Therefore, this
      operation force clear the kth bit while leaving the other bits
      unchanged.
    """
    return x & ~(1 << kth)

def clearLowestBit( n ):
    """
    Clear the least significant (set) bit in the given sequence of bits.
    Sample Input:  1111111110 (integer representation of bit sequence )
    Sample Output: 1111111100 after clearing the lowest set bit
    Technical Details: When counting in binary, the difference
    between two cons cutive numbers (i.e. n and n-1) is twofold:
     1] The least significant set bit in the greater number
       is not set in the lesser number.
     2] All bits to the left of said least significant set bit
        are the same for both numbers.
    (7) 0000_0111,  (6) 0000_0110,  (5) 0000_0101,  (4) 0000_0100,
    (6) 0000_0110,  (5) 0000_0101,  (4) 0000_0100,  (3) 0000_0011.

     Hence, taking the bitwise AND of n and n-1 is sufficient for
     clearing the least significant bit.

    """
    return n & ( n - 1 )

def countBits(n):
    """
    Statement: Count the number of 1s in the given bit sequence
    Sample Input:  1000110010
    Sample Output: 4

    Technical Details: Numerous techniques have been devised to
    count the number of bits in a bit sequence. The simplest way
    to internalize why a given technique works is to take a
    pencil and run though a few examples.

    The presented approach runs through a loop and clears the
    lowest set bit of n during each iteration. When no set bit
    is left (i.e. n==0) the number of iterations is returned.

    0] Set count to 0
    1] while n > 0:
    -- clear the least significant bit in n: n &= (n-1)
    -- increment count by 1: count+=1
    2] return count.
    Alternate Algorithm: e.g. n = n & ~(n & ~(n-1));
    """
    count = 0
    while n != 0:
        n &= ( n - 1 )
        count += 1
    return count


def findOddSingleton( a ):
    """
    Statement:
    Given a list where all values occur an even number of times;
    except for one value, which occurs an odd number of times and which
    we shall call a singleton; find the singleton.

    Sample Input: 1,2,7,3,4,5,7,6,7,4,2,6,3,1,5
    Sample Output: 7

    Technical Details:
    The most efficient approach is to XOR all the elements of the list
    and return the result. Recall from digital logic the following
    truths about the XOR (^) operator: x^x = 0; 0^x = x.
    """
    i = a[0]
    for n in range(1, len(a)):
        i ^= a[n]
    return i

def singleNumber(x):
    """
    Given an array of integers, every element appears three times except for one. Find that single one.
    explanation:
    ones - At any point of time, this variable holds XOR of all the elements which have appeared "only" once.
    twos - At any point of time, this variable holds XOR of all the elements which have appeared "only" twice.
    https://www.careercup.com/question?id=15066700

    """
    ones = 0
    twos = 0
    threes = 0
    for i in range(len(x)):
        twos |= ones & x[i]
        ones ^= x[i]
        threes = ones & twos
        ones &= ~threes
        twos &= ~threes
    return ones


print (singleNumber([1, 1, 2, 3,1,  3, 3]))

def intersection( x, y ):
    """
    # Statement:
    Given two sets of bits, x and y, find their intersection.

    Sample Input: 0101100 and 0110101
    Sample Output: 0100100

    Technical Details:
    The intersection of two sets is the subset comprising only the
    elements that appear in both sets. For example if s1 = [a,b,f,h,k]
    and s2 = [b,c,d,f,h,i] then the intersection of s1 and s2 is
    [b,f,h]. For two sets of bits the intersection is simply the bitwise
    AND of the two sets. For example if x = 0110101 and y=0101100 then
    the intersection of x and y is x U y = 0100100.
    """
    return x & y



def isEven( x ):
    """
    Statement: Indicate whether the given integer is even.
    Sample Input: 28
    Sample Output: true
    Technical Details: The lowest bit of an even number is 0.
    0 = 0; 2 = 10; 4 = 100; 6 = 110; 8 = 1000; etc.
    Therefore, x AND 1 should be 0 for all even numbers.
    """
    return ( x & 1 ) == 0

def isOdd( x ):
    return (x & 1) == 1





def isPowerOfTwo( n ):
    """
    Statement: Indicate whether the given integer n is a power of two.
    Sample Input:  16
    Sample Output: true
    Technical Details:
    A number that is a power of two only has one set bit: 0 = 0; 2 = 10;
    4 = 100; 8 = 1000; 16 = 10000; etc. Therefore checking whether a
    number is a power of two is as simple as clearing the lowest set bit
    and then checking that the result is equal to zero.
    """
    return (n & (n - 1)) == 0

def MSB( n ):
    """
    Statement:
      Given a bit sequence, indicate the index of the most significant
      set bit, where the index of the least significant bit is zero.

    Sample Input:  00110101
    Sample Output: 5

    Time Complexity of Solution:
      Best = Average = Worst = O(lg n).

    Technical Details:
      The MSB algorithm is as simple as algorithms comes. Basically,
      you continually shift the sequence of bit to the right until
      you reach the last set bit. Let's run through the above example:

      0] 00110101  Given
      1]  0011010  After dropping the 0th right-most bit
      2]   001101  After dropping the 1st right-most bit
      3]    00110  After dropping the 2nd right-most bit
      4]     0011  After dropping the 3rd right-most bit
      5]      001  After dropping the 4th right-most bit

      At step 5] we are at the 5th and last set bit.

      As it turns out MSB(n) is the eger portion of log2(n). So
      to find the log base two of n, just shift right until one bit is
      left.     """
    ndx = 0
    while ( 1 < n ):
        n = ( n >> 1 )
        ndx += 1
    return ndx



def reverseBitsOfInt( x ):
    """
    Statement: Given an integer, reverse its bit sequence.
    Sample Input:  00000000000000001111111111111110
    Sample Output: 01111111111111110000000000000000
    """
    size = 32
    y = 0
    position = size - 1
    while position > 0:
        y += ( ( x & 1 ) << position )
        x >>= 1
        position -= 1
    return y


def subtraction( x, y ) :
    """
    Statement:
    Given two sets of bits, x and y, find their difference.

    Sample Input:  0010010010
    Sample Output: 0010010011

    Technical Details: The subtraction of two sets is the subset
    comprising the elements that appear in the minuend x and not in the
    subtrahend y. For example if s1 = [a,b,f,h,k] and s2 = [b,c,d,f,h,i]
    then the subtraction of s1 and s2 is [a,k]. For two sets of bits the
    subtraction is a two steps process. First, the negative of the
    second set is calculated. Then the bitwise AND of the result and the
    first set is taken. For example if x = 0110101 and y=0101100 then
    the subtraction of x and y follows:

    step_1: z = negative y = ~y = 1010011.
    step_2: x AND z = x & z = x & (~y) = 0010001
    """
    return x & ~y



def setBit( x, kth ):
    """
    Statement:
    Given a bit sequence x, set the kth bit; where the zeroth (0th) bit
    is the least significant (rightmost) bit.

    Sample Input:  0010010010
    Sample Output: 0010010011

    Description:

    Technical Details: Let x = 0010010010. Then only the 1st, 4th,
    and the 7th bits are set. The function setBit(x,0) would
    return 0010010011.

    setBit is a two steps operation:
    step_1] Using the shift-left operator << create a bit
           sequence where only the kth bit is set.
    step_2] Take the bitwise OR of x and the sequence in step_1.
    """
    return x | ( 1 << kth )

def negation( x ):
    """
    Statement:
      Given a set of bits, x, find its negation.

    Sample Input:  0101100
    Sample Output: 1010011

    Technical Details:
      The negation of a set x is the set comprising all the elements in
      the universe that are not in x. For example if the context is all
      the ciphers in the decimal system and s1 = [0,2,5,8] then the
      negation of s1 is [1,3,4,6,7,9]. For a set of bits the negation is
      simply the bitwise NOT of the set. For example if x = 0110101 then
      the negation of x is 1001010.

    Alternate Algorithm:
      The negation of a set of bits x may also be calculated as
      ALL_BITS ^ x, where ^ is the bitwise XOR operator. For example,
      if x = 0110101 then perforce ALL_BITS = 1111111. Hence,
      negative x = 1111111^0110101=1001010
    """
    u = int( "1111111111111111", 2 )
    return u ^ x # or return ~x

def union( x, y ):
    """
    Statement:
      Given two sets of bits, x and y, find their union.

    Sample Input:  0110101; 0101100
    Sample Output: 0111101

    Technical Details:
      The union of two sets is the superset comprising all the elements
      that appear in both sets. For example if s1 = [a,b,f,h,k] and
      s2 = [b,c,d,f,h,position] then the union of s1 and s2 is
      s1 U s2 = [a,b,c,d,f,h,position,k]. For two sets of bits the union
      is simply the bitwise OR of the two sets. For example if x = 0110101
      and y=0101100 then the union of x and y is x U y = 0111101.
    """

    return x | y




def testBit( x, kth ):
    """
    Statement:
      Given a bit sequence, indicate whether the kth bit is set.
      The zeroth (0th) bit is the least significant
       (rightmost) bit.
    Sample Input:  0010010010, 4
    Sample Output: true

    Technical Details: Let x = 0010010010. Then only the 1st, 4th,
       and the 7th bits are set. Therefore, testBit(x,4) would return
       TRUE while testBit(x,2) would return FALSE.

        testBit is a three steps operation:
        step_1] Using the shift-left operator << create a bit
            sequence where only the kth bit is set.
        step_2] Take the bitwise AND of x and the sequence in step_1.
            This operation will force clear all the bits in x; except
            the kth bit. It leaves the kth bit unchanged.
        step_3] Compare the result of step_2 to zero (0). This step
             is effectively comparing the kth bit to zero.
    """

    return ( x & 1 << kth ) != 0


import struct
def findOddFloatSingleton( a ):
    """
    Statement:
      Given an array of floating point numbers where all values occur an
      even number of times; except for one value, which occurs an odd
      number of times and which we shall call a singleton; find the
      singleton.

    Sample Input: fArr = [1.2, 7.340, 2.3, 3.34, 7.340, 4.567,
                          5.65, 6.234, 7.340, 4.567, 7.340, 2.3,
                          6.234, 7.340, 3.34, 1.2, 5.65]
    Sample Output: 7.340

    Technical Details:
      The most efficient approach is to XOR all the elements of the array
      and return the result. Recall from digital logic the following truths
      about the XOR (^) operator: x^x = 0; 0^x = x.
      (Ref http://www.teahlab.com/basicGates/xorgate).

      However, there is still one problem: Python does not define bitwise
      operations for float. Therefore, the following steps are followed to
      find the singleton:
        0] Convert each floating point number to virtual
           bits using floatToBits(f), which we also define.
        1] Perform XOR operation on the values while in virtual bits form.
        2] Convert the final bits result to float using bitsToFloat( i ).
        3] Return the final float value.
      """

    def floatToBits( n ):
        value = struct.pack( '>f', n )
        return struct.unpack( '>l', value )[0]

    def bitsToFloat( n ):
        value = struct.pack( '>l', n )
        return struct.unpack( '>f', value )[0]

    b = floatToBits( a[0] )
    for n in range( 1, len( a ) ):
        b ^= floatToBits( a[n] )
    return bitsToFloat( b )




def powerSet( aList ):
    """
    Statement:
      Given a set of objects (e.g. characters), find the power set.

    Sample Input:  [a,b,c]
    Sample Output: [[a,b,c],[a,b],[a,c],[a],[b,c],[b],[c],[]]

    Technical Details:
      This solution is one of the most powerful and most elegant results
      of bitwise operations. To find the powerset of any set of size n,
      simply start with an ALL_BITS number of size n and count down:
      [a,b,c],[a,b  ], [a,  c],[a    ],[  b,c],[  b  ],[    c],[     ]
       1 1 1 , 1 1 0 ,  1 0 1 , 1 0 0 , 0 1 1 , 0 1 0 , 0 0 1 , 0 0 0.
    """

    # return None if set is None or empty
    if ( aList is None or len( aList.strip() ) == 0 ):
        return None

    powset = []
    length = len( aList )
    bits = "1"*length

    # extract power set by counting down in 'binary'
    b = int( bits, 2 )
    while b >= 0:
        # get bit representation of new subset
        bits = bin( b )
        bits = bits[2:] # to remove the 0b appearing at 0b111
        subset = "" # empty subset holder

        # Python drops leading 0s so that if 7==111, then 3 != 011 but 3==11
        k = length - len( bits )
        for c in bits: # assemble subset from bits
            if '1' == c:
                subset += aList[k]
            k += 1
        b -= 1

        powset.append( subset ) # add subset to power set

    return powset

print (powerSet('abc'))


def rangeBitwiseAnd(m, n):
    """
    Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
    of all numbers in this range, inclusive. For example, given the range [5, 7],
    you should return 4. Java

    The key to solve this problem is bitwise AND consecutive numbers. You can use
    the following example to walk through the code.
    The problem is all about finding the longest common sequence between n and m
    starting from the most significant bit, since all the following bits will flip
    for at least once and the AND result will be 0.
    """
    while n > m:
        n = n &  (n - 1)
    return m & n
