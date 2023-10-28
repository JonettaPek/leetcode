"""
    Problem Description:
        To determine how you "say" a digit string, 
        split it into the minimal number of substrings such that each substring contains exactly one unique digit. 
        Then for each substring, say the number of digits, then say the digit. 
        Finally, concatenate every said digit.
"""


from collections import defaultdict


def cache(func):
    def wrapper(self, n):
        RESULTS = defaultdict(str)
        if RESULTS[n]:
            return RESULTS[n]
        RESULTS[n] = func(self, n)
        return RESULTS[n]
    return wrapper

@cache
def countAndSay(n: int) -> str:
    '''
        countAndSay(1) -> '1'
        countAndSay(2) -> '11'
        countAndSay(3) -> '21'
        countAndSay(4) -> '1211'
        countAndSay(5) -> '111221'
        countAndSay(6) -> '312211'
        countAndSay(7) -> '13112221'
    '''
    if n == 1:
        return '1'
    elif n == 2:
        return '11'

    returnString = '11'
    
    for _ in range(2,n):
        temp = []
        prevChar = returnString[0]
        occurrence = 1
        for index in range(1, len(returnString)):
            if prevChar != returnString[index]:
                temp.append(str(occurrence))
                temp.append(prevChar)
                prevChar = returnString[index]
                occurrence = 0
            occurrence += 1
        temp.append(str(occurrence))
        temp.append(prevChar)
        returnString = ''.join(temp)

    return returnString
