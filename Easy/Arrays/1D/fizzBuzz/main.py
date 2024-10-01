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
