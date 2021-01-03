class BST:
    def __init__(self, head):
        self.head = head

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def insert(self, node, val):
        if not node:
            return Node(val)

        else:

            if (val) < (node.data):
                node.left = self.insert(node.left, val)
            else:
                node.right = self.insert(node.right, val)

        return node


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


tree = BST(Node(5))
tree.insert(tree.head, 4)
tree.insert(tree.head, 6)

tree.inorder(tree.head)
