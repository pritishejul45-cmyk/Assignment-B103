# 1. Find the second-largest unique element without sort() or max()
'''
numbers = [10, 20, 30, 30, 40, 50]

first = float('-inf')
second = float('-inf')

for n in numbers:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

print("Second largest:", second)
'''

# 2. Find all pairs whose sum equals target
'''
numbers = [2, 4, 3, 5, 7, 8]
target = 10

seen = set()

for n in numbers:
    diff = target - n

    if diff in seen:
        print(diff, n)

    seen.add(n)
    '''

# 3. Move all zeros to the end
'''
numbers = [0, 1, 0, 3, 12]

result = []

for n in numbers:
    if n != 0:
        result.append(n)

zeros = numbers.count(0)

result.extend([0] * zeros)

print(result)
'''

# 4. Find the missing number from 1 to N
'''
numbers = [1, 2, 4, 5, 6]

n = 6

total = n * (n + 1) // 2

missing = total - sum(numbers)

print("Missing number:", missing)
'''

# 5. Find duplicate elements without nested loops
'''
numbers = [1, 2, 3, 2, 4, 5, 3]

seen = set()
duplicates = set()

for n in numbers:
    if n in seen:
        duplicates.add(n)
    else:
        seen.add(n)

print(list(duplicates))
'''

# 6. Find the first non-repeating character
'''
text = "abccba"

char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

for char in text:
    if char_count[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found")
'''

# 7. Check whether two strings are anagrams without sorted()
'''
str1 = "listen"
str2 = "silent"

if len(str1) != len(str2):
    print("Not Anagram")
else:
    count = {}

    for ch in str1:
        count[ch] = count.get(ch, 0) + 1

    for ch in str2:
        count[ch] = count.get(ch, 0) - 1

    if all(value == 0 for value in count.values()):
        print("Anagram")
    else:
        print("Not Anagram")
        '''
# 8. Merge two sorted arrays without sort()
'''
a = [1, 3, 5]
b = [2, 4, 6]

result = []

i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result.extend(a[i:])
result.extend(b[j:])

print(result)
'''
# 9. Rotate an array to the right by K positions
'''
numbers = [1, 2, 3, 4, 5]
k = 2

k = k % len(numbers)

result = numbers[-k:] + numbers[:-k]

print(result)
'''

# 10. Find intersection of two arrays including duplicates
'''
a = [1, 2, 2, 3, 4]
b = [2, 2, 3, 5]

result = []

for n in a:
    if n in b:
        result.append(n)
        b.remove(n)

print(result)
'''

# 11. Find maximum sum of a contiguous subarray
'''
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current = numbers[0]
maximum = numbers[0]

for n in numbers[1:]:
    current = max(n, current + n)
    maximum = max(maximum, current)

print("Maximum sum:", maximum)
'''

# 12. Find longest substring without repeating characters
'''
text = "abcabcbb"

seen = {}
start = 0
longest = 0

for i, ch in enumerate(text):
    if ch in seen and seen[ch] >= start:
        start = seen[ch] + 1

    seen[ch] = i

    longest = max(longest, i - start + 1)

print("Longest length:", longest)
'''

# 13. Find longest common prefix
'''
words = ["flower", "flow", "flight"]

prefix = words[0]

for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Common prefix:", prefix)
'''

#14. Group strings into anagram groups
'''
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = tuple(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print(list(groups.values()))
'''

# 15. Find Kth largest unique element in a list
'''
numbers = [3, 2, 1, 5, 6, 4]
k = 2

unique = list(set(numbers))

for i in range(k):
    largest = unique[0]

    for n in unique:
        if n > largest:
            largest = n

    if i == k - 1:
        print("Kth largest:", largest)

    unique.remove(largest)
    '''

# 16. Check balanced parentheses using stack
'''
expression = "((()))"

stack = []

for ch in expression:
    if ch == '(':
        stack.append(ch)
    elif ch == ')':
        if not stack:
            print("Not Balanced")
            break
        stack.pop()
else:
    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")
'''

# 17. Find all subarrays whose sum equals target
'''
numbers = [1, 2, 3, 2, 1]
target = 5

for i in range(len(numbers)):
    total = 0

    for j in range(i, len(numbers)):
        total += numbers[j]

        if total == target:
            print(numbers[i:j+1])
            '''

