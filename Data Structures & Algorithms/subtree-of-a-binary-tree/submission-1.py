class Solution:
    def check_subtree(self, node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        if node1.val != node2.val:
            return False

        return (
            self.check_subtree(node1.left, node2.left)
            and self.check_subtree(node1.right, node2.right)
        )

    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True

        if not root:
            return False

        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.val == subRoot.val:
                if self.check_subtree(node, subRoot):
                    return True

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False