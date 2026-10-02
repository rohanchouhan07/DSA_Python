class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        self.index = 0
        
        def buildBST(left, right):
            if left > right:
                return None
            
            # Build left subtree first
            mid = (left + right) // 2
            
            leftNode = buildBST(left, mid - 1)
            
            # Create node with current element
            root = TreeNode(nums[self.index])
            self.index += 1
            
            # Build right subtree
            root.left = leftNode
            root.right = buildBST(mid + 1, right)
            
            return root
        
        return buildBST(0, len(nums) - 1)