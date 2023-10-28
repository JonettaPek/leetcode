"""
    Author: Pek, Jonetta
    Date: 23 May 2023
    Problem Description:
        Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

def contains_duplicate(numbers: list[int]) -> bool:
        unique = set()
        for number in numbers:
            if number in unique:
                return True
            unique.add(number)
        return False
