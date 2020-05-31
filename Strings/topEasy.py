from collections import defaultdict


def reverseString(chars):
    """
    Write a function that reverses a string. The input string is given as an array 
    of characters char[].

    Do not allocate extra space for another array, you must do this by modifying 
    the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.
    """
    p1 = 0
    p2 = len(chars) - 1

    while p1 < p2:
        chars[p1], chars[p2] = chars[p2], chars[p1]
        p1 += 1
        p2 -= 1

    return chars


def romanToInt(s):
    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, two is written as II in Roman numeral, just two one's added 
    together. Twelve is written as, XII, which is simply X + II. The number 
    twenty seven is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. 
    However, the numeral for four is not IIII. Instead, the number four is written 
    as IV. Because the one is before the five we subtract it making four. The same 
    principle applies to the number nine, which is written as IX. There are six 
    instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

    Given a roman numeral, convert it to an integer. Input is guaranteed to be 
    within the range from 1 to 3999.
    """

    count = 0
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    n = len(s)

    i = 0
    while i < n:
        if i == n-1:
            count += mapping[s[i]]
            i += 1
        else:
            if mapping[s[i]] < mapping[s[i+1]]:
                count += mapping[s[i+1]] - mapping[s[i]]
                i += 2
            else:
                count += mapping[s[i]]
                i += 1

    return count


def firstUnique(s):
    """
    Given a string, find the first non-repeating character in it and return it's 
    index. If it doesn't exist, return -1.
    """

    dic = defaultdict(int)

    for char in s:
        dic[char] += 1

    for i in range(len(s)):
        if dic[s[i]] == 1:
            return i

    return -1


def countAndSay(n):
    """
    The count-and-say sequence is the sequence of integers with the first five 
    terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say 
    sequence. You can do so recursively, in other words from the previous member 
    read off the digits, counting the number of digits in groups of the same digit.

    Note: Each term of the sequence of integers will be represented as a string.
    """

    if n == 1:
        return "1"

    prevMember = countAndSay(n - 1)

    # 2nd entry: "11"
    print(n-1, ": ", prevMember)
    curr = prevMember[0]  # "" prevMember[0]  # curr = "1"
    res = ""
    i = 1
    currCount = 1

    while i < len(prevMember):
        if curr == prevMember[i]:
            currCount += 1
        else:
            res += str(currCount) + prevMember[i-1]
            curr = prevMember[i]
            currCount = 1

        i += 1

    res += str(currCount) + prevMember[-1]
    return res


def countAndSay2(n):
    if n == 1:
        return "1"