# 18. Merge overlapping intervals
'''
intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

intervals.sort()

result = [intervals[0]]

for start, end in intervals[1:]:
    last = result[-1]

    if start <= last[1]:
        last[1] = max(last[1], end)
    else:
        result.append([start, end])

print(result)
'''

# 19. Search in a rotated sorted array

numbers = [4, 5, 6, 7, 0, 1, 2]
target = 0

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Index:", mid)
        break

    if numbers[left] <= numbers[mid]:
        if numbers[left] <= target < numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1

    else:
        if numbers[mid] < target <= numbers[right]:
            left = mid + 1
        else:
            right = mid - 1

else:
    print("Not Found")

# 20. Find longest consecutive sequence
'''
numbers = [100, 4, 200, 1, 3, 2]

num_set = set(numbers)
longest = 0

for n in num_set:
    if n - 1 not in num_set:
        count = 1
        current = n

        while current + 1 in num_set:
            current += 1
            count += 1

        longest = max(longest, count)

print("Longest sequence:", longest)
'''

# 21. Find trapped rainwater between elevation bars
'''
height = [4, 2, 0, 3, 2, 5]

left = 0
right = len(height) - 1

left_max = 0
right_max = 0
water = 0

while left < right:

    if height[left] < height[right]:

        if height[left] >= left_max:
            left_max = height[left]
        else:
            water += left_max - height[left]

        left += 1

    else:
        if height[right] >= right_max:
            right_max = height[right]
        else:
            water += right_max - height[right]

        right -= 1

print("Trapped water:", water)
'''

# 22. Find median of two sorted arrays
'''
a = [1, 3]
b = [2]

merged = []

i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

merged.extend(a[i:])
merged.extend(b[j:])

n = len(merged)

if n % 2 == 1:
    median = merged[n // 2]
else:
    median = (merged[n // 2 - 1] + merged[n // 2]) / 2

print("Median:", median)

'''
# 23. Find maximum product of contiguous subarray
'''
numbers = [2, 3, -2, 4]

maximum = numbers[0]
minimum = numbers[0]
result = numbers[0]

for n in numbers[1:]:

    if n < 0:
        maximum, minimum = minimum, maximum

    maximum = max(n, maximum * n)
    minimum = min(n, minimum * n)

    result = max(result, maximum)

print("Maximum product:", result)
'''

# 24. Find smallest missing positive integer
'''
numbers = [3, 4, -1, 1]

num_set = set(numbers)

missing = 1

while missing in num_set:
    missing += 1

print("Smallest missing:", missing)
'''

# 25. Count subarrays whose sum equals K
'''
numbers = [1, 1, 1]
k = 2

count = 0
total = 0

prefix = {0: 1}

for n in numbers:
    total += n

    count += prefix.get(total - k, 0)

    prefix[total] = prefix.get(total, 0) + 1

print("Count:", count)
'''

# 26. Find longest increasing subsequence
'''
numbers = [10, 9, 2, 5, 3, 7, 101, 18]

dp = [1] * len(numbers)

for i in range(len(numbers)):
    for j in range(i):

        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print("Longest length:", max(dp))
'''

# 27. Coin Change using Dynamic Programming
'''
coins = [1, 2, 5]
amount = 11

dp = [float('inf')] * (amount + 1)

dp[0] = 0

for coin in coins:
    for i in range(coin, amount + 1):

        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[amount] == float('inf'):
    print(-1)
else:
    print("Minimum coins:", dp[amount])
    '''

# 28. Word Break using Dynamic Programming

text = "leetcode"

words = ["leet", "code"]

dp = [False] * (len(text) + 1)

dp[0] = True

for i in range(1, len(text) + 1):
    for j in range(i):

        if dp[j] and text[j:i] in words:
            dp[i] = True
            break

print(dp[len(text)])

# 29. Minimum jumps to reach last index
'''
numbers = [2, 3, 1, 1, 4]

jumps = 0
current_end = 0
farthest = 0

for i in range(len(numbers) - 1):

    farthest = max(farthest, i + numbers[i])

    if i == current_end:
        jumps += 1
        current_end = farthest

print("Minimum jumps:", jumps)
'''

# 30. Maximum stock profit with multiple transactions
'''
prices = [7, 1, 5, 3, 6, 4]

profit = 0

for i in range(1, len(prices)):

    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]

print("Maximum profit:", profit)
'''

