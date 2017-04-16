#Heap
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        return heapq.nlargest(k, nums)[-1]

#Quckselect (https://en.wikipedia.org/wiki/Quickselect)
"""
 function partition(list, left, right, pivotIndex)
     pivotValue := list[pivotIndex]
     swap list[pivotIndex] and list[right]  // Move pivot to end
     storeIndex := left
     for i from left to right-1
         if list[i] < pivotValue
             swap list[storeIndex] and list[i]
             increment storeIndex
     swap list[right] and list[storeIndex]  // Move pivot to its final place
     return storeIndex

  // Returns the k-th smallest element of list within left..right inclusive
  // (i.e. left <= k <= right).
  // The search space within the array is changing for each round - but the list
  // is still the same size. Thus, k does not need to be updated with each round.
  function select(list, left, right, k)
     if left = right        // If the list contains only one element,
         return list[left]  // return that element
     pivotIndex  := ...     // select a pivotIndex between left and right,
                            // e.g., left + floor(rand() % (right - left + 1))
     pivotIndex  := partition(list, left, right, pivotIndex)
     // The pivot is in its final sorted position
     if k = pivotIndex
         return list[k]
     else if k < pivotIndex
         return select(list, left, pivotIndex - 1, k)
     else
         return select(list, pivotIndex + 1, right, k)
"""
"""
In quick select, pivot_index is in its final sorted position
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from random import randint
        def partition(nums, left, right, pivot_index):
            pivot_value = nums[pivot_index]
            #move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left
            for i in range(left, right):
                if nums[i] > pivot_value:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            #move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def select(nums, left, right, k):
            #if the list contains only one element
            if left == right:
                return nums[left]
            pivot_index = randint(left, right)
            pivot_index = partition(nums, left, right, pivot_index)
            if k == pivot_index:
                return nums[k]
            elif k < pivot_index:
                return select(nums, left, pivot_index-1, k)
            else:
                return select(nums, pivot_index+1, right, k)
        r = select(nums, 0, len(nums)-1, k-1)
        return r


nums = [3, 2 ,1, 5, 6, 4]
k = 2
r = Solution().findKthLargest(nums, k)
print(r)