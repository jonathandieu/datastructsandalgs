class binaryTreeTraversal
{
    public List<Integer> inorderTraversal(TreeNode root) {
        // EXAMPLE:    1
            //              \
            //               2
            //              /
            //             3
            //            / \
            //          null null

            // Function call 1: [1, ]
            // First recursive call: [2,]
            // Second recursive call: [3, ]
            List traversal = new ArrayList<Integer>();
            // Base Case where we've reached the bottom of the tree
            if (root == null)
                return traversal;
            else
            {
                traversal.addAll((inorderTraversal(root.left))); // Left
                traversal.add(root.val); // Middle
                traversal.addAll((inorderTraversal(root.right))); // Right
            }
            return traversal; // Complete list
        }
}