# 🧪 Registro de resultados
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# 🌳 Nodo del árbol
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

# 🌲 Árbol Binario de Búsqueda (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value) -> bool:
        def _insert(node, value):
            if node is None:
                return TreeNode(value), True
            if value == node.value:
                return node, False
            elif value < node.value:
                node.left, inserted = _insert(node.left, value)
            else:
                node.right, inserted = _insert(node.right, value)
            return node, inserted

        self.root, result = _insert(self.root, value)
        return result

    def search(self, value) -> bool:
        def _search(node, value):
            if node is None:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)

    def delete(self, value) -> bool:
        def _delete(node, value):
            if not node:
                return node, False
            if value < node.value:
                node.left, deleted = _delete(node.left, value)
            elif value > node.value:
                node.right, deleted = _delete(node.right, value)
            else:
                # Nodo encontrado
                if not node.left:
                    return node.right, True
                elif not node.right:
                    return node.left, True
                else:
                    # Dos hijos: buscar el sucesor
                    successor = node.right
                    while successor.left:
                        successor = successor.left
                    node.value = successor.value
                    node.right, _ = _delete(node.right, successor.value)
                    return node, True
            return node, deleted

        self.root, deleted = _delete(self.root, value)
        return deleted

    def update(self, old_value, new_value) -> bool:
        if self.search(old_value):
            if old_value == new_value:
                return True
            if not self.search(new_value):
                self.delete(old_value)
                self.insert(new_value)
                return True
            else:
                return False  # nuevo valor ya existe
        return False

# 🧪 Ejecutar los tests
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

# 🚀 Correr tests
test_o7_1()

# 📋 Mostrar resultados
for r in test_results:
    print(r)