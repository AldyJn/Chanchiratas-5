test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value) -> bool:
        if self.root is None:
            self.root = TreeNode(value)
            return True
        
        current = self.root
        while current:
            if value == current.value:
                return False     # Value already exists
            elif value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    return True
                current = current.right

    def search(self, value) -> bool:
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def update(self, old_value, new_value) -> bool:
        if not self.delete(old_value):
            return False
        self.insert(new_value)
        return True

    def delete(self, value) -> bool:
        parent = None
        current = self.root
        
        # Find the node to delete and its parent
        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        
        if not current:
            return False  # Value not found
        
        # Case 1: Node has no children or only one child
        if current.left is None or current.right is None:
            new_child = current.left if current.left else current.right
            
            if parent is None:
                self.root = new_child
            elif parent.left == current:
                parent.left = new_child
            else:
                parent.right = new_child
        
        # Case 2: Node has two children
        else:
            # Find the inorder successor (smallest in right subtree)
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            # Replace current's value with successor's value
            current.value = successor.value
            
            # Remove the successor (which has at most one right child)
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        
        return True
def test_o7_1():
    # o7.1.1 Insert & Search
    bst = BinarySearchTree()
    record_test("o7.1.1 insert/find",
        bst.insert(5) is True and bst.insert(3) and bst.insert(7)
        and bst.search(3) is True and bst.search(8) is False
    )
    # o7.1.2 Update Existing
    bst = BinarySearchTree()
    for v in [10,5,15]: bst.insert(v)
    record_test("o7.1.2 update",
        bst.update(5,6) is True and bst.search(6) and not bst.search(5)
    )
    # o7.1.3 Delete Leaf & One/Two-Child
    bst = BinarySearchTree()
    for v in [20,10,30,5,15]: bst.insert(v)
    record_test("o7.1.3 delete",
        bst.delete(5) and bst.delete(30) and bst.delete(10)
        and not bst.search(5) and not bst.search(30) and not bst.search(10)
    )
    # o7.1.4 Validation: Duplicate Insert
    bst = BinarySearchTree()
    bst.insert(2)
    record_test("o7.1.4 dup insert",
        bst.insert(2) is False and bst.search(2) is True
    )
    # o7.1.5 Return-Type Verification
    bst = BinarySearchTree()
    record_test("o7.1.5 types",
        isinstance(bst.insert(1), bool)
        and isinstance(bst.update(1,2), bool)
        and isinstance(bst.delete(1), bool)
    )

# 🚀 Run tests
test_o7_1()

# 📋 Summary
for r in test_results:
    print(r)