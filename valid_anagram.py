"""
Author: Pek, Jonetta
Date: 23 May 2023
Problem Description: 

        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

        Example 1:

        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.

        Example 2:

        Input: s = "cbbd"
        Output: "bb"
"""


def count_letters(word: str) -> dict:
    letter_count = dict()
    for letter in word:
        if letter in letter_count:
            letter_count[letter] = letter_count[letter] + 1
        else:
            letter_count[letter] = 1
    return letter_count


def is_anagram(first_word: str, second_word: str) -> bool:
    return True if count_letters(first_word) == count_letters(second_word) else False


def construct_reply(word_one: str, word_two: str, anagramic: bool) -> str:
    sentence = f'The words, {word_one} and {word_two}, are '
    return sentence + 'anagrams.' if anagramic else sentence + 'are not an anagrams.'



if __name__ == '__main__':
    print('To check if two words are anagrams of each other, please enter one word after another:')
    input_one: str = input('1: ')
    input_two: str = input('2: ')
    print(construct_reply(input_one, input_two, is_anagram(input_one.lower(), input_two.lower())))
