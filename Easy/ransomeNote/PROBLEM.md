# Problem: Ransom Note

## Problem Statement

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed from the letters in `magazine`. Each letter in `magazine` can only be used once in `ransomNote`.

### Example 1:

#### Input:

`ransomNote = "a" magazine = "b"`

#### Output:

`false`

**Explanation:**

- There is no 'a' in the magazine to construct the ransom note.

### Example 2:

#### Input:

` ransomNote = "aa" magazine = "ab"`

#### Output:

`false`

**Explanation:**

- The magazine contains only one 'a', but two 'a's are required to construct the ransom note.

### Example 3:

#### Input:

`ransomNote = "aa" magazine = "aab"`

#### Output:

`true`

**Explanation:**

- The magazine contains two 'a's and one 'b', which are enough to construct the ransom note.

---

## Approach

We can solve this problem by counting the occurrences of each character in both the `ransomNote` and `magazine`. We then check if all the characters in the ransom note can be found in the magazine in the necessary quantities.

### Steps:

1. Use a `Counter` to count the occurrences of each character in the ransom note and the magazine.
2. Iterate over the ransom note's character counts and compare them with the counts in the magazine:
   - If any character is missing in the magazine or its count is less than the required count in the ransom note, return `False`.
3. If all characters are present in the required quantities, return `True`.

---

## Code

```python
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        return True
```
