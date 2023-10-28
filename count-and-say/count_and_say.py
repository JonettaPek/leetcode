"""
    Problem Description:
        To determine how you "say" a digit string, 
        split it into the minimal number of substrings such that each substring contains exactly one unique digit. 
        Then for each substring, say the number of digits, then say the digit. 
        Finally, concatenate every said digit.

        countAndSay(1) -> '1'
        countAndSay(2) -> '11'
        countAndSay(3) -> '21'
        countAndSay(4) -> '1211'
        countAndSay(5) -> '111221'
        countAndSay(6) -> '312211'
        countAndSay(7) -> '13112221'
"""


from collections import defaultdict


def cache(func):
    def wrapper(n):
        RESULTS = defaultdict(str)
        if RESULTS[n]:
            return RESULTS[n]
        RESULTS[n] = func(n)
        return RESULTS[n]
    return wrapper


@cache
def count_and_say(n: int) -> str:
    if n == 1:
        return '1'
    elif n == 2:
        return '11'

    return_string = '11'
    
    for _ in range(2,n):
        temp = []
        previous_char = return_string[0]
        occurrence = 1
        for index in range(1, len(return_string)):
            if previous_char != return_string[index]:
                temp.append(str(occurrence))
                temp.append(previous_char)
                previous_char = return_string[index]
                occurrence = 0
            occurrence += 1
        temp.append(str(occurrence))
        temp.append(previous_char)
        return_string = ''.join(temp)

    return return_string


if __name__ == '__main__':
    print(count_and_say(1))
    print(count_and_say(2))
    print(count_and_say(3))
    print(count_and_say(4))
    print(count_and_say(5))
    print(count_and_say(6))
    print(count_and_say(7))
    print(count_and_say(8))

