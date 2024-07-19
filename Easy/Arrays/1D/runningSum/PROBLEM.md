# Problem: Running Sum of 1D Array

## Problem Statement

Given an array `nums`, we are tasked with calculating the **running sum** of the array. The running sum of an array is defined as:

`runningSum[i] = sum(nums[0]…nums[i])`

Where each element at index `i` is the sum of the elements from the start of the array up to the current index `i`. Our task is to return an array that represents the running sum for each element in the input array.

### Example:

#### Input:

`nums = [1, 2, 3, 4]`

#### Output:

`[1, 3, 6, 10]`

**Explanation:**

- The running sum at index `0` is `1`.
- The running sum at index `1` is `1 + 2 = 3`.
- The running sum at index `2` is `1 + 2 + 3 = 6`.
- The running sum at index `3` is `1 + 2 + 3 + 4 = 10`.

Thus, the output is `[1, 3, 6, 10]`.

---

## Approach

The approach to solving this problem involves updating the input array `nums` in-place. This means we will modify each element at index `i` by adding the previous element (at index `i - 1`) to it. We start this process from the second element (i.e., index `1`), because the first element remains unchanged.

### Steps Involved:

1. Iterate through the array starting from index `1` up to the last element of the array.
2. For each element at index `i`, add the previous element `nums[i - 1]` to the current element `nums[i]`.
3. Continue this process for all elements in the array.
4. Return the modified array, which now contains the running sum.

---

## Code

```python
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Start iterating from index 1
        for i in range(1, len(nums)):
            # Update the current element with the sum of the current and previous element
            nums[i] = nums[i-1] + nums[i]

        # Return the modified list which now contains the running sum
        return nums
```
