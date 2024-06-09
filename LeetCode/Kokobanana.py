from typing import List
import math

'''
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.
'''

'''
max(piles) --> rate = len(piles) --> min rate
1 <= k <= max(piles)
'''

def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    res = right
    while left <= right:
        rate = (left + right) // 2
        time = 0
        for pile in piles:
            time += math.ceil(pile / rate)
        if time > h:           
            left = rate + 1
        else:
            res = min(rate,res)
            right = rate - 1
    return res

print(minEatingSpeed([3,6,7,11], 8))
