#Hashtable
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        m = defaultdict(int)
        l = len(nums)
        for n in nums:
            m[n] += 1
            if m[n] > l // 2:
                return n

#Sort
"""
Since the marjority element appears more than n/2 times, 
the n/2-th element in sorted nums must be majority element.

result is the n/2 th element in nums

beg,end of majority element
beg + n / 2 < n
beg < n / 2

beg > 0
end > beg + n/2 > n/2
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]

#Randomization
"""
pick a element and see if it is the majority
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from random import randint
        l = len(nums)
        while True:
            i = randint(0, l-1)
            candidate = nums[i]
            print(candidate)
            count = 0
            for n in nums:
                if n == candidate:
                    count += 1
            if count > l // 2:
                return candidate
#Divide and Conquer
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def majority(nums, left, right):
            if left == right:
                return nums[left]
            mid = (left+right)//2
            lm = majority(nums, left, mid)
            rm = majority(nums, mid+1, right)
            if lm == rm:
                return lm
            a = nums[left:mid+1].count(lm)
            b = nums[mid+1:right+1].count(rm)
            return lm if a > b else rm
        return majority(nums, 0, len(nums)-1)

#Boyer-Moore majority vote algorithm (https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
"""
The algorithm maintains in its local variables a sequence element 
and a counter, with the counter initially zero. 
It then processes the elements of the sequence, one at a time. 
When processing an element x, if the counter is zero, 
the algorithm stores x as its remembered sequence element and
sets the counter to one. 
Otherwise, it compares x to the stored element 
and either increments the counter (if they are equal) 
or decrements the counter (otherwise). 
At the end of this process, if the sequence has a majority, 
it will be the element stored by the algorithm. 
This can be expressed in pseudocode as the following steps:

Initialize an element m and a counter i with i = 0
For each element x of the input sequence:
    If i = 0, then assign m = x and i = 1
    else if m = x, then assign i = i + 1
    else assign i = i − 1
Return m

Even when the input sequence has no majority, the algorithm will report one of the sequence elements as its result. However, it is possible to perform a second pass over the same input sequence in order to count the number of times the reported element occurs and determine whether it is actually a majority. This second pass is needed, as it is not possible for a sublinear-space algorithm to determine whether there exists a majority element in a single pass through the input.[3]
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major, counts = 0, 0
        for n in nums:
            if not counts:
                major = n
                counts = 1
            else:
                if n == major:
                    counts += 1
                else:
                    counts -= 1
            print(n, major, counts)
        return major

#Bit Manipulation
"""
class Solution(object):
    def majorityElement(self, nums):
        major = 0
        mask = 1
        for i in range(32):
            bit_counts = 0
            for n in nums:
                if n & mask:
                    bit_counts += 1
                if bit_counts > len(nums)//2:
                    major |= mask
                    break
            mask <<= 1
        return major
"""

t = [3,3,4]
r = Solution().majorityElement(t)
print(r)