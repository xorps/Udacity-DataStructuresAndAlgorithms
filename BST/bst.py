class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value
    def insert(self, node):
        assert isinstance(node, Node)
        if node < self:
            if self.left: self.left.insert(node)
            else: self.left = node
        elif node > self:
            if self.right: self.right.insert(node)
            else: self.right = node
    def search(self, value):
        assert isinstance(value, int)
        if value == self.value: return self
        if value < self.value:
            if self.left: return self.left.search(value)
            return None
        if self.right: return self.right.search(value)
        return None
    def search_v2(self, parent, value):
        if value == self.value: return parent, self
        if value < self.value:
            if self.left: return self.left.search_v2(self, value)
            return None, None
        if self.right: return self.right.search_v2(self, value)
        return None, None
    def num_children(self):
        n = 0
        if self.left: n += 1
        if self.right: n += 1
        return n
    def set_child(self, old, new):
        if self.left is old:
            self.left = new
        elif self.right is old:
            self.right = new
    def delete(self, value):
        parent, node = self.search_v2(None, value)
        if not node: return
        n = node.num_children()
        # case 1: leaf node
        if n == 0:
            parent.set_child(node, None)
        # case 2: node has one child node
        elif n == 1:
            child = node.left if node.left else node.right
            parent.set_child(node, child)
        # case 3: node has two child nodes
        else:
            parent.set_child(node, None)
            parent.insert(node.left)
            parent.insert(node.right)
    def bfs(self, visit):
        queue = []
        queue.append((0, self))
        while len(queue) > 0:
            level, node = queue.pop(0)
            visit(level, node)
            if node.left: queue.append((level + 1, node.left))
            if node.right: queue.append((level + 1, node.right))
    def print(self):
        class State:
            def __init__(self):
                self.prev_level = -1
        state = State()
        def visit(level, node):
            if state.prev_level != level:
                state.prev_level = level
                print()
                print('(' + str(level) + ') ', end='')
            print(' ' + str(node.value) + ' ', end='')
        self.bfs(visit)
        print()

def test():
    t = Node(5)

    three = Node(3)
    six = Node(6)

    t.insert(three)
    t.insert(six)
    t.insert(Node(4))
    t.insert(Node(7))
    t.insert(Node(8))
    t.insert(Node(2))
    
    assert t.search(3) is three
    assert t.search(6) is six

    t.print()
    t.delete(4)
    t.print()

test()