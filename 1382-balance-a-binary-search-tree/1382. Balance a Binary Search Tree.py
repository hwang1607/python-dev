class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: collect values using inorder traversal (sorted for BST)
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        # Step 2: build a balanced BST from sorted values
        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(values[mid])

            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(values) - 1)