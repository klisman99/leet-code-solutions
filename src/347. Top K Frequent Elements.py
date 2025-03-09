class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        countBuckets = [[] for i in range(len(nums) + 1)]

        for freq, cnt in frequency.items():
            countBuckets[cnt].append(freq)

        res = []

        countBuckets.reverse()

        for items in countBuckets:
            for n in items:
                if len(res) < k:
                    res.append(n)

        return res