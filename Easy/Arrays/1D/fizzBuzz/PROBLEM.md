# Problem: FizzBuzz

## Problem Statement

Given an integer `n`, return a list of strings representing numbers from `1` to `n` with the following rules:

1. For multiples of `3`, append `"Fizz"` instead of the number.
2. For multiples of `5`, append `"Buzz"` instead of the number.
3. For numbers which are multiples of both `3` and `5`, append `"FizzBuzz"`.
4. For all other numbers, append the number itself as a string.

### Example:

#### Input:

```
n = 15

```

#### Output:

```
["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

```

---

## Approach

We iterate through numbers from `1` to `n` and use string concatenation to build the FizzBuzz output. Instead of using multiple conditional checks, we construct the result string in the following steps:

1. Initialize an empty string for each number.
2. If the number is divisible by `3`, append `"Fizz"` to the string.
3. If the number is divisible by `5`, append `"Buzz"` to the string.
4. If the string is still empty, it means the number is neither divisible by `3` nor `5`, so we append the number itself as a string.
5. Append the resulting string to the result list.

---

## Code

```python
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            fizzbuzz_str = ""
            if i % 3 == 0:
                fizzbuzz_str += "Fizz"
            if i % 5 == 0:
                fizzbuzz_str += "Buzz"
            if fizzbuzz_str == "":
                fizzbuzz_str = str(i)
            result.append(fizzbuzz_str)
        return result
```
