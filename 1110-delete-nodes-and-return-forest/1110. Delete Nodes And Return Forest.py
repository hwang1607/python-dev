# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        res = []
        to_delete = set(to_delete)
        
        def helper(root):
            if not root:
                return None


            root.left = helper(root.left)
            root.right = helper(root.right)

            if root.val in to_delete:
                print("d")
                if root.left:
                    print("d")

                    res.append(root.left)
                    print(res)
                if root.right:
                    res.append(root.right)
                return None
            return root

        if helper(root):
            res.append(root)
        return res


