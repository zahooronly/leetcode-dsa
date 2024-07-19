class Solution:
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxWealthOfCustomer = 0
        for customer in accounts:
            currentCustomerWealth = sum(customer)
            maxWealthOfCustomer = max(maxWealthOfCustomer, currentCustomerWealth)
        return maxWealthOfCustomer
