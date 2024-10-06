# Problem: Middle of the Linked List

## Problem Statement

Given the head of a singly linked list, return the middle node of the list. If there are two middle nodes, return the second middle node.

### Example 1:

#### Input:

```
head = [1, 2, 3, 4, 5]
```

#### Output:

```
Node with value 3
```

**Explanation:**

- The list has 5 nodes, so the middle node is the 3rd one (value 3).

### Example 2:

#### Input:

```
head = [1, 2, 3, 4, 5, 6]
```

#### Output:

```
Node with value 4
```

**Explanation:**

- The list has 6 nodes, so the middle node is the 4th one (value 4), since we return the second middle node when there are two.

---

## Approach

We solve this problem using the **two-pointer technique**:

1. **Slow pointer**: This pointer moves one node at a time.
2. **Fast pointer**: This pointer moves two nodes at a time.

By the time the fast pointer reaches the end of the list, the slow pointer will be at the middle node. This works efficiently because the fast pointer traverses the list at twice the speed of the slow pointer.

### Steps:

1. Initialize both `slow` and `fast` pointers at the head of the list.
2. Move the `fast` pointer two steps at a time and the `slow` pointer one step at a time.
3. When the `fast` pointer reaches the end (or null), the `slow` pointer will be at the middle node.
4. Return the `slow` pointer.

---

## Code

```python
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```
