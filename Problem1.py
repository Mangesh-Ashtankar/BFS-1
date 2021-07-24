# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# iterative
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
        
#         queue, out = [],[]
#         queue.append(root)
        
#         while len(queue)>0:
#             n = len(queue)
#             temp = []
#             for i in range(n):
#                 node = queue.pop(0)
#                 temp.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             out.append(temp)
            
#         return out
    #     space = O(n)
    # time = (n)
