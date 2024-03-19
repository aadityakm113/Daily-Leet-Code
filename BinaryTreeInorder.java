// https://leetcode.com/problems/binary-tree-inorder-traversal/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class BinaryTreeInorder {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list= new ArrayList<>();
        if(root==null){
            return list;
        }
        return inorderTraversal(root,list);
    }
    private List<Integer> inorderTraversal(TreeNode root, List<Integer> list){
        if(root!=null){
        inorderTraversal(root.left,list);
        list.add(root.val);
        System.out.println(root.val+" ");
        inorderTraversal(root.right,list);
        
        }
        return list;
    }
    
}