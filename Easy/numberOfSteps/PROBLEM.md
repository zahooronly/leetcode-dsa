# Problem: Number of Steps to Reduce a Number to Zero

## Problem Statement

Given an integer `num`, the task is to return the number of steps to reduce the number to zero. In each step, you can do one of the following:

1. If the current number is even, divide it by 2.
2. If the current number is odd, subtract 1 from it.

### Example:

#### Input:

```
num = 14
```

#### Output:

```
6
```

**Explanation:**

- Step 1: 14 is even, divide by 2 -> 7
- Step 2: 7 is odd, subtract 1 -> 6
- Step 3: 6 is even, divide by 2 -> 3
- Step 4: 3 is odd, subtract 1 -> 2
- Step 5: 2 is even, divide by 2 -> 1
- Step 6: 1 is odd, subtract 1 -> 0

Thus, it took 6 steps to reduce `14` to `0`.

---

## Approach

We follow the problem statement by using a `while` loop that continues until `num` becomes `0`. In each iteration:

1. **If the number is even**, divide it by 2.
2. **If the number is odd**, subtract 1 from it.
3. Count each step until `num` reaches `0`.

---

## Code

```python
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps

```

