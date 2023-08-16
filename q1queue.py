# Question 1: Jumping The Queue

# A]
from collections import deque

queue = deque()

with open("hw3_q1.txt", "r") as f:
    for line in f:
        action, name = line.split()
        if action == "JOIN":
            queue.append(name)
        elif action == "JUMP":
            queue.appendleft(name)
f.close()

print(list(queue))

# B] Time complexity:
# This solution runs in O(n) time (or "linear time"), where n is the number of items in the file.
# This is because you need to read each line and perform either a constant time O(1) operation (append or appendleft) or a linear time O(n) operation (split) on the deque.
# The total time complexity is the sum of the time complexities of each operation, which is O(n) + O(1) + O(n) = O(2n + 1).
# When calculating the big O complexity, the constants are thrown out so the time complexity is O(n)

# Space complexity:
# O(n), where n is the number of lines in the file.
# This is because you need to store each line in the deque, which takes O(n) space.
# The space complexity does not depend on the operations performed on the deque, but only on the size of the deque.

# Assumptions:
# The append and appendleft methods of the deque class take constant time O(1) to add an element to the right or left end of the deque.
# The appendleft method also shifts all existing elements to the right by one position, which does not affect time complexity.
# The list function takes linear time O(n) to convert an iterable object, such as a deque, into a list.
# The list function also creates a new list object, which takes O(n) space.