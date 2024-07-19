# Problem: Richest Customer Wealth

## Problem Statement

You are given a 2D list `accounts` where `accounts[i][j]` represents the wealth of the `i`-th customer in the `j`-th bank. Your task is to find the wealthiest customer, where a customer's total wealth is defined as the sum of the money they have across all their bank accounts.

Return the wealth of the richest customer.

### Example:

#### Input:

```
accounts = [[1, 2, 3], [3, 2, 1]]

```

#### Output:

```
6
```

**Explanation:**

- Customer 1 has a total wealth of `1 + 2 + 3 = 6`.
- Customer 2 has a total wealth of `3 + 2 + 1 = 6`.

Both customers have a wealth of `6`, so the output is `6`.

---

## Approach

The approach to solving this problem involves iterating through each customer's accounts and calculating their total wealth. We keep track of the maximum wealth encountered during this iteration.

### Steps Involved:

1. Initialize a variable `maxWealthOfCustomer` to keep track of the maximum wealth encountered, starting from `0`.
2. For each customer (represented as a list of integers), calculate their total wealth by summing up their accounts.
3. Update `maxWealthOfCustomer` with the maximum of the current customer's wealth and the current maximum.
4. Return `maxWealthOfCustomer` after iterating through all the customers.

---

## Code

```python
class Solution:
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxWealthOfCustomer = 0
        for customer in accounts:
            currentCustomerWealth = sum(customer)  # Sum of all banks for current customer
            maxWealthOfCustomer = max(maxWealthOfCustomer, currentCustomerWealth)
        return maxWealthOfCustomer
```
