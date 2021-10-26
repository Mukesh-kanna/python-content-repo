class BTNode:
    """Binary Tree Node Structure."""

    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


"""
    Different different traversal techniques for binary tree.
    1. Preorder traversal
    2. Inorder traversal
    3. Postorder traversal
"""


def printPreorder(root):
    """Function for printing preorder travelsal of binary tree."""
    if root:
        print(root.data, end=" ")
        printPreorder(root.left)
        printPreorder(root.right)


def printInorder(root):
    """Function for printing inorder travelsal of binary tree."""
    if root:
        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)


def printPostorder(root):
    """Function for printing postorder travelsal of binary tree."""
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data, end=" ")


def main():
    """
    Tree:
                1
              /  \
            2      3
           / \    / \
          4   5  6   7
         / \    / \
        8   9  10 11
    """
    root = BTNode(
        1,
        BTNode(2, BTNode(4, BTNode(8), BTNode(9)), BTNode(5)),
        BTNode(3, BTNode(6, BTNode(10), BTNode(11)), BTNode(7)),
    )

    print("Preorder Traversal:")
    printPreorder(root)
    print("\n")

    print("Inorder Traversal:")
    printInorder(root)
    print("\n")

    print("Postorder Traversal:")
    printPostorder(root)
    print("\n")


if __name__ == "__main__":
    main()
