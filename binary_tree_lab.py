from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    # if there is no node, the depth is 0
    if root is None:
        return 0

    # find the depth of the left and right sides
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # take the bigger one and add 1 for the current node
    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # if the tree is empty there is no ancestor
    if root is None:
        return None

    # if both p and q are smaller than root, go left
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # if both p and q are bigger than root, go right
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    # otherwise the root is where they split, so it is the answer
    return root