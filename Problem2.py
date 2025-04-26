"""
Problem: Top K Frequent Elements

Given a non-empty list of integers nums, return the k most frequent elements.
You may return the answer in any order.
⸻
Function Signature:
def top_k_frequent(nums: list[int], k: int) -> list[int]:
⸻
Input:
	•	nums: List of integers with length n (1 ≤ n ≤ 10⁵)
	•	k: Integer (1 ≤ k ≤ number of unique elements in nums)
⸻
Output:
	•	A list of k integers representing the most frequent elements.
	•	The answer can be in any order.
⸻
Example:

Example 1:

Input: nums = [1, 1, 1, 2, 2, 3], k = 2  
Output: [1, 2]

Example 2:

Input: nums = [1], k = 1  
Output: [1]

Example 3:

Input: nums = [4, 4, 4, 6, 6, 5, 5, 5, 7], k = 3  
Output: [4, 5, 6]  # or any permutation
⸻
Constraints:
	•	Time complexity must be better than O(n log n) — ideally O(n log k) or O(n).
	•	The output order does not matter unless specified.
⸻
Can you solve it in linear time O(n)?
"""
    
from collections import Counter
import heapq


# The below code will work in O(NLogK) where the N is the number of elements in the nums list
# K is the value provided in the input

# def top_k_frequent(nums: list[int], k: int) -> list[int]:
#     freq_map = Counter(nums)
#     min_heap = []

#     for num, freq in freq_map.items():
#         heapq.heappush(min_heap, (freq, num))
#         if len(min_heap) > k:
#             heapq.heappop(min_heap)
    
#     return [num for _, num in min_heap]


# Below code will work in O(N) as we are creating the bucket for each frequency
# Frequency can be max len(nums)

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq_map = Counter(nums)
    bucket = [[] for _ in range(len(nums) + 1)]

    for num, freq in freq_map.items():
        bucket[freq].append(num)

    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            res.append(num)
            if len(res) == k:
                return res

    
if __name__ == "__main__":
    print(top_k_frequent(nums = [4, 4, 4, 6, 6, 5, 5, 5, 7], k = 3))
    print(top_k_frequent(nums = [1, 1, 1, 2, 2, 3], k = 2))
    print(top_k_frequent(nums = [1], k = 1))
