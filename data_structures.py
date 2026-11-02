"""Core data structures: Binary Search Tree and Priority Queue (min-heap)."""


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    """Binary Search Tree keyed by roll number."""

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, value):
        """Insert a record. If the key exists, its value is updated."""
        if self.root is None:
            self.root = BSTNode(key, value)
            self.size += 1
            return
        node = self.root
        while True:
            if key == node.key:
                node.value = value
                return
            side = "left" if key < node.key else "right"
            nxt = getattr(node, side)
            if nxt is None:
                setattr(node, side, BSTNode(key, value))
                self.size += 1
                return
            node = nxt

    def search(self, key):
        """Return the value for key, or None if not found."""
        node = self.root
        while node:
            if key == node.key:
                return node.value
            node = node.left if key < node.key else node.right
        return None

    def delete(self, key):
        """Delete a record. Returns True if it existed."""
        self.root, removed = self._delete(self.root, key)
        if removed:
            self.size -= 1
        return removed

    def _delete(self, node, key):
        if node is None:
            return None, False
        if key < node.key:
            node.left, removed = self._delete(node.left, key)
            return node, removed
        if key > node.key:
            node.right, removed = self._delete(node.right, key)
            return node, removed
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True
        succ = node.right
        while succ.left:
            succ = succ.left
        node.key, node.value = succ.key, succ.value
        node.right, _ = self._delete(node.right, succ.key)
        return node, True

    def inorder(self):
        """Return all values sorted by key."""
        out, stack, node = [], [], self.root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            out.append(node.value)
            node = node.right
        return out

    def __len__(self):
        return self.size


class PriorityQueue:
    """Min-heap priority queue: the smallest priority is served first."""

    def __init__(self):
        self._heap = []

    def push(self, priority, item):
        self._heap.append((priority, item))
        i = len(self._heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self._heap[parent][0] <= self._heap[i][0]:
                break
            self._heap[parent], self._heap[i] = self._heap[i], self._heap[parent]
            i = parent

    def pop(self):
        if not self._heap:
            raise IndexError("pop from empty priority queue")
        top = self._heap[0]
        last = self._heap.pop()
        if self._heap:
            self._heap[0] = last
            i, n = 0, len(self._heap)
            while True:
                l, r, s = 2 * i + 1, 2 * i + 2, i
                if l < n and self._heap[l][0] < self._heap[s][0]:
                    s = l
                if r < n and self._heap[r][0] < self._heap[s][0]:
                    s = r
                if s == i:
                    break
                self._heap[s], self._heap[i] = self._heap[i], self._heap[s]
                i = s
        return top

    def is_empty(self):
        return not self._heap

    def __len__(self):
        return len(self._heap)
