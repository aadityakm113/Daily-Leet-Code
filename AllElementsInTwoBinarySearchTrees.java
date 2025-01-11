// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.swing.tree.TreeNode;

public class AllElementsInTwoBinarySearchTrees {
   public void inorder(List<Integer> l,TreeNode node){
        if(node==null){
            return;
        }
        else{
            inorder(l,node.left);
            l.add(node.val);
            inorder(l,node.right);
        }
        // return l;

    }
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> lst = new ArrayList<>();
        inorder(lst,root1);
        inorder(lst,root2);
        Collections.sort(lst);
        return lst;
        
    } 
}