# 31. Implement LRU Cache with O(1) get() and put()
'''
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):

        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))

cache.put(3, 30)

print(cache.get(2))
print(cache.get(3))
'''

# 32. Implement Min Stack
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


s = MinStack()

s.push(5)
s.push(3)
s.push(7)

print(s.getMin())
print(s.top())

s.pop()

print(s.getMin())
'''

# 33. Find number of islands using DFS
'''
grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]

rows = len(grid)
cols = len(grid[0])

def dfs(r, c):

    if (r < 0 or r >= rows or
        c < 0 or c >= cols or
        grid[r][c] == 0):
        return

    grid[r][c] = 0

    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)


count = 0

for i in range(rows):
    for j in range(cols):

        if grid[i][j] == 1:
            count += 1
            dfs(i, j)

print("Number of islands:", count)
'''

# 34. Shortest path using Dijkstra's Algorithm
'''
import heapq

graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 1)],
    'C': [('B', 2), ('D', 5)],
    'D': []
}

distances = {node: float('inf') for node in graph}

distances['A'] = 0

pq = [(0, 'A')]

while pq:

    distance, node = heapq.heappop(pq)

    if distance > distances[node]:
        continue

    for neighbor, weight in graph[node]:

        new_distance = distance + weight

        if new_distance < distances[neighbor]:

            distances[neighbor] = new_distance

            heapq.heappush(pq, (new_distance, neighbor))

print(distances)
'''

# 35. Detect cycle in directed and undirected graph
'''
graph = {
    0: [1],
    1: [0, 2],
    2: [1, 0]
}

visited = set()

def has_cycle(node, parent):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:
            if has_cycle(neighbor, node):
                return True

        elif neighbor != parent:
            return True

    return False


print(has_cycle(0, -1))
'''

# 36. Implement Topological Sorting
'''
from collections import deque

graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

indegree = {node: 0 for node in graph}

for node in graph:
    for neighbor in graph[node]:
        indegree[neighbor] += 1

queue = deque()

for node in graph:
    if indegree[node] == 0:
        queue.append(node)

result = []

while queue:

    node = queue.popleft()
    result.append(node)

    for neighbor in graph[node]:

        indegree[neighbor] -= 1

        if indegree[neighbor] == 0:
            queue.append(neighbor)

if len(result) == len(graph):
    print(result)
else:
    print("Cycle exists")
    '''

# 37. Solve N-Queens using Backtracking
'''
def solve(n):

    board = [["."] * n for _ in range(n)]

    result = []

    def backtrack(row):

        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):

            safe = True

            for r in range(row):
                if board[r][col] == "Q":
                    safe = False

                if (row - r == abs(col - board[r].index("Q"))
                    and "Q" in board[r]):
                    safe = False

            if safe:
                board[row][col] = "Q"

                backtrack(row + 1)

                board[row][col] = "."

    backtrack(0)

    return result


print(solve(4))
'''

# 38. Generate all permutations without duplicates
'''
def permutations(text):

    result = []

    def backtrack(path, remaining):

        if not remaining:
            result.append(path)
            return

        for i in range(len(remaining)):

            if i > 0 and remaining[i] == remaining[i - 1]:
                continue

            backtrack(
                path + remaining[i],
                remaining[:i] + remaining[i + 1:]
            )

    backtrack("", "".join(sorted(text)))

    return result


print(permutations("aab"))
'''

# 39. Serialize and deserialize a binary tree
'''
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def serialize(root):

    if not root:
        return "#"

    return (
        str(root.value) + "," +
        serialize(root.left) + "," +
        serialize(root.right)
    )


def deserialize(data):

    values = iter(data.split(","))

    def build():

        value = next(values)

        if value == "#":
            return None

        node = Node(int(value))

        node.left = build()
        node.right = build()

        return node

    return build()


root = Node(1)
root.left = Node(2)
root.right = Node(3)

data = serialize(root)

print(data)

new_root = deserialize(data)

print(new_root.value)
'''

# 40. Find Lowest Common Ancestor in Binary Tree
'''
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lca(root, p, q):

    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    return left if left else right


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

answer = lca(root, root.left.left, root.left.right)

print("Lowest Common Ancestor:", answer.value)
'